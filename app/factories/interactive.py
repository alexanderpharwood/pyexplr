from random import randint
from app.models.interactives.tree import Tree
from app.models.interactives.herb import Herb
from app.models.interactives.grass import Grass
from app.models.interactives.loose_ground import LooseGround
from app.models.interactives.signpost import Signpost
from app.models.interactives.fishing_spot import FishingSpot


class InteractiveFactory:
    models: list[dict] = [
        {
            "id": "TREE",
            "model": Tree,
        },
        {
            "id": "HERB",
            "model": Herb,
        },
        {
            "id": "GRASS",
            "model": Grass,
        },
        {
            "id": "LOOSE_GROUND",
            "model": LooseGround,
        },
        {
            "id": "SIGNPOST",
            "model": Signpost,
        },
        {
            "id": "FISHING_SPOT",
            "model": FishingSpot,
        }

    ]

    @staticmethod
    def random():
        models = InteractiveFactory.models
        selection = models[randint(0, len(models) - 1)]
        return InteractiveFactory.create(selection["id"])

    @staticmethod
    def create(model: str):
        index = next(i for i, v in enumerate(
            InteractiveFactory.models) if v["id"] == model)
        return InteractiveFactory.models[index]["model"]()

    @staticmethod
    def getForArea(game):
        data = game.save.getInteractivesForArea(game.area.id)
        instances = []
        for item in data:
            interactive = next(
                filter(lambda i: i["id"] == item["id"], InteractiveFactory.models), None)
            if interactive == None:
                continue
            instances.append(interactive["model"].createScene(game, item))
        return instances

    @staticmethod
    def generate(game):
        chances: list[dict] = []
        for item in InteractiveFactory.models:
            model = item["model"]
            chance: int = model.calculateChance(game)
            if (chance == 0):
                continue
            chances.append(
                {"chance": chance, "id": item["id"], "model": item["model"]})

        return list(map(lambda i: i["model"].createScene(game, {"area": game.area.id}), chances))
