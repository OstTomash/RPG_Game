import random

from .character import Character


class Mage(Character):
    _character_class = "mage"
    __base_damage = 130
    __base_defence = 150
    __base_health = 800
    __fatality_probability = 1 if random.random() <= 0.15 else 0  # 15% probability
    __fatality_damage = 250

    def __init__(self) -> None:
        super().__init__()
        self._health = Mage.__base_health
        self._damage = Mage.__base_damage
        self._defence = Mage.__base_defence
        self._fatal_prop = Mage.__fatality_probability
        self._fatal_damage = Mage.__fatality_damage

    def __str__(self) -> str:
        return (f"Mage \nName: {self._name} \nLevel: {self._level} \nHealth: {self._health}"
                f"\nDefence: {self._defence} \nDamage: {self._damage} \nFatality: {self.__fatality_damage}"
                f"\nExperience: {self._experience}")
