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
            '+2 урона [t1]',
            '+4 урона [t2]',
            '+6 урона [t3]',
            '+1d2 урона [t1]',
            '+1d4 урона [t2]',
            '+1d6 урона [t3]',
        ],
    ),
    Group(
        tags=ItemTags(weapon=True),
        type_args=['Критический'],
        value_args=[
            '+1 к диапазону крита [t1]',
            '+2 к диапазону крита [t2]',
        ],
    ),
    Group(
        tags=ItemTags(weapon=True),
        type_args=['Меткий'],
        value_args=[
            '+1 на попадание [t1]',
            '+2 на попадание [t2]',
            '+3 на попадание [t3]',
        ],
    ),
]
