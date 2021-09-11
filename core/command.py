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
    VERSION = '0.20.2'

    COMMON_COMMANDS = [
        'предмет оружие|броня|кольцо [xN]',
        'необычное оружие|броня|кольцо [xN]',
        'редкое оружие|броня|кольцо [xN]',
        'очень редкое оружие|броня|кольцо [xN]',
        'слот оружие|броня|кольца [xN]',
        'префикс оружие|броня|кольца [xN]',
        'суффикс оружие|броня|кольца [xN]',
        'собственное свойство оружия|брони|кольца [xN]',
        'редкость [xN]',
        'ресурсы',
    ]

    def __init__(self, *, used_intentionally: bool, msg: Optional[str] = False) -> None:
        super().__init__()
        self._used_intentionally = used_intentionally
        self._msg = msg

    def run(self, ctx: business.Context) -> str:
        msg = []

        if self._used_intentionally:
            msg.append(f'Я создан для помощи в крафте предметов [version {self.VERSION}]')
        elif self._msg:
            msg.append(self._msg)
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
            raise ParseError('Нужно указать тип предмета: оружие, броня или кольцо')

    def run(self, ctx: business.Context) -> str:
        raise NotImplementedError()


class CommandWithTagXN(Command):
    DELIM = '\n'
    NUMERABLE = True

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

        if self.NUMERABLE:
            return self.DELIM.join(f'{i}. {m}' for i, m in enumerate(result, 1))

        return self.DELIM.join(f'{m}' for m in result)

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


class ItemCommand(CommandWithTagXN):
    DELIM = '\n\n'
    NUMERABLE = False

    def _run_one(self, ctx: business.Context) -> str:
        slots_mapping = {
            types.RarityType.Uncommon: 2,
            types.RarityType.Rare: 3,
            types.RarityType.VeryRare: 4,
        }

        rarity = business.roll_rarity(ctx)
        slots_count = slots_mapping[rarity]

        slots = [business.roll_slot(ctx, self._tag) for _ in range(slots_count)]
        slots.sort(key=lambda s: s.slot_type.value)

        slots_msg = '\n'.join(f'{i}. {s}' for i, s in enumerate(slots, 1))
        return f'{rarity}\n{slots_msg}'


class CommandForItemWithRarity(CommandWithTagXN):
    DELIM = '\n\n'
    NUMERABLE = False

    def _run_one(self, ctx: business.Context) -> str:
        result = [business.roll_slot(ctx, self._tag) for _ in range(self._slots_count())]
        result.sort(key=lambda s: s.slot_type.value)
        return '\n'.join(f'{i}. {s}' for i, s in enumerate(result, 1))

    def _slots_count(self) -> int:
        raise NotImplementedError()


class UncommonItemCommand(CommandForItemWithRarity):
    def _slots_count(self) -> int:
        return 2


class RareItemCommand(CommandForItemWithRarity):
    def _slots_count(self) -> int:
        return 3


class VeryRareItemCommand(CommandForItemWithRarity):
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
    'предмет': ItemCommand,
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
            except ParseError as exc:
                return HelpCommand(used_intentionally=False, msg=str(exc))
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

    if tag in {'кольцо', 'кольца'}:
        return types.ItemTags(jewellery=True)

    raise ParseError()


def _parse_xn(xn: str) -> int:
    # english and russian "x"
    if not (xn.startswith('x') or xn.startswith('х')):
        raise ParseError()

    n = int(xn[1:])
    if n <= 0:
        raise ParseError()

    return n
