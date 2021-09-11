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
            '+2 урона [P1]',
            '+4 урона [P2]',
            '+6 урона [P3]',
            '+1d2 урона [P1]',
            '+1d4 урона [P2]',
            '+1d6 урона [P3]',
        ],
    ),
    Group(
        tags=ItemTags(weapon=True),
        type_args=['Критический'],
        value_args=[
            '+1 к диапазону крита [P1]',
            '+2 к диапазону крита [P2]',
        ],
    ),
    Group(
        tags=ItemTags(weapon=True),
        type_args=['Меткий'],
        value_args=[
            '+1 на попадание [P1]',
            '+2 на попадание [P2]',
            '+3 на попадание [P3]',
        ],
    ),
]
