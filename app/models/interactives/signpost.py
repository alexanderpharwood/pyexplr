from app.models.interactives.base import Base
from app.scenes.interactives.signpost import Signpost as SignpostScene
from app.services.utilities import generateHash


class Signpost(Base):
    scene = SignpostScene
    id = "SIGNPOST"
    BASE_CHANCE = 100

    def toDict(self):
        return {
            "id": self.id,
            "hash": self.hash,
            "area": self.area,
            "name": self.name,
        }

    def setDefaultProperties(self):
        self.hash = generateHash()
        self.name = "Signpost"

    def generateName(self):
        return "Signpost"

    def generateDescription(self):
        return "I wonder what it says..."
