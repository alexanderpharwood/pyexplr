from app.services.UI import UI
from app.scenes.map import Map as MapScene
from app.scenes.area import Area as AreaScene
from app.models.Save import Save
from app.models.region import Region
from app.models.area import Area
from app.models.clock import Clock
from app.models.weather import Weather
from app.models.player import Player


class Game:
    def __init__(self, save: Save):
        self.save = save
        self.back = False
        self.clock = Clock(save.clock)
        self.player = Player(save.player)
        self.setGeography()

    def render(self):
        UI.clear()
        if self.back:
            self.back = False
            return
        self.commitSave()
        self.renderStatusBar()
        UI.line()
        UI.say(self.area.name)
        UI.say(self.area.getCurrentSituation())
        UI.say(self.weather.getReport())
        UI.line()
        self.renderActions()
        return self.render()

    def renderStatusBar(self):
        UI.say(
            f"{self.clock.formatDateTime()} | {self.weather.getShortReport()} | {self.region.name} > {self.area.name}")

    def setRegion(self) -> None:
        self.region = Region.create(self.player.region)

    def setArea(self):
        self.area = Area.create(self.player.area)
        self.areaScene = AreaScene(self)

    def setWeather(self):
        self.weather = Weather(self.region, self.area, self.clock)
        currentAreaConditions = self.save.getWeatherConditionsForArea(
            self.area.id)
        if currentAreaConditions != None and currentAreaConditions["day"] == self.clock.day:
            self.weather.conditions = currentAreaConditions["conditions"]
        else:
            self.weather.generateCurrentConditions()

    def setGeography(self):
        self.setRegion()
        self.setArea()
        self.setWeather()

    def applySaveData(self):
        self.save.player = self.player.toDict()
        self.save.clock = self.clock.toDict()
        currentAreaConditionsToDict = self.weather.currentAreaConditionsToDict()
        self.save.setWeatherConditions(currentAreaConditionsToDict)

    def commitSave(self):
        self.applySaveData()
        self.save.writeToDisk()

    def renderActions(self):
        choice: int = UI.choice([
            "Explore",
            "Rucksack",
            "Map",
        ], True)

        match choice:
            case 0:
                self.back = True
            case 1:
                self.areaScene.render()
            case 2:
                self.renderRucksack()
            case 3:
                map = MapScene(self)
                map.render()

    def renderRucksack(self) -> None:
        UI.clear()
        UI.say(f"Gold: ${self.player.rucksack.gold}")
        UI.line()
        print(self.player.rucksack.items)
        UI.line()
        UI.say(f"Your rucksack is x% full")
        UI.wait()
