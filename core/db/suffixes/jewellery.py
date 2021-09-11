from core.types import Group
from core.types import ItemTags


DATA = [
    Group(
        tags=ItemTags(jewellery=True),
        type_args=['Несломимости'],
        value_args=[
            '+2 к спасброску Силы [S2]',
            '+3 к спасброску Силы [S1]',
            '+2 к спасброску Ловкости [S2]',
            '+3 к спасброску Ловкости [S1]',
            '+2 к спасброску Телосложения [S2]',
            '+3 к спасброску Телосложения [S1]',
            '+2 к спасброску Интеллекта [S2]',
            '+3 к спасброску Интеллекта [S1]',
            '+2 к спасброску Мудрости [S2]',
            '+3 к спасброску Мудрости [S1]',
            '+2 к спасброску Харизмы [S2]',
            '+3 к спасброску Харизмы [S1]',
        ],
    ),
    Group(
        tags=ItemTags(jewellery=True),
        type_args=['Абсолютной Несломимости'],
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
