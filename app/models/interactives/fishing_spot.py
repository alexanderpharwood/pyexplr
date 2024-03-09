from app.models.interactives.base import Base
from app.scenes.interactives.fishing_spot import FishingSpot as FishingSpotScene
from app.services.utilities import generateHash


class FishingSpot(Base):
    scene = FishingSpotScene
    id = "FISHING_SPOT"
    BASE_CHANCE = 80

    def toDict(self):
        return {
            "id": self.id,
            "hash": self.hash,
            "area": self.area,
            "name": self.name,
        }

    def setDefaultProperties(self):
        self.hash = generateHash()
        self.name = "Fishing spot"

    def generateName(self):
        return "Fishing spot"

    def generateDescription(self):
        return "Perhaps something will bite."
