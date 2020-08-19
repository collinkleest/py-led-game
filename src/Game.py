import json
from gpiozero import (Button, LED)
from time import sleep
from Player import Player


class Game:

    run: bool = True

    def __init__(self: object, p1: Player, p2: Player) -> None:
        self.player1: Player = p1
        self.player2: Player = p2
        self.gameSpeed: float = 1
        self.p1BtnNum: int = 0
        self.p2BtnNum: int = 0
        self.ledArrNums: list = []
        self.ledArr: list = []

    # read rpi gpio pin configuration, located at config/gpio-config.json
    def readConfig(self: object) -> None:
        with open('config/gpio-config.json', 'r') as file:
            data: dict = json.load(file)
            self.p1BtnNum = data['p1Btn']
            self.p2BtnNum = data['p2Btn']
            self.ledArrNums = data['ledArray']

    # initialize all gpio pins with gpiozero module
    # store leds in array and buttons in vars
    def initializeGPIO(self: object) -> None:
        for i in self.ledArrNums:
            tempLed = LED(i)
            self.ledArr.append(tempLed)
        self.p1Btn = Button(self.p1BtnNum)
        self.p2Btn = Button(self.p2BtnNum)
        self.p1Btn.when_pressed = self.btnCheck1
        self.p2Btn.when_pressed = self.btnCheck2

    # check player 1 scored
    def btnCheck1(self: object) -> None:
        if (self.currentLed.pin == self.ledArr[len(self.ledArr)-1].pin and self.currentLed.is_active and self.player1.getIsTurn()):
            self.player1.playerScored()
            self.player1.decrementSpeed()
            print(self.player1.getName(), 'Score:', self.player1.getScore())
            self.player2.checkScore()
            # switch turns
            self.player1.setIsTurn(False)
            self.player2.setIsTurn(True)

        elif (self.player1.getIsTurn):
            print(self.player1.getName(), 'missed!')
            # switch turns
            self.player1.setIsTurn(False)
            self.player2.setIsTurn(True)

    # check player 2 scored
    def btnCheck2(self: object) -> None:
        if (self.currentLed.pin == self.ledArr[0].pin and self.currentLed.is_active and self.player2.getIsTurn()):
            self.player2.playerScored()
            self.player2.decrementSpeed()
            print(self.player2.getName(), 'Score:', self.player2.getScore())
            self.player2.checkScore()
            # switch turns
            self.player2.setIsTurn(False)
            self.player1.setIsTurn(True)
        elif (self.player2.getIsTurn()):
            print(self.player2.getName(), 'missed!')
            # switch turns
            self.player2.setIsTurn(False)
            self.player1.setIsTurn(True)

    def startGame(self: object) -> None:
        self.readConfig()
        self.initializeGPIO()
        self.loopLeds()

    def loopLeds(self: object) -> None:
        while self.run:
            for i in self.ledArr[1:len(self.ledArr)]:
                i.on()
                self.currentLed = i
                sleep(self.player1.getSpeed())
                i.off()

            revArr = self.ledArr[::-1]
            for i in revArr[1:len(revArr)]:
                i.on()
                self.currentLed = i
                sleep(self.player2.getSpeed())
                i.off()
