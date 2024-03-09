from os import makedirs
import config
from app.services.UI import UI
from app.scenes.Menu import Menu

makedirs(config.SAVE_LOCATION, exist_ok=True)

UI.clear()

menu = Menu()
menu.render()
