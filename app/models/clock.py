from app.services.utilities import generateHash


class Clock:
    unit: int = 15
    seasons: list[str] = ["Spring", "Summer", "Autumn", "Winter"]

    def __init__(self, properties: dict):
        self.minute: int = properties["minute"]
        self.minuteHash: int = properties["minuteHash"]
        self.hour: int = properties["hour"]
        self.hourHash: int = properties["hourHash"]
        self.day: int = properties["day"]
        self.dayHash: int = properties["dayHash"]
        self.season: int = properties["season"]
        self.seasonHash: int = properties["seasonHash"]
        self.year: int = properties["year"]
        self.yearHash: int = properties["yearHash"]

    def toDict(self) -> dict:
        return {
            "minute": self.minute,
            "minuteHash": self.minuteHash,
            "hour": self.hour,
            "hourHash": self.hourHash,
            "day": self.day,
            "dayHash": self.dayHash,
            "season": self.season,
            "seasonHash": self.seasonHash,
            "year": self.year,
            "yearHash": self.yearHash,
        }

    def increment(self, units: int = 1):
        # Units represents the number of Clock.unit intervals by which we will increment the time
        for _ in range(units):
            self.minute += self.unit
            self.minuteHash = generateHash()
            if self.minute == 60:
                self.minute = 0
                self.incrementHour(1)
        pass

    def incrementHour(self, hours: int):
        for _ in range(hours):
            self.hour += 1
            self.hourHash = generateHash()
            if self.hour == 24:
                self.hour = 0
                self.incrementDay(1)
        pass

    def incrementDay(self, days: int):
        for _ in range(days):
            self.day += 1
            self.dayHash = generateHash()
            if self.day == 29:
                self.day = 1
                self.incrementSeason(1)

    def incrementSeason(self, seasons: int):
        for _ in range(seasons):
            self.season += 1
            self.seasonHash = generateHash()
            if self.season == 4:
                self.season = 0
                self.incrementYear(1)

    def incrementYear(self, years: int):
        for _ in range(years):
            self.year += 1
            self.yearHash = generateHash()

    def formatTime(self):
        formatted = ""
        if self.hour < 10:
            formatted += "0"
        formatted += f"{self.hour}:"
        if self.minute == 0:
            formatted += "0"
        formatted += f"{self.minute}"
        return formatted

    def formatDate(self):
        return f"Day {self.day} of {Clock.seasons[self.season]}, Year {self.year}"

    def formatDateTime(self):
        return f"{self.formatTime()} | {self.formatDate()}"
