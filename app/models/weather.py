from random import randint


class Weather:
    BASE: int = 12
    SEASON_MODIFIERS: list[list[int]] = [[1, 3], [5, 5], [3, 1], [-5, -5]]
    HOUR_MODIFIERS: list[int] = [-5, 1, 5, -3]
    CONDITIONS: list[str] = [
        "SUNNY", "RAINING", "SNOWING", "WINDY", "OVERCAST"
    ]
    CONDITIONS_FORMATTED: list[str] = ["Sunny", "Raining",
                                       "Snowing", "Windy", "Overcast"]

    def __init__(self, region, area, clock):
        self.region = region
        self.area = area
        self.clock = clock
        self.conditions = None
        self.temperature: int | None = None

    def generateCurrentConditions(self):
        # Currently, this is just random
        # We can tae into account: temperature, season, altitude (set altitude in regions data - can show this on map)
        self.conditions = self.CONDITIONS[randint(0, len(self.CONDITIONS) - 1)]

    def getConditions(self):
        return self.CONDITIONS_FORMATTED[self.conditions.index(self.conditions)]

    def getReport(self):
        return f"Current conditions are {self.getConditions().lower()}, with a temperature of {self.getTemperature()}°C"

    def getShortReport(self):
        return f"{self.getConditions()}, {self.getTemperature()}°C"

    def calculateTemperature(self):
        self.temperature: int = self.BASE
        self.temperature += self.region.temperatureModifier
        self.temperature += self.area.temperatureModifier
        self.temperature += self.getSeasonModifier()
        self.temperature += self.getHourModifier()
        self.temperature += self.generateFluctuation()

    def getTemperature(self) -> int:
        if self.temperature == None:
            self.calculateTemperature()
        return self.temperature

    def generateFluctuation(self):
        return randint(-2, 2)

    def getSeasonModifier(self):
        seasonMod: list[int] = self.SEASON_MODIFIERS[self.clock.season]
        if (self.clock.day < 15):
            return seasonMod[0]
        return seasonMod[1]

    def getHourModifier(self):
        if (self.clock.hour < 6):
            return self.HOUR_MODIFIERS[0]
        if (self.clock.hour < 12):
            return self.HOUR_MODIFIERS[1]
        if (self.clock.hour < 18):
            return self.HOUR_MODIFIERS[2]
        return self.HOUR_MODIFIERS[3]

    def currentAreaConditionsToDict(self):
        return {
            "day": self.clock.day,
            "area": self.area.id,
            "conditions": self.conditions
        }
