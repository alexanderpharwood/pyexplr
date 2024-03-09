from app.services.UI import UI
from app.models.Save import Save
from app.scenes.Game import Game
from app.data.geography import regions


class CharacterCreation:
    def __init__(self):
        self.name = None
        self.region = None

    def render(self):
        self.renderName()
        self.renderLocation()
        save: Save = Save()
        save.player["name"] = self.name
        save.player["region"] = self.region
        save.player["area"] = self.area
        save.writeToDisk()
        game = Game(save)
        return game.render()

    def renderName(self):
        UI.clear()
        UI.say("Character name (max 10):")
        UI.line()
        name: str = UI.read()
        if (len(name) > 10):
            self.error = "That's rather a long name. Try something shorter."
            return self.renderName()

        self.name = name

    def renderLocation(self):
        UI.clear()
        UI.say("Choose a starting region:")
        UI.line()
        choices = list(map(lambda r: r["name"], regions))
        choice = UI.choice(choices)
        region = regions[choice - 1]
        UI.clear()
        UI.say(region["name"])
        UI.line()
        UI.say(region["description"])
        UI.line()
        confirm = UI.boolChoice(["Sounds good!", "On second thought..."])
        if (confirm == True):
            self.region = region["id"]
            self.area = region["startingArea"]
        else:
            return self.renderLocation()
