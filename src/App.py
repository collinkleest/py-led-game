from Player import Player
from Game import Game

# app starting class


class App:
    def __init__(self: object) -> None:
        players: list = self.promptPlayerNames()
        self.createPlayers(players)
        self.createGame()

    # gets both players names
    def promptPlayerNames(self) -> list:
        p1Name = str(input("Enter Player 1 Name: "))
        p2Name = str(input("Enter Player 2 Name: "))
        return([p1Name, p2Name])

    # create player objects for game
    def createPlayers(self: object, players: list) -> None:
        # player 1 starts first (name, score, isTurn, isP1)
        self.p1 = Player(players[0], 0, True)
        self.p2 = Player(players[1], 0, False)

    def createGame(self: object) -> None:
        self.game: object = Game(self.p1, self.p2)


# create an app object, grab game object and call start game
if __name__ == "__main__":
    app: object = App()
    app.game.startGame()
