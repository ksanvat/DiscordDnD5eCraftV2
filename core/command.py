from typing import Optional


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
    COMMON_COMMANDS = [
        'префикс',
        'суффикс',
    ]

    def __init__(self, *, intentional_usage: bool) -> None:
        super().__init__()
        self.intentional_usage = intentional_usage

    def run(self) -> str:
        msg = []

        if self.intentional_usage:
            msg.append('Я создан для помощи в крафте предметов')
        else:
            msg.append(f'Не понял тебя :(')

        msg += [
            'Что именно ты хочешь нароллить?',
            '',
        ]

        msg.extend(f'!{c}' for c in self.COMMON_COMMANDS)

        return '\n'.join(msg)


class PrefixCommand(Command):
    def run(self) -> str:
        return '<PrefixObject>'


class SuffixCommand(Command):
    def run(self) -> str:
        return '<SuffixCommand>'


COMMAND_PREFIX = '!'
COMMAND_MAPPING = {
    'префикс',
    'суффикс',
}


def parse(cmd: str) -> Optional[Command]:
    if not cmd.startswith(COMMAND_PREFIX):
        return None

    return _create_cmd(cmd[1:])


def _create_cmd(cmd: str) -> Command:
    if not cmd:
        return HelpCommand(intentional_usage=True)

    possible_cmd = cmd.strip().lower().split()
    possible_args = []

    while possible_cmd:
        cmd = ' '.join(possible_cmd)
        if cmd in COMMAND_MAPPING:
            cls = COMMAND_MAPPING[cmd]
            try:
                return cls(*possible_args)
            except:
                return HelpCommand(intentional_usage=False)

        last_arg = possible_cmd.pop()
        possible_args.insert(0, last_arg)

    return HelpCommand(intentional_usage=False)
