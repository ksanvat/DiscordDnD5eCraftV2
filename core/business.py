import random

from typing import List

from core import types
from core.db import prefixes


def roll_prefix(tags: types.ItemTags) -> types.Property:
    group = random.choice(_matched_groups(prefixes.DATA, tags))
    return group.roll_args()


def _matched_groups(groups: List[types.Group], tags: types.ItemTags) -> List[types.Group]:
    return [g for g in groups if g.matches(tags)]
