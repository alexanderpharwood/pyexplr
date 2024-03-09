from io import TextIOWrapper

class File:

    @staticmethod
    def write(location: str, content: str) -> None:
        f: TextIOWrapper = open(location, "w")
        f.write(content)
        f.close()

    @staticmethod
    def read(location: str) -> str:
        f: TextIOWrapper = open(location, "r")
        value: str = f.read()
        f.close()
        return value

    
