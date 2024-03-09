class Rucksack:
    def __init__(self, properties):
        self.gold: str = properties["gold"]
        self.items: int = properties["items"]

    def toDict(self) -> dict:
        return {
            "gold": self.gold,
            "items": self.items,
        }

    def addItem(self, itemId: str):
        self.items.append(itemId)
        # Check if the item is stackable
        # if so, check if we already have one.
        # If so, update the quantity
        # Need to accept properties with the item

    def replaceItem(self):
        pass
