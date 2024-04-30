class Item:
    _item_type = None

    def __init__(self, name=None, boost_damage=None, boost_health=None, boost_defence=None) -> None:
        self._boost_damage = boost_damage
        self._boost_health = boost_health
        self._boost_defence = boost_defence
        self._name = name
        self._is_on = False

    def __str__(self) -> str:
        return (f"Type: {self._item_type} \nName: {self._name} \nBoost damage: {self._boost_damage},"
                f"boost health: {self._boost_health}, boost defence: {self._boost_defence}.")

    @property
    def boost_damage(self) -> None | float:
        return self._boost_damage

    @property
    def boost_defence(self) -> None | float:
        return self._boost_defence

    @property
    def boost_health(self) -> None | float:
        return self._boost_health

    @property
    def item_name(self) -> None | str:
        return self._name

    @classmethod
    def get_item_type(cls) -> None | str:
        return cls._item_type

    @property
    def is_on(self) -> bool:
        return self._is_on

    def is_off(self) -> None:
        self._is_on = False
