import time
from random import randint
from app.services.UI import UI
from app.scenes.interactives.base import Base


class FishingSpot(Base):
    def render(self):
        UI.clear()
        self.game.renderStatusBar()
        UI.line()
        UI.say(self.model.name)
        UI.say(self.model.description)
        UI.line()
        choice = UI.choice(["Cast a line"], True)
        if choice == 0:
            return
        if choice == 1:
            self.dig()
        self.render()

    def dig(self):
        UI.clear()
        # UI.say("A rod ought to be useful in this situation.")

        threshold = randint(200, 1000)
        trigger = randint(3, 10)
        for i in range(trigger):
            if i + 1 == trigger:
                start = int(time.time() * 1000)
                UI.line()
                check = UI.read()
                print(check)
                UI.wait("That's a bite! ")
                end = int(time.time() * 1000)
                UI.clear()
                if end - start > threshold:
                    UI.clear()
                    UI.say(
                        "That one got away. THey are quick as anthing, these fish!")
                    UI.line()
                else:
                    UI.say("Gotcha!")
                    UI.say("Description of generated fish based on area, etc!")
                    UI.line()
                break
            else:
                UI.say(".")
                time.sleep(1)
        UI.wait()
