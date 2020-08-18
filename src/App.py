from Player import Player
from Game import Game

class App:

    def __init__(self):
        self.p1Name = ""
        self.p2Name = ""
        self.promptPlayerNames()
        self.createPlayers()

    def promptPlayerNames(self):
        self.p1Name = str(input("Enter Player 1 Name: "))
        self.p2Name = str(input("Enter Player 2 Name: "))


    def createPlayers(self):
        self.p1 = Player(self.p1Name, 0)
        self.p2 = Player(self.p2Name, 0) 

    def createGame(self):
        self.game = Game(self.p1, self.p2)

app = App()
