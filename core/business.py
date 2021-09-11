import random

from typing import List


class LogicError(Exception):
    pass


class Tags:
    def __init__(
            self,
            universal: bool = False,
            weapon: bool = False,
            armor: bool = False
    ) -> None:
        self._universal = universal

        self._tags = set()
        if weapon:
            self._tags.add('Оружие')
        if armor:
            self._tags.add('Броня')

    def matches(self, other: 'Tags') -> bool:
        if self._universal or other._universal:
            return True

        return bool(self._tags & other._tags)

    def __str__(self) -> str:
        if self._universal or not self._tags:
            return 'X'

        if len(self._tags) == 1:
            for tag in self._tags:
                return tag

        return str(self._tags)


class Group:
    def __init__(self, name: str, tags: Tags, args: List) -> None:
        self._name = name
        self._tags = tags
        self._args = args

    def tags_matches(self, other: Tags) -> bool:
        return self._tags.matches(other)

    def roll_args(self) -> str:
        result = []

        for arg_group in self._args:
            if isinstance(arg_group, str):
                result.append(arg_group)
            elif isinstance(arg_group, list):
                result.append(random.choice(arg_group))
            else:
                raise LogicError()

        return ' '.join(result)


PREFIXES = [
    Group(
        name='Плоский фикс урон',
        tags=Tags(weapon=True),
        args=[
            [
                'Колющее',
                'Режущее',
                'Дробящее',
                'Огненное',
                'Ледяное',
                'Электрическое',
                'Звуковое',
                'Кислотное',
                'Ядовитое',
                'Силовое',
                'Излучающее',
                'Некротическое',
                'Психическое',
            ],
            'Оружие',
            [
                '2 [dmg]',
                '4 [dmg]',
                '6 [dmg]',
            ],
        ],
    ),
    Group(
        name='Плоский ранд урон',
        tags=Tags(weapon=True),
        args=[
            [
                'Колющее',
                'Режущее',
                'Дробящее',
                'Огненное',
                'Ледяное',
                'Электрическое',
                'Звуковое',
                'Кислотное',
                'Ядовитое',
                'Силовое',
                'Излучающее',
                'Некротическое',
                'Психическое',
            ],
            'Оружие',
            [
                '1d2 [dmg]',
                '1d4 [dmg]',
                '1d6 [dmg]',
            ],
        ],
    ),
]


def roll_prefix(tags: Tags) -> str:
    matching_groups = [g for g in PREFIXES if g.tags_matches(tags)]
    group = random.choice(matching_groups)
    return group.roll_args()
