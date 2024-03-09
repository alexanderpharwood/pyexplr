from random import randint
from app.models.interactives.base import Base
from app.scenes.interactives.tree import Tree as TreeScene
from app.services.utilities import generateHash


class Tree(Base):
    scene = TreeScene
    id = "TREE"
    BASE_CHANCE = 50

    def toDict(self):
        return {
            "id": self.id,
            "hash": self.hash,
            "area": self.area,
            "species": self.species,
            "name": self.name,
            "size": self.size
        }

    @staticmethod
    def calculateChance(game):
        chance = Tree.BASE_CHANCE
        if game.area.isUnderground:
            return 0
        if game.area.isUrban:
            return 0

        if game.area.altitude > 600:
            chance -= 40

        return chance

    def setDefaultProperties(self):
        self.hash = generateHash()
        self.species = "OAK"
        self.name = "Tree"
        self.size = randint(1, 10)

    def generateName(self):
        return "Oak tree"

    def generateDescription(self):
        if self.size < 5:
            return "It's a fairly young tree."
        return "It's a grand old tree. It ought to provide a lot of lumber!"
