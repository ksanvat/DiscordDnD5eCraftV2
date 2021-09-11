import enum
import random
import uuid

from typing import List


class ItemTags:
    def __init__(
            self,
            universal: bool = False,
            weapon: bool = False,
            armor: bool = False,
            jewellery: bool = False,
    ) -> None:
        self._universal = universal

        self._tags = set()
        if weapon:
            self._tags.add('Weapon')
        if armor:
            self._tags.add('Armor')
        if jewellery:
            self._tags.add('Jewellery')

    def matches(self, other: 'ItemTags') -> bool:
        if self._universal or other._universal:
            return True

        return bool(self._tags & other._tags)


class SlotType(enum.IntEnum):
    Prefix = 100
    Suffix = 200
    Implicit = 300


class Slot:
    def __init__(self, slot_type: SlotType, weight: int) -> None:
        self.type = slot_type
        self.weight = weight


class Property:
    def __init__(self, name: str, value: str, slot_type: SlotType) -> None:
        self.name = name
        self.value = value
        self.slot_type = slot_type

    def __str__(self) -> str:
        return f'{self.name}: {self.value}'


class Group:
    def __init__(self, tags: ItemTags, type_args: List[str], value_args: List[str]) -> None:
        internal_id = uuid.uuid4()
        if not internal_id.is_safe:
            raise Exception('InternalID is unsafe')

        self._internal_id = str(internal_id)
        self._tags = tags
        self._type_args = type_args
        self._value_args = value_args

    @property
    def internal_id(self) -> str:
        return self._internal_id

    def matches(self, other: ItemTags) -> bool:
        return self._tags.matches(other)

    def roll_args(self, slot_type: SlotType) -> Property:
        return Property(
            name=random.choice(self._type_args),
            value=random.choice(self._value_args),
            slot_type=slot_type,
        )
