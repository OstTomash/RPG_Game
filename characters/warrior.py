import random

from .character import Character


class Warrior(Character):
    _character_class = "warrior"
    __base_damage = 120
    __base_defence = 200
    __base_health = 1200
    __fatality_probability = 1 if random.random() <= 0.1 else 0  # 10% probability
    __fatality_damage = 400

    def __init__(self) -> None:
        super().__init__()
        self._health = Warrior.__base_health
        self._damage = Warrior.__base_damage
        self._defence = Warrior.__base_defence
        self._fatal_prop = Warrior.__fatality_probability
        self._fatal_damage = Warrior.__fatality_damage

    def __str__(self) -> str:
        return (f"Warrior \nName: {self._name} \nLevel: {self._level} \nHealth: {self._health}"
                f"\nDefence: {self._defence} \nDamage: {self._damage} \nFatality: {self.__fatality_damage}"
                f"\nExperience: {self._experience}")
