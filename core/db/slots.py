from core.types import Slot
from core.types import SlotType


DATA = [
    Slot(slot_type=SlotType.Prefix, weight=45),
    Slot(slot_type=SlotType.Suffix, weight=45),
    Slot(slot_type=SlotType.Implicit, weight=10),
]
