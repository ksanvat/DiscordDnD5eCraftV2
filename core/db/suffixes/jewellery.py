from core.types import Group
from core.types import ItemTags


DATA = [
    Group(
        tags=ItemTags(jewellery=True),
        type_args=[
            'Несломимой Силы',
            'Несломимой Ловкости',
            'Несломимого Тела',
            'Несломимого Интеллекта',
            'Несломимой Мудрости',
            'Несломимой Харизмы',
        ],
        value_args=[
            '+2 к спасброску [S2]',
            '+3 к спасброску [S1]',
        ],
    ),
    Group(
        tags=ItemTags(jewellery=True),
        type_args=['Несломимости'],
        value_args=['+1 ко всем спасброскам [S1]'],
    ),
    Group(
        tags=ItemTags(jewellery=True),
        type_args=['Жизни'],
        value_args=[
            '+5 к максимальному запасу ХП [S3]',
            '+10 к максимальному запасу ХП [S2]',
            '+15 к максимальному запасу ХП [S1]',
        ],
    ),
    Group(
        tags=ItemTags(jewellery=True),
        type_args=['Сопротивления'],
        value_args=[
            'колющему',
            'режущему',
            'дробящему',
            'огню',
            'холоду',
            'электричеству',
            'звуку',
            'кислоте',
            'яду',
            'силе',
            'излучению',
            'некротике',
            'психическому',
        ],
    ),
    Group(
        tags=ItemTags(jewellery=True),
        type_args=['Гибкости'],
        value_args=[
            '+1 к ловкости [S2]',
            '+2 к ловкости [S1]',
        ],
    ),
]
