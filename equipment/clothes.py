from .item import Item


class Shield(Item):
    _item_type = "shield"

    def __init__(self, name="Metal shield", boost_damage=1.05, boost_health=1.0, boost_shield=1.3) -> None:
        super().__init__(name, boost_damage, boost_health, boost_shield)


class Shoes(Item):
    _item_type = "shoes"

    def __init__(self, name="Leather shoes", boost_damage=1.05, boost_health=1.1, boost_shield=1.05) -> None:
        super().__init__(name, boost_damage, boost_health, boost_shield)


class Ring(Item):
    _item_type = "ring"

    def __init__(self, name="Ring of Sun", boost_damage=1.1, boost_health=1.2, boost_shield=0.9) -> None:
        super().__init__(name, boost_damage, boost_health, boost_shield)


class Helmet(Item):
    _item_type = "helmet"

    def __init__(self, name="Usual helmet", boost_damage=1.0, boost_health=1.0, boost_shield=1.2) -> None:
        super().__init__(name, boost_damage, boost_health, boost_shield)
