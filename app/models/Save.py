from datetime import datetime
import json
import config
from app.services.File import File


class Save:
    CURRENT_VERSION: int = 0
    WRITEABLE: list[str] = [
        "meta",
        "player",
        "clock",
        "weatherConditions",
        "locationItems",
        "npcs",
        "storageLocations",
        "extantItems",
    ]

    def __init__(self):
        self.setDefaultProperties()

    def setDefaultProperties(self):
        self.meta = {
            "version": self.CURRENT_VERSION,
            "createdAt": datetime.now().strftime("%Y-%m-%d %H:%M:%S"),
        },
        self.player = {
            "name": None,
            "totalHealth": 100,
            "health": 100,
            "totalEnergy": 100,
            "energy": 100,
            "equipped": [],
            "rucksack": {
                "gold": 0,
                "items": [],
            },
            "region": "GREAT_PLAINS",
            "area": "LOWLANDS"
        }
        self.clock = {
            "minute": 0,
            "minuteHash": "000000000000000000000000",
            "hour": 12,
            "hourHash": "000000000000000000000000",
            "day": 1,
            "dayHash": "000000000000000000000000",
            "season": 0,
            "seasonHash": "000000000000000000000000",
            "year": 1,
            "yearHash": "000000000000000000000000",
        }
        self.weatherConditions = []
        self.interactives = []
        self.locationItems = []
        self.npcs = []
        self.storageLocations = []
        self.extantItems = []

    def writeToDisk(self) -> None:
        asJSON: str = self.toJSON()
        File.write(
            f"{config.SAVE_LOCATION}/{self.player['name']}.{config.SAVE_EXTENSION}", asJSON)

    @staticmethod
    def readFromDisk(fileName: str) -> None:
        data: str = File.read(f"{config.SAVE_LOCATION}/{fileName}")
        dataAsDict = json.loads(data)
        instance: Save = Save()
        instance.fromDict(dataAsDict)
        return instance

    def fromDict(self, asDict: dict) -> None:
        self.meta = asDict["meta"]
        self.player = asDict["player"]
        self.clock = asDict["clock"]
        self.weatherConditions = asDict["weatherConditions"]
        self.interactives = asDict["interactives"]
        self.locationItems = asDict["locationItems"]
        self.npcs = asDict["npcs"]
        self.storageLocations = asDict["storageLocations"]
        self.extantItems = asDict["extantItems"]

    def toDict(self) -> dict:
        return {
            "meta": self.meta,
            "player": self.player,
            "clock": self.clock,
            "weatherConditions": self.weatherConditions,
            "interactives": self.interactives,
            "locationItems": self.locationItems,
            "npcs": self.npcs,
            "storageLocations": self.storageLocations,
            "extantItems": self.extantItems,
        }

    def toJSON(self) -> str:
        asDict: dict = self.toDict()
        return json.dumps(asDict)

    def getWeatherConditionsForArea(self, area: str) -> dict | None:
        return next(filter(lambda a: a["area"] == area, self.weatherConditions), None)

    def setWeatherConditions(self, properties: dict):
        exists = next(
            filter(lambda a: a["area"] == properties["area"], self.weatherConditions), None)
        if (exists == None):
            self.weatherConditions.append(properties)
        else:
            exists["day"] = properties["day"]
            exists["conditions"] = properties["conditions"]

    def getInteractivesForArea(self, area: str) -> list[dict] | None:
        return list(filter(lambda a: a["area"] == area, self.interactives))

    def addInteractive(self, properties: dict):
        self.interactives.append(properties)
