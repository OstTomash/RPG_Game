class Inventory:
    def __init__(self) -> None:
        self.__items = list()

    def add_item(self, *args) -> None:
        for item in args:
            self.__items.append(item)

    def remove_item(self, item) -> None:
        self.__items.remove(item)

    @property
    def inventory(self) -> list:
        return self.__items
