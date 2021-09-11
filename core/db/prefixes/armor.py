from core.types import Group
from core.types import ItemTags


DATA = [
    Group(
        tags=ItemTags(armor=True),
        type_args=[
            'Шипованный',
            'Режущий',
        ],
        value_args=[
            'атакующий вас в ближнем бою персонаж получает 3 ед урона [P1]',
            'атакующий вас в ближнем бою персонаж получает 6 ед урона [P2]',
            'атакующий вас в ближнем бою персонаж получает 10 ед урона [P3]',
        ],
    ),
    Group(
        tags=ItemTags(armor=True),
        type_args=['Маневренный'],
        value_args=['+1 на попадание [P1]'],
    ),
    Group(
        tags=ItemTags(armor=True),
        type_args=['Тяжелый'],
        value_args=[
            '+1 к проверкам атлетики',
            '+2 к проверкам атлетики',
            '+3 к проверкам атлетики',
        ],
    ),
]
