from core.db.implicits import armor
from core.db.implicits import jewellery
from core.db.implicits import weapon


DATA = []
DATA.extend(armor.DATA)
DATA.extend(jewellery.DATA)
DATA.extend(weapon.DATA)
