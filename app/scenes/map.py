from app.data.geography import areas
from app.services.UI import UI


class Map:
    def __init__(self, game):
        self.game = game
        self.back = False

    def render(self):
        UI.clear()
        if self.back:
            self.back = False
            return
        UI.title("MAP")
        UI.line()
        UI.say(
            f"Current location: {self.game.region.name} > {self.game.area.name}")
        UI.say(
            f"Weather: {self.game.weather.getReport()}")
        UI.line()
        choice: int = UI.choice(["Local map", "World map", "Travel"], True)
        UI.clear()
        match choice:
            case 0:
                return
            case 1:
                UI.title(self.game.region.name)
                UI.line()
                UI.say(self.game.region.getMap())
                UI.line()
                UI.wait()
            case 2:
                UI.say("The world map will be available soon!")
                UI.line()
                UI.wait()
            case 3:
                self.renderTravel()
        return self.render()

    def renderTravel(self) -> None:
        if len(self.game.area.connectedAreas) == 0:
            UI.clear()
            UI.say("There are no areas nearby to which you can travel.")
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
        self.game.setGeography()
        self.game.clock.increment(4)
        self.back = True
