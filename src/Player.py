
class Player:

    def __init__(self, name, score):
        self.__name = name
        self.__score = score
        self.__speed = 1

    def getName(self):
        return self.__name

    def setName(self, newName):
        self.__name = newName

    def getScore(self):
        return self.__score

    def setScore(self, newScore):
        self.__score = newScore
    
    def playerScored(self):
        self.__score += 1
   
    def getSpeed(self):
        return self.__speed
   
    def decrementSpeed(self):
        self.__speed *= .85
