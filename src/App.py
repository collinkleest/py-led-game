from Player import Player
from Game import Game


class App:
    def __init__(self: object):
        players: list = self.promptPlayerNames()
        self.createPlayers(players)
        self.createGame()

    def promptPlayerNames(self) -> list:
        p1Name = str(input("Enter Player 1 Name: "))
        p2Name = str(input("Enter Player 2 Name: "))
        return([p1Name, p2Name])

    def createPlayers(self: object, players: list):
        self.p1 = Player(players[0], 0)
        self.p2 = Player(players[1], 0)

    def createGame(self: object):
        self.game: object = Game(self.p1, self.p2)


if __name__ == "__main__":
    app: object = App()
    app.game.startGame()
