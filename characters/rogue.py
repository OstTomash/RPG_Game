import random

from .character import Character


class Rogue(Character):
    _character_class = "rogue"
    __base_damage = 110
    __base_defence = 100
    __base_health = 1000
    __fatality_probability = 1 if random.random() <= 0.2 else 0  # 20% probability
    __fatality_damage = 200

    def __init__(self) -> None:
        super().__init__()
        self._health = Rogue.__base_health
        self._damage = Rogue.__base_damage
        self._defence = Rogue.__base_defence
        self._fatal_prop = Rogue.__fatality_probability
        self._fatal_damage = Rogue.__fatality_damage

    def __str__(self) -> str:
        return (f"Rogue \nName: {self._name} \nLevel: {self._level} \nHealth: {self._health}"
                f"\nDefence: {self._defence} \nDamage: {self._damage} \nFatality: {self.__fatality_damage}"
                f"\nExperience: {self._experience}")
