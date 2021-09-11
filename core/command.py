from typing import Optional

from core import business
from core import types


class NotABotCommand(Exception):
    pass


class ParseError(Exception):
    pass


class Command:
    def __init__(self) -> None:
        pass

    def run(self) -> str:
        raise NotImplementedError()


class HelpCommand(Command):
    VERSION = '0.0.2'
    COMMON_COMMANDS = [
        'необычное [оружие|броня]',
        'редкое [оружие|броня]',
        'очень редкое [оружие|броня]',
        'слот [оружие|броня]',
        'префикс [оружие|броня]',
        'суффикс [оружие|броня]',
    ]

    def __init__(self, *, used_intentionally: bool) -> None:
        super().__init__()
        self._used_intentionally = used_intentionally

    def run(self) -> str:
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
    def __init__(self, tag: Optional[str] = None) -> None:
        super().__init__()
        self._tag = _parse_tag(tag)

    def run(self) -> str:
        raise NotImplementedError()


class PrefixCommand(CommandWithTag):
    def run(self) -> str:
        return str(business.roll_prefix(self._tag))


class SuffixCommand(CommandWithTag):
    def run(self) -> str:
        return str(business.roll_suffix(self._tag))


class SlotCommand(CommandWithTag):
    def run(self) -> str:
        return str(business.roll_slot(self._tag))


class CommandForItem(CommandWithTag):
    def run(self) -> str:
        result = []

        for _ in range(self._slots_count()):
            result.append(business.roll_slot(self._tag))

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


COMMAND_PREFIX = '!'
COMMAND_MAPPING = {
    'префикс': PrefixCommand,
    'суффикс': SuffixCommand,
    'слот': SlotCommand,
    'необычный': UncommonItemCommand,
    'необычная': UncommonItemCommand,
    'необычное': UncommonItemCommand,
    'редкий': RareItemCommand,
    'редкая': RareItemCommand,
    'редкое': RareItemCommand,
    'очень редкий': VeryRareItemCommand,
    'очень редкая': VeryRareItemCommand,
    'очень редкое': VeryRareItemCommand,
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
                return cls(*possible_args)
            except:
                return HelpCommand(used_intentionally=False)

        last_arg = possible_cmd.pop()
        possible_args.insert(0, last_arg)

    return HelpCommand(used_intentionally=False)


def _parse_tag(tag: Optional[str]) -> types.ItemTags:
    if tag is None:
        return types.ItemTags(universal=True)

    if tag in {'оружие', 'оружия'}:
        return types.ItemTags(weapon=True)

    if tag in {'броня', 'брони'}:
        return types.ItemTags(armor=True)

    raise ParseError()
