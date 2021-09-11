from typing import Optional

from core import business
from core import types

from typing import List


class ParseError(Exception):
    pass


class Command:
    def __init__(self) -> None:
        pass

    def run(self, ctx: business.Context) -> str:
        raise NotImplementedError()


class HelpCommand(Command):
    VERSION = '0.0.4'
    COMMON_COMMANDS = [
        'необычное [оружие|броня]',
        'редкое [оружие|броня]',
        'очень редкое [оружие|броня]',
        'слот [оружие|броня] [xN]',
        'префикс [оружие|броня] [xN]',
        'суффикс [оружие|броня] [xN]',
        'собственное свойство [оружия|брони] [xN]',
        'редкость [xN]',
        'ресурсы',
    ]

    def __init__(self, *, used_intentionally: bool) -> None:
        super().__init__()
        self._used_intentionally = used_intentionally

    def run(self, ctx: business.Context) -> str:
        msg = []

        if self._used_intentionally:
            msg.append(f'Я создан для помощи в крафте предметов [version {self.VERSION}]')
        else:
            msg.append(f'Не понял тебя :(')

        msg += [
            'Что именно ты хочешь нароллить?',
            '',
        ]

        msg.extend(f'!{c}' for c in self.COMMON_COMMANDS)

        return '\n'.join(msg)


class CommandWithTag(Command):
    def __init__(self, args: List[str]) -> None:
        super().__init__()

        try:
            self.tag = _parse_tag(args[0])
            args.pop(0)
        except:
            self.tag = types.ItemTags(universal=True)

    def run(self, ctx: business.Context) -> str:
        raise NotImplementedError()


class CommandWithTagXN(Command):
    def __init__(self, args: List[str]) -> None:
        super().__init__()

        self._cmd_with_tag = CommandWithTag(args)

        try:
            self._n = _parse_xn(args[0])
            args.pop(0)
        except:
            self._n = 1

    def run(self, ctx: business.Context) -> str:
        if self._n == 1:
            return self._run_one(ctx)

        result = [self._run_one(ctx) for _ in range(self._n)]
        return '\n'.join(f'{i}. {m}' for i, m in enumerate(result, 1))

    def _run_one(self, ctx: business.Context) -> str:
        raise NotImplementedError()

    @property
    def _tag(self) -> types.ItemTags:
        return self._cmd_with_tag.tag


class PrefixCommand(CommandWithTagXN):
    def _run_one(self, ctx: business.Context) -> str:
        return str(business.roll_prefix(ctx, self._tag))


class SuffixCommand(CommandWithTagXN):
    def _run_one(self, ctx: business.Context) -> str:
        return str(business.roll_suffix(ctx, self._tag))


class ImplicitCommand(CommandWithTagXN):
    def _run_one(self, ctx: business.Context) -> str:
        return str(business.roll_implicit(ctx, self._tag))


class SlotCommand(CommandWithTagXN):
    def _run_one(self, ctx: business.Context) -> str:
        return str(business.roll_slot(ctx, self._tag))


class RarityItemCommand(Command):
    def __init__(self, args: List[str]) -> None:
        super().__init__()

        try:
            self._n = _parse_xn(args[0])
            args.pop(0)
        except:
            self._n = 1

    def run(self, ctx: business.Context) -> str:
        result = [business.roll_rarity(ctx) for _ in range(self._n)]
        return '\n'.join(f'{i}. {s}' for i, s in enumerate(result, 1))

    @staticmethod
    def _rarity_str(rarity_type: types.RarityType) -> str:
        mapping = {
            types.RarityType.Uncommon: 'Необычный',
            types.RarityType.Rare: 'Редкий',
            types.RarityType.VeryRare: 'Очень редкий',
        }

        return mapping[rarity_type]


class CommandForItem(CommandWithTag):
    def run(self, ctx: business.Context) -> str:
        result = [business.roll_slot(ctx, self.tag) for _ in range(self._slots_count())]
        result.sort(key=lambda s: s.slot_type.value)
        return '\n'.join(f'{i}. {s}' for i, s in enumerate(result, 1))

    def _slots_count(self) -> int:
        raise NotImplementedError()


class UncommonItemCommand(CommandForItem):
    def _slots_count(self) -> int:
        return 2


class RareItemCommand(CommandForItem):
    def _slots_count(self) -> int:
        return 3


class VeryRareItemCommand(CommandForItem):
    def _slots_count(self) -> int:
        return 4


class ResourcesCommand(Command):
    def __init__(self, args: List[str]) -> None:
        super().__init__()

    def run(self, ctx: business.Context) -> str:
        msg = [
            'Сфера перемен: `&@%#&@#%&@&^@#@*(#&($`',
            'Сфера активных перемен: `#(*&#(*@(*%&(*!(`',
            'Сфера пассивных перемен: `@#)%*@#)%&*(#!@&$!#(`',
            'Сфера очищения: `#&@*%(@*$&!)$!*(!@#$`',
            'Сфера царей: `)#!*@)!#$)*!(&%#)!(*#&!`',
            'Сфера божества: `"!№%*%)(!"*%*)!()#!*#!$)$!*)(`',
            'Сфера...',
        ]

        return '\n\n'.join(f'- {row}' for row in msg)


COMMAND_PREFIX = '!'
COMMAND_MAPPING = {
    'префикс': PrefixCommand,
    'суффикс': SuffixCommand,
    'собственное': ImplicitCommand,
    'собственное свойство': ImplicitCommand,
    'слот': SlotCommand,
    'редкость': RarityItemCommand,
    'необычный': UncommonItemCommand,
    'необычная': UncommonItemCommand,
    'необычное': UncommonItemCommand,
    'редкий': RareItemCommand,
    'редкая': RareItemCommand,
    'редкое': RareItemCommand,
    'очень редкий': VeryRareItemCommand,
    'очень редкая': VeryRareItemCommand,
    'очень редкое': VeryRareItemCommand,
    'ресурс': ResourcesCommand,
    'ресурсы': ResourcesCommand,
}


def parse(cmd: str) -> Optional[Command]:
    if not cmd.startswith(COMMAND_PREFIX):
        return None

    return _create_cmd(cmd[1:])


def _create_cmd(cmd: str) -> Command:
    if not cmd:
        return HelpCommand(used_intentionally=True)

    possible_cmd = cmd.strip().lower().split()
    possible_args = []

    while possible_cmd:
        cmd = ' '.join(possible_cmd)
        if cmd in COMMAND_MAPPING:
            cls = COMMAND_MAPPING[cmd]
            try:
                command = cls(possible_args)
                if possible_args:
                    return HelpCommand(used_intentionally=False)

                return command
            except:
                return HelpCommand(used_intentionally=False)

        last_arg = possible_cmd.pop()
        possible_args.insert(0, last_arg)

    return HelpCommand(used_intentionally=False)


def _parse_tag(tag: str) -> types.ItemTags:
    if tag in {'оружие', 'оружия'}:
        return types.ItemTags(weapon=True)

    if tag in {'броня', 'брони'}:
        return types.ItemTags(armor=True)

    raise ParseError()


def _parse_xn(xn: str) -> int:
    if not xn.startswith('x'):
        raise ParseError()

    n = int(xn[1:])
    if n <= 0:
        raise ParseError()

    return n
