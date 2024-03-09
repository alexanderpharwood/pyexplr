from app.services.UI import UI
from app.scenes.interactives.base import Base


class LooseGround(Base):
    def render(self):
        UI.clear()
        self.game.renderStatusBar()
        UI.line()
        UI.say(self.model.name)
        UI.say(self.model.description)
        UI.line()
        choice = UI.choice(["Dig"], True)
        if choice == 0:
            return
        if choice == 1:
            self.dig()
        self.render()

    def dig(self):
        UI.clear()
        UI.say("A shovel ought to be useful in this situation.")
        UI.line()
        UI.wait()
