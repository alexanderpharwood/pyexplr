from app.services.UI import UI
from app.scenes.interactives.base import Base


class Herb(Base):
    def render(self):
        UI.clear()
        self.game.renderStatusBar()
        UI.line()
        UI.say(self.model.name)
        UI.say(self.model.description)
        UI.line()
        choice = UI.choice(["Harvest"], True)
        if choice == 0:
            return
        if choice == 1:
            self.harvest()
        self.render()

    def harvest(self):
        UI.clear()
        UI.loading(3, "Harvesting herbs...")
        UI.clear()
        UI.say(f"Collected some herbs")
        UI.line()
        UI.wait()
        # find the item by its id
        # self.game.player.rucksack.addItem("LUMBER")
