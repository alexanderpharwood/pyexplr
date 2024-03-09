from app.services.UI import UI
from app.data.geography import areas
from app.scenes.interactives.base import Base


class Signpost(Base):
    def render(self):
        if self.back == True:
            return
        UI.clear()
        self.game.renderStatusBar()
        UI.line()
        UI.say(self.model.name)
        UI.say(self.model.description)
        UI.line()
        choice = UI.choice(["Read"], True)
        if choice == 0:
            return
        if choice == 1:
            self.read()
        self.render()

    def read(self):
        if len(self.game.area.connectedAreas) == 0:
            UI.clear()
            UI.say("That's odd: it's blank.")
            UI.line()
            UI.wait()
            return

        connectedAreas: list = []
        for areaId in self.game.area.connectedAreas:
            area = next(filter(lambda a: a["id"] == areaId, areas), None)
            connectedAreas.append(area)

        UI.clear()
        UI.say("Where do you want to go?")
        UI.line()
        choices = list(map(lambda a: a["name"], connectedAreas))
        choice: int = UI.choice(choices, True)
        if (choice == 0):
            return

        chosenArea = connectedAreas[choice - 1]
        UI.clear()
        UI.loading(5, f"Travelling to {chosenArea['name']}...")
        UI.clear()
        UI.say(f"Arrived at {chosenArea['name']}")
        UI.line()
        UI.wait()

        self.game.player.area = chosenArea["id"]
        self.game.clock.increment(4)
        self.back = True
        self.game.areaScene.back = True
        self.game.setArea()
