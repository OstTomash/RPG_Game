from .item import Item


class LWeapon(Item):
    _item_type = "l_weapon"

    def __init__(self, name="Simple left hand sword", boost_damage=1.2, boost_health=1.0, boost_shield=0.9) -> None:
        super().__init__(name, boost_damage, boost_health, boost_shield)


class RWeapon(Item):
    _item_type = "r_weapon"

    def __init__(self, name="Simple right hand axe", boost_damage=1.25, boost_health=1.0, boost_shield=0.85) -> None:
        super().__init__(name, boost_damage, boost_health, boost_shield)
