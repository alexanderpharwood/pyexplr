from app.models.interactives.base import Base
from app.scenes.interactives.grass import Grass as GrassScene
from app.services.utilities import generateHash


class Grass(Base):
    scene = GrassScene
    id = "GRASS"
    BASE_CHANCE = 80

    def toDict(self):
        return {
            "id": self.id,
            "hash": self.hash,
            "area": self.area,
            "name": self.name,
        }

    @staticmethod
    def calculateChance(game):
        chance = Grass.BASE_CHANCE
        if game.area.isUnderground:
            return 0
        if game.area.isUrban:
            return 0

        if game.area.altitude > 800:
            chance -= 40

        return chance

    def setDefaultProperties(self):
        self.hash = generateHash()
        self.name = "Grass"

    def generateName(self):
        return "Grass"

    def generateDescription(self):
        return "A patch of long and luscious grass useful for feeding animals."
