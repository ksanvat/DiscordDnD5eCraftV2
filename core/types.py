import enum
import random

from typing import List


class ItemTags:
    def __init__(
            self,
            universal: bool = False,
            weapon: bool = False,
            armor: bool = False
    ) -> None:
        self._universal = universal

        self._tags = set()
        if weapon:
            self._tags.add('Weapon')
        if armor:
            self._tags.add('Armor')

    def matches(self, other: 'ItemTags') -> bool:
        if self._universal or other._universal:
            return True

        return bool(self._tags & other._tags)


class SlotType(enum.Enum):
    Prefix = enum.auto()
    Suffix = enum.auto()
    Implicit = enum.auto()


class Slot:
    def __init__(self, slot_type: SlotType, weight: int) -> None:
        self.type = slot_type
        self.weight = weight


class Property:
    def __init__(self, name: str, value: str) -> None:
        self.name = name
        self.value = value

    def __str__(self) -> str:
        return f'{self.name}: {self.value}'


class Group:
    def __init__(self, tags: ItemTags, type_args: List[str], value_args: List[str]) -> None:
        self._tags = tags
        self._type_args = type_args
        self._value_args = value_args

    def matches(self, other: ItemTags) -> bool:
        return self._tags.matches(other)

    def roll_args(self) -> Property:
        return Property(
            name=random.choice(self._type_args),
            value=random.choice(self._value_args),
        )
