import random

from typing import List
from typing import Set

from core import types
from core.db import implicits as db_implicits
from core.db import prefixes as db_prefixes
from core.db import slots as db_slots
from core.db import suffixes as db_suffixes


class LogicError(Exception):
    pass


class Context:
    def __init__(self) -> None:
        self.implicit_used: Set[str] = set()


def roll_prefix(ctx: Context, tags: types.ItemTags) -> types.Property:
    groups = _matched_groups(db_prefixes.DATA, tags, set())
    if not groups:
        raise LogicError('Подходящих префиксов не найдено')

    return random.choice(groups).roll_args(types.SlotType.Prefix)


def roll_suffix(ctx: Context, tags: types.ItemTags) -> types.Property:
    groups = _matched_groups(db_suffixes.DATA, tags, set())
    if not groups:
        raise LogicError('Подходящих суффиксов не найдено')

    return random.choice(groups).roll_args(types.SlotType.Suffix)


def roll_implicit(ctx: Context, tags: types.ItemTags) -> types.Property:
    groups = _matched_groups(db_implicits.DATA, tags, ctx.implicit_used)
    if not groups:
        raise LogicError('Подходящих собственных свойств не найдено')

    chosen_group = random.choice(groups)
    ctx.implicit_used.add(chosen_group.internal_id)

    return chosen_group.roll_args(types.SlotType.Implicit)


def roll_slot(ctx: Context, tags: types.ItemTags) -> types.Property:
    slot_type = _choice_slot(db_slots.DATA)

    if slot_type == types.SlotType.Prefix:
        return roll_prefix(ctx, tags)

    if slot_type == types.SlotType.Suffix:
        return roll_suffix(ctx, tags)

    if slot_type == types.SlotType.Implicit:
        return roll_implicit(ctx, tags)

    raise Exception('Unknown Slot Type')


def _matched_groups(groups: List[types.Group], tags: types.ItemTags, skip_id: Set[str]) -> List[types.Group]:
    return [g for g in groups if g.matches(tags) and g.internal_id not in skip_id]


def _choice_slot(slots: List[types.Slot]) -> types.SlotType:
    total_weight = sum(s.weight for s in slots)

    chosen_value = random.randint(1, total_weight)
    current_value = 0
    for slot in slots:
        current_value += slot.weight
        if chosen_value <= current_value:
            return slot.type

    raise Exception('Choice Slot Error')
