import random

from typing import Any
from typing import List


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


class Group:
    def __init__(self, name: str, tags: Tags, args: List[List[str]]) -> None:
        self._name = name
        self._tags = tags
        self._args = args

    def tags_matches(self, other: Tags) -> bool:
        return self._tags.matches(other)

    def roll_args(self) -> str:
        result = []

        for arg_group in self._args:
            result.append(random.choice(arg_group))

        return ' '.join(result)


PREFIXES = [
    Group(
        name='Плоский фикс урон',
        tags=Tags(weapon=True),
        args=[
            [
                'Колющий',
                'Режущий',
                'Дробящий',
                'Огненный',
                'Холодом',
                'Молнией',
                'Звуком',
                'Кислотный',
                'Ядовитый',
                'Силовой',
                'Излучением',
                'Некротический',
                'Психический',
            ],
            [
                '2',
                '4',
                '6',
            ],
        ],
    ),
    Group(
        name='Плоский ранд урон',
        tags=Tags(weapon=True),
        args=[
            [
                'Колющий',
                'Режущий',
                'Дробящий',
                'Огненный',
                'Холодом',
                'Молнией',
                'Звуком',
                'Кислотный',
                'Ядовитый',
                'Силовой',
                'Излучением',
                'Некротический',
                'Психический',
            ],
            [
                '1d2',
                '1d4',
                '1d6',
            ],
        ],
    ),
]


def roll_prefix(tags: Tags) -> str:
    matching_groups = [g for g in PREFIXES if g.tags_matches(tags)]
    group = random.choice(matching_groups)
    return group.roll_args()
