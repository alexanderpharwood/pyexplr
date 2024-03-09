from app.models.interactives.base import Base
from app.scenes.interactives.loose_ground import LooseGround as LooseGroundScene
from app.services.utilities import generateHash


class LooseGround(Base):
    scene = LooseGroundScene
    id = "LOOSE_GROUND"
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
        self.name = "Loose ground"

    def generateName(self):
        return "Loose ground"

    def generateDescription(self):
        return "The ground seems to have been disturbed. Perhaps something is buried here."
