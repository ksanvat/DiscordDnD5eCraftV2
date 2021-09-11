from core.types import Group
from core.types import ItemTags


DATA = [
    Group(
        tags=ItemTags(weapon=True),
        type_args=['Быстрые атаки'],
        value_args=[
            'позволяет в свой ход совершить дополнительную атаку, если вы совершили атаку действием в ближнем бою',
        ],
    ),
    Group(
        tags=ItemTags(armor=True),
        type_args=['Непоколебимость'],
        value_args=[
            (
                'позволяет встать в уклонение за бонусное действие, '
                'если в этом раунде вы не перемещались и совершили не больше одной атаки'
            ),
        ],
    ),
]
