from app.services.UI import UI
from app.factories.interactive import InteractiveFactory


class Area:
    def __init__(self, game):
        self.game = game
        self.interactives = []
        self.populateInteractives()
        self.back = False

    def populateInteractives(self):
        self.interactives = InteractiveFactory.getForArea(self.game)
        if len(self.interactives) == 0:
            self.interactives = InteractiveFactory.generate(self.game)
            for interactive in self.interactives:
                self.game.save.addInteractive(
                    interactive.model.toDict())

    def render(self):
        if self.back:
            self.back = False
            return
        UI.clear()
        self.game.renderStatusBar()
        UI.line()
        UI.say(
            f"Exploring the {self.game.area.name} area ({self.game.area.size}/{self.game.area.size})")
        UI.line()
        names = list(map(lambda inter: inter.model.name, self.interactives))
        choice = UI.choice(names, True)
        if choice == 0:
            return

        interactive = self.interactives[choice - 1]
        interactive.render()
        self.render()
