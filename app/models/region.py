from app.data.geography import maps, regions


class Region:
    def __init__(self, properties):
        self.id: str = properties["id"]
        self.name: str = properties["name"]
        self.description: str = properties["description"]
        self.temperatureModifier: int = properties["temperatureModifier"]
        self.weatherConditions: list[str] = properties["weatherConditions"]
        self.areas: list[str] = properties["areas"]
        map = next(filter(lambda m: m["region"] == self.id, maps), None)
        if (map == None):
            self.map = None
        else:
            self.map = map["map"]

    @staticmethod
    def create(id: str):
        data = next(filter(lambda r: r["id"] == id, regions), None)
        return Region(data)

    def getMap(self) -> None:
        if self.map == None:
            return "No map is available for this region."
        return self.map
