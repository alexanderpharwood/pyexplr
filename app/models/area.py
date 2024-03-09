from app.data.geography import areas


class Area:
    def __init__(self, properties):
        self.id: str = properties["id"]
        self.name: str = properties["name"]
        self.temperatureModifier: str = properties["temperatureModifier"]
        self.size: str = properties["size"]
        self.description: str = properties["description"]
        self.region: str = properties["description"]
        self.connectedAreas: str = properties["connectedAreas"]
        self.altitude: int = properties["altitude"]
        self.hasCoastline: bool = properties["hasCoastline"]
        self.hasRiver: bool = properties["hasRiver"]
        self.hasLake: bool = properties["hasLake"]
        self.isUrban: bool = properties["isUrban"]
        self.isUnderground: bool = properties["isUnderground"]

    @staticmethod
    def create(id: str):
        data = next(filter(lambda a: a["id"] == id, areas), None)
        return Area(data)

    def getCurrentSituation(self):
        # Seed some situation generator which takes into account events happening and things like that.
        # For now, we will just return the description
        return self.description
