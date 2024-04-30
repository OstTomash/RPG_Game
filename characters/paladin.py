import random

from .character import Character


class Paladin(Character):
    _character_class = "paladin"
    __base_damage = 115
    __base_defence = 180
    __base_health = 1100
    __fatality_probability = 1 if random.random() <= 0.12 else 0  # 12% probability
    __fatality_damage = 350

    def __init__(self) -> None:
        super().__init__()
        self._health = Paladin.__base_health
        self._damage = Paladin.__base_damage
        self._shield = Paladin.__base_defence
        self._fatal_prop = Paladin.__fatality_probability
        self._fatal_damage = Paladin.__fatality_damage

    def __str__(self) -> str:
        return (f"Paladin \nName: {self._name} \nLevel: {self._level} \nHealth: {self._health}"
                f"\nDefence: {self._defence} \nDamage: {self._damage} \nFatality: {self.__fatality_damage}"
                f"\nExperience: {self._experience}")