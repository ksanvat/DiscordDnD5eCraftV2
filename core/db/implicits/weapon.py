from core.types import Group
from core.types import ItemTags


DATA = [
    Group(
        tags=ItemTags(weapon=True),
        type_args=['Быстрые атаки'],
        value_args=[
            (
                'позволяет в свой ход совершить дополнительную атаку ближнего боя, '
                'если вы совершили атаку действием в ближнем бою'
            ),
        ],
    ),
    Group(
        tags=ItemTags(weapon=True),
        type_args=['Рисковый'],
        value_args=[
            (
                '+5 к диапазону критов, все атаки по вам считаются критическими, '
                'этот эффект нельзя убрать ничем, пока вы используете оружие'
            ),
        ],
    ),
    Group(
        tags=ItemTags(weapon=True),
        type_args=['Вампиризм'],
        value_args=[
            'если ты попадаешь по существу атакой оружием в радиусе 10фт, то восстанавливаешь 2 хит поинта',
        ],
    ),
    Group(
        tags=ItemTags(weapon=True),
        type_args=['Сокрушающий Удар'],
        value_args=[
            (
                'когда ты попадаешь этим оружием по врагу, он должен пройти спасбросок Силы '
                'сл 8 + бонус мастерства + мод силы или упадет ничком'
            ),
        ],
    ),
    Group(
        tags=ItemTags(weapon=True),
        type_args=['Всплеск Магии'],
        value_args=[
            'раз в день вы можете одним действием наложить два заклинания',
        ],
    ),
]
