from app.services.UI import UI
from app.scenes.interactives.base import Base


class Tree(Base):
    def render(self):
        UI.clear()
        self.game.renderStatusBar()
        UI.line()
        UI.say(self.model.description)
        UI.line()
        choice = UI.choice(["Collect lumber", "Climb..."], True)
        if choice == 0:
            return
        if choice == 1:
            self.collectLumber()
        if choice == 2:
            self.climb()
        self.render()

    def climb(self):
        UI.clear()
        UI.say("There's a good view from up here, but nothing else of interest.")
        UI.line()
        UI.wait()

    def collectLumber(self):
        UI.clear()
        # Check if they have an axe
        UI.loading(3, "Collecting lumber...")
        UI.clear()
        UI.say(f"Collected {self.model.size} logs")
        UI.line()
        UI.wait()
        # find the item by its id
        # self.game.player.rucksack.addItem("LUMBER")
