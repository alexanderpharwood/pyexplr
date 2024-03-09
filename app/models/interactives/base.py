from app.services.utilities import generateHash


class Base:
    scene = None
    id = None
    hash = None
    BASE_CHANCE = 50

    def __init__(self, properties: dict = None):
        self.setDefaultProperties()
        if properties != None:
            self.setProperties(properties)
        self.name = self.generateName()
        self.description = self.generateDescription()

    def toDict(self):
        return {
            "id": self.id,
            "hash": self.hash,
            "area": self.area,
        }

    @classmethod
    def createScene(cls, game, properties: dict | None = None):
        return cls.scene(game, cls(properties))

    @classmethod
    def calculateChance(cls, _):
        return cls.BASE_CHANCE

    def setProperties(self, properties: dict):
        for key, value in properties.items():
            setattr(self, key, value)

    def setDefaultProperties(self):
        self.hash = generateHash()

    def generateDescription(self):
        return ""

    def generateName(self):
        return self.id
