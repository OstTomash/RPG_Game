import random

from equipment import Item, Helmet, LWeapon, RWeapon, Shoes, Shield, Ring


class Bot:
    _type: str = "bot"
    __drop_item_probability: float = 1 if random.random() <= 0.05 else 0

    def __init__(self) -> None:
        self._inventory: list[Item] = [Helmet(), LWeapon(), RWeapon(), Shield(), Shoes(), Ring()]
        self._health: int = 300
        self._damage: int = 15
        self._level: str = "bot"

    def boost_bot(self, opponent_level: int) -> None:
        self._health += (opponent_level / 10 * self._health)
        self._damage += (opponent_level / 10 * self._damage)

    def drop_item(self) -> Item:
        if self.__drop_item_probability:
            item = random.choice(self._inventory)
            print(f"You picked up a new item: \n{item}.")
            return item

    def reduce_health(self, value: int) -> None:
        self._health -= value

    @property
    def attack(self) -> int:
        return self._damage

    @property
    def health(self) -> int:
        return self._health

    @property
    def level(self) -> str:
        return self._level

    @staticmethod
    def generate_bot():
        while True:
            yield Bot()
