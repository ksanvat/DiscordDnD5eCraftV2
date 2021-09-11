from core.types import Group
from core.types import ItemTags


DATA = [
    Group(
        tags=ItemTags(weapon=True),
        type_args=[
            'Колющий',
            'Режущий',
            'Дробящий',
            'Огненный',
            'Ледяной',
            'Электрический',
            'Звуковой',
            'Кислотный',
            'Ядовитый',
            'Силовой',
            'Излучающий',
            'Некротический',
            'Психический',
        ],
        value_args=[
            '2 [dmg prefix t1]',
            '4 [dmg prefix t2]',
            '6 [dmg prefix t3]',
            '1d2 [dmg prefix t1]',
            '1d4 [dmg prefix t2]',
            '1d6 [dmg prefix t3]',
        ],
    ),
]
