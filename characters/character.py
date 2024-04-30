from equipment import Arsenal, Inventory, Item


class Character:
    _character_class: None | str = None

    def __init__(self):
        self._inventory: Inventory = Inventory()
        self._arsenal: Arsenal = Arsenal()
        self._name: None | str = None
        self._health: None | int = None
        self._damage: None | int = None
        self._defence: None | int = None
        self._fatal_prop: None | float = None
        self._fatal_damage: None | int = None
        self._experience: int = 0
        self._level: int = 1

    def level_up(self) -> None:

        if self._experience >= 100:
            self._experience -= 100
            self._level += 1

    def experience_add(self, opponent_level: int | str) -> None:
        if opponent_level == "bot":
            self._experience += 4
            return
        self._experience += 20
        if opponent_level > self._level:
            level_diff = opponent_level - self._level
            self._experience += (level_diff / 10 * self._experience)

    def experience_drop(self) -> None:
        self._experience = 0

    @property
    def name(self) -> str | None:
        return self._name

    @property
    def inventory(self) -> Inventory:
        return self._inventory

    @name.setter
    def name(self, name) -> None:
        self._name = name

    @property
    def fatal_prop(self) -> float | None:
        return self._fatal_prop

    @property
    def fatal_damage(self) -> int | None:
        return self._fatal_damage

    @property
    def level(self) -> int:
        return self._level

    @property
    def defence(self) -> int | None:
        return self._defence

    @property
    def char_class(self) -> str | None:
        return self._character_class

    @property
    def health(self) -> int | None:
        return self._health

    @property
    def damage(self) -> int | None:
        return self._damage

    @damage.setter
    def damage(self, value) -> None:
        self._damage = value

    @defence.setter
    def defence(self, value) -> None:
        self._defence = value

    @health.setter
    def health(self, value) -> None:
        self._health = value

    def defence_off(self) -> None:
        self._defence = 0

    def type_boost_damage(self) -> None:
        self._damage *= 1.15

    def reduce_defence(self, value: int) -> None:
        self._defence -= value

    def reduce_health(self, value: int) -> None:
        self._health -= value

    @property
    def strike(self) -> int | None:
        return self._damage

    def level_dependent_boost(self) -> None:
        self._health += (self._level/100 * self._health)
        self._defence += (self._level/100 * self._defence)
        self._damage += (self._level/100 * self._damage)

    def __count_attack_put_on(self, item: Item) -> None:
        self._health *= item.boost_health
        self._defence *= item.boost_defence
        self._damage *= item.boost_damage

    def __count_attack_take_off(self, item: Item) -> None:
        self._health /= item.boost_health
        self._defence /= item.boost_defence
        self._damage /= item.boost_damage

    def check_items(self, container, action_name, action_fn):
        while True:
            items = [item for item in container if item]
            result = "\n".join([f"{i + 1}. {item}" for i, item in enumerate(items)])
            print(f"{self._name}, check out your {action_name}:\n", result)
            index = input(f"\nIf you want to {action_name.lower()} something - choose index. If no, type 'n': ")
            if index.isdigit():
                try:
                    action_fn(items[int(index) - 1])
                except IndexError:
                    print("Incorrect index.")
                    continue
            else:
                return

    def check_inventory(self) -> None:
        self.check_items(
            self._inventory.inventory,
            "Inventory",
            lambda item: self._arsenal.set_item(item) and self.__count_attack_put_on(item)
        )

    def check_armory(self) -> None:
        self.check_items(
            self._arsenal.list_items.values(),
            "Arsenal",
            lambda item: self._arsenal.take_off_item(item) and self.__count_attack_take_off(item)
        )
