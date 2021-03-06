from core.types import Group
from core.types import ItemTags


DATA = [
    Group(
        tags=ItemTags(jewellery=True),
        type_args=['Фокусировка'],
        value_args=[
            '+1 к попаданию заклинаниями [P2]',
            '+2 к попаданию заклинаниями [P1]',
        ],
    ),
    Group(
        tags=ItemTags(jewellery=True),
        type_args=['Концентрация'],
        value_args=['+1 к сложности спасброска [P1]'],
    ),
    Group(
        tags=ItemTags(jewellery=True),
        type_args=['Воровской'],
        value_args=[
            '+1 к ловкости рук [P2]',
            '+1 к ловкости рук и +1 к ловкости [P1]',
        ],
    ),
    Group(
        tags=ItemTags(jewellery=True),
        type_args=['Умелый'],
        value_args=[
            '+1 к Силе [P2]',
            '+2 к Силе [P1]',
            '+1 к Интеллекту [P2]',
            '+2 к Интеллекту [P1]',
            '+1 к Мудрости [P2]',
            '+2 к Мудрости [P1]',
            '+1 к Харизме [P2]',
            '+2 к Харизме [P1]',
        ],
    ),
]
