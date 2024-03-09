from app.models.rucksack import Rucksack


class Player:
    def __init__(self, properties):
        self.name: str = properties["name"]
        self.totalHealth: int = properties["totalHealth"]
        self.health: int = properties["health"]
        self.totalEnergy: int = properties["totalEnergy"]
        self.energy: int = properties["energy"]
        self.equipped: list[dict] = properties["equipped"]
        self.rucksack: dict = Rucksack(properties["rucksack"])
        self.region: str = properties["region"]
        self.area: str = properties["area"]

    def toDict(self) -> dict:
        return {
            "name": self.name,
            "totalHealth": self.totalHealth,
            "health": self.health,
            "totalEnergy": self.totalEnergy,
            "energy": self.energy,
            "equipped": self.equipped,
            "rucksack": self.rucksack.toDict(),
            "region": self.region,
            "area": self.area,
        }
