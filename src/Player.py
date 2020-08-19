from sys import exit


class Player:

    def __init__(self: object, name: str, score: int):
        self.__name: str = name
        self.__score: int = score
        self.__speed: float = 1

    def getName(self: object) -> str:
        return self.__name

    def setName(self: object, newName: str):
        self.__name = newName

    def getScore(self: object) -> int:
        return self.__score

    def setScore(self: object, newScore: int):
        self.__score = newScore

    def playerScored(self: object):
        self.__score += 1

    def getSpeed(self: object) -> float:
        return self.__speed

    def decrementSpeed(self: object):
        self.__speed *= .85

    def checkScore(self: object):
        if (self.__score >= 10):
            print(self.__name, "has won!")
            print("EXITING GAME")
            exit()
