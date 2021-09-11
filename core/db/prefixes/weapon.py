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
            '+2 урона [P3]',
            '+4 урона [P2]',
            '+6 урона [P1]',
            '+1d2 урона [P3]',
            '+1d4 урона [P2]',
            '+1d6 урона [P1]',
        ],
    ),
    Group(
        tags=ItemTags(weapon=True),
        type_args=['Критический'],
        value_args=[
            '+1 к диапазону крита [P2]',
            '+2 к диапазону крита [P1]',
        ],
    ),
    Group(
        tags=ItemTags(weapon=True),
        type_args=['Меткий'],
        value_args=[
            '+1 на попадание [P2]',
            '+2 на попадание [P1]',
        ],
    ),
    Group(
        tags=ItemTags(weapon=True),
        type_args=['Мощный'],
        value_args=[
            '-1 к КД цели при крите (пока не починит) [P2]',
            '-2 к КД цели при крите (пока не починит) [P1]',
        ],
    ),
    Group(
        tags=ItemTags(weapon=True),
        type_args=['Давящий'],
        value_args=[
            '+1 к сложности спасброска, если спасбросок инициирован этим предметом [P2]',
            '+2 к сложности спасброска, если спасбросок инициирован этим предметом [P1]',
        ],
    ),
    Group(
        tags=ItemTags(weapon=True),
        type_args=['Отчаянный'],
        value_args=[
            '+2 на попадание, -2 к КД [P2]',
            '+3 на попадание, -3 к КД [P1]',
        ],
    ),
]
