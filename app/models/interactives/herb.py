from app.models.interactives.base import Base
from app.scenes.interactives.herb import Herb as HerbScene
from app.services.utilities import generateHash


class Herb(Base):
    scene = HerbScene
    id = "HERB"
    BASE_CHANCE = 80

    def toDict(self):
        return {
            "id": self.id,
            "hash": self.hash,
            "area": self.area,
            "species": self.species,
            "name": self.name,
        }

    @staticmethod
    def calculateChance(game):
        chance = Herb.BASE_CHANCE
        if game.area.isUnderground:
            return 0
        if game.area.isUrban:
            return 0

        if game.area.altitude > 600:
            chance -= 40

        return chance

    def setDefaultProperties(self):
        self.hash = generateHash()
        self.species = "LAVENDAR"
        self.name = "Herb"

    def generateName(self):
        return "Lavendar plant"

    def generateDescription(self):
        return "It has a lovely smell and colour. Somebody ought to be able to use it for something!"
