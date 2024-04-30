from .item import Item


class Arsenal:
    def __init__(self) -> None:
        self._items_on = {
            "helmet": None,
            "l_weapon": None,
            "r_weapon": None,
            "shield": None,
            "shoes": None,
            "ring": None
        }

    @property
    def list_items(self) -> dict[str, None | Item]:
        return self._items_on

    def set_item(self, item: Item) -> None | str:

        if item.get_item_type() == "shield" and self._items_on["l_weapon"]:
            print("You can't hold shield. Take off left hand weapon first.")
            return "You can't hold shield. Take off left hand weapon first."

        elif item.get_item_type() == "l_weapon" and self._items_on["shield"]:
            print("You can't hold left hand weapon. Take off shield first.")
            return "You can't hold left hand weapon. Take off shield first."

        if not self._items_on.get(item.get_item_type()):
            item._is_on = True
            self._items_on[item.get_item_type()] = item

    def take_off_item(self, item: Item) -> None:
        self._items_on[item.get_item_type()].is_off()
        self._items_on[item.get_item_type()] = None
