from app.services.UI import UI
from app.scenes.interactives.base import Base


class Grass(Base):
    def render(self):
        UI.clear()
        self.game.renderStatusBar()
        UI.line()
        UI.say(self.model.name)
        UI.say(self.model.description)
        UI.line()
        choice = UI.choice(["Cut"], True)
        if choice == 0:
            return
        if choice == 1:
            self.cut()
        self.render()

    def cut(self):
        UI.clear()
        UI.loading(3, "Cutting grass...")
        UI.clear()
        UI.say(f"Collected some grass")
        UI.line()
        UI.wait()
        # find the item by its id
        # self.game.player.rucksack.addItem("LUMBER")
