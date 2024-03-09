import sys
import os
import time
import itertools


class UI:
    BACK = "Exit"
    DIVIDER = "--"

    @staticmethod
    def clear() -> None:
        os.system("cls||clear")

    def line(times: int = 1) -> None:
        for _ in range(times):
            print("")

    @staticmethod
    def read() -> str:
        sys.stdin.flush()
        try:
            value: str = input("//: ")
            if value == "!q":  # Emergency escape for dev
                return sys.exit("Process exited via !q")
            return value
        except KeyboardInterrupt:
            return UI.read()

    @staticmethod
    def readChoice(max: int) -> int:
        try:
            choice: int = int(UI.read())
            if choice == 0:
                return choice
            if choice < 1 or choice > max:
                return UI.readChoice(max)
            return choice
        except ValueError:
            return UI.readChoice(max)

    @staticmethod
    def wait(text="Press [enter] to continue ") -> None:
        try:
            UI.sayLine(text)
            input()
        except KeyboardInterrupt:
            return None

    @staticmethod
    def say(message: str) -> None:
        print(message)

    @staticmethod
    def sayLine(message: str) -> None:
        print(message, end="", flush=True)

    def sayLineOverwrite(message: str):
        print(message, end="\r", flush=True)

    def divider():
        UI.say(UI.DIVIDER)

    @staticmethod
    def title(message: str) -> None:
        length: int = len(message)
        for _ in range(length + 4):
            UI.sayLine("*")
        UI.line()
        UI.say("* " + message + " *")
        for _ in range(length + 4):
            UI.sayLine("*")
        UI.line()

    @staticmethod
    def choice(choices: list, back: bool = False) -> int:
        UI.say("╥")
        for i in range(len(choices)):
            UI.say("╠═ " + str(i + 1) + ") " + choices[i])
        if back == True:
            UI.say("║")
            UI.say(f"╠═ 0) {UI.BACK}")
        UI.say("╨")
        return UI.readChoice(len(choices))

    def boolChoice(choices: list) -> int:
        for i in range(len(choices)):
            UI.say(str(i + 1) + ".) " + choices[i])
        UI.line()
        choice = UI.readChoice(len(choices))
        if choice == 1:
            return True
        return False

    @staticmethod
    def backOption():
        UI.say("0) Back")

    @staticmethod
    def loading(duration: int, text=""):
        completedTime = duration * 10
        completed = 0
        for c in itertools.cycle(['|', '/', '-', '\\']):
            completed += 1
            if completed == completedTime:
                break
            UI.sayLineOverwrite(f'\r{text} ' + c)
            time.sleep(0.1)
