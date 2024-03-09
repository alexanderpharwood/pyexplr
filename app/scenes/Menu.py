from os import walk
import sys
import config
from app.services.UI import UI
from app.models.Save import Save
from app.scenes.CharacterCreation import CharacterCreation
from app.scenes.Game import Game


class Menu:

    def render(self):
        UI.clear()
        self.renderSplash()
        UI.line(3)
        UI.wait()
        UI.clear()
        self.renderSplash()
        UI.line()
        UI.say("What would you like to do?")
        UI.line()
        choice: int = UI.choice(["New character", "Load character"], True)
        match choice:
            case 0:
                UI.clear()
                sys.exit(0)
            case 1:
                CharacterCreation().render()
            case 2:
                self.loadSave()
        return self.render()

    def loadSave(self):
        UI.clear()
        UI.say("Choose a save file")
        UI.line()
        choices = []
        for (_, _, fileNames) in walk(config.SAVE_LOCATION):
            choices.extend(fileNames)
            break
        choice = UI.choice(list(
            map(
                lambda c: c.replace(f".{config.SAVE_EXTENSION}", ''),
                choices
            )
        ),
            True
        )

        if (choice == 0):
            return

        save = None
        try:
            save = Save.readFromDisk(choices[choice - 1])
        except Exception as e:
            print(e)
            UI.say(f"Failed to load save file: {choices[choice - 1]}")
            UI.line()
            UI.wait()
            return
        game = Game(save)
        UI.clear()
        UI.say(f"Loaded {save.player['name']} successfully")
        UI.line()
        UI.wait()
        return game.render()

    def renderSplash(self):
        UI.say("""
  _______  __   __  _______  ___      _______  ______    _______ 
 |       ||  |_|  ||       ||   |    |       ||    _ |  |       |
 |    ___||       ||    _  ||   |    |   _   ||   | ||  |    ___|
 |   |___ |       ||   |_| ||   |    |  | |  ||   |_||_ |   |___ 
 |    ___| |     | |    ___||   |___ |  |_|  ||    __  ||    ___|
 |   |___ |   _   ||   |    |       ||       ||   |  | ||   |___ 
 |_______||__| |__||___|    |_______||_______||___|  |_||_______|
""")
