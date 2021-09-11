import random

from typing import List

from core import types
from core.db import prefixes as db_prefixes
from core.db import slots as db_slots
from core.db import suffixes as db_suffixes


class LogicError(Exception):
    pass


def roll_prefix(tags: types.ItemTags) -> types.Property:
    groups = _matched_groups(db_prefixes.DATA, tags)
    if not groups:
        raise LogicError('Подходящих префиксов не найдено')

    return random.choice(groups).roll_args(types.SlotType.Prefix)


def roll_suffix(tags: types.ItemTags) -> types.Property:
    groups = _matched_groups(db_suffixes.DATA, tags)
    if not groups:
        raise LogicError('Подходящих суффиксов не найдено')

    return random.choice(groups).roll_args(types.SlotType.Suffix)


def roll_slot(tags: types.ItemTags) -> types.Property:
    slot_type = _choice_slot(db_slots.DATA)

    if slot_type == types.SlotType.Prefix:
        return roll_prefix(tags)

    if slot_type == types.SlotType.Suffix:
        return roll_suffix(tags)

    raise Exception('Unknown Slot Type')


def _matched_groups(groups: List[types.Group], tags: types.ItemTags) -> List[types.Group]:
    return [g for g in groups if g.matches(tags)]


def _choice_slot(slots: List[types.Slot]) -> types.SlotType:
    total_weight = sum(s.weight for s in slots)

    chosen_value = random.randint(1, total_weight)
    current_value = 0
    for slot in slots:
        current_value += slot.weight
        if chosen_value <= current_value:
            return slot.type

    raise Exception('Choice Slot Error')
