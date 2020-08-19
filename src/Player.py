from sys import exit


class Player:

    __pointThreshold: int = 10

    def __init__(self: object, name: str, score: int, isTurn: bool):
        self.__name: str = name
        self.__score: int = score
        self.__speed: float = 1
        self.__isTurn: bool = isTurn

    def getName(self: object) -> str:
        return self.__name

    def setName(self: object, newName: str) -> None:
        self.__name = newName

    def getScore(self: object) -> int:
        return self.__score

    def setScore(self: object, newScore: int) -> None:
        self.__score = newScore

    def playerScored(self: object) -> None:
        self.__score += 1

    def getSpeed(self: object) -> float:
        return self.__speed

    def decrementSpeed(self: object) -> None:
        self.__speed *= .85

    def getIsTurn(self: object) -> bool:
        return self.__isTurn

    def setIsTurn(self: object, isTurn: bool) -> None:
        self.__isTurn = isTurn

    def checkScore(self: object) -> None:
        if (self.__score >= self.__pointThreshold):
            print(self.__name, "has won!")
            print("EXITING GAME")
            exit()
