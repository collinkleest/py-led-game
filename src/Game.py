import json
import gpiozero as gpio
import sys
from time import sleep

class Game:
    
    def __init__(self, p1, p2):
        self.player1 = p1
        self.player2 = p2
        self.gameSpeed = 1
        self.pointThreshold = 10
        self.p1BtnNum = 0
        self.p2BtnNum = 0 
        self.ledArrNums = []
        self.ledArr = []
        self.turn = 'p1'
        self.run = True 

    def readConfig(self):
        with open('config/gpio-config.json', 'r') as file:
            data = json.load(file)
            self.p1BtnNum = data['p1Btn']
            self.p2BtnNum = data['p2Btn']
            self.ledArrNums = data['ledArray']
    
    def initializeGPIO(self):
        for i in self.ledArrNums:
            tempLed = gpio.LED(i)
            self.ledArr.append(tempLed)
        self.p1Btn = gpio.Button(self.p1BtnNum)
        self.p2Btn = gpio.Button(self.p2BtnNum)
        self.p1Btn.when_pressed = self.btnCheck1
        self.p2Btn.when_pressed = self.btnCheck2


    def btnCheck1(self):
        if (self.currentLed.pin == self.ledArr[len(self.ledArr)-1].pin and self.currentLed.is_active and self.turn == 'p1'):
            self.hasWon()
            self.turn = 'p2'
            self.player1.playerScored()
            self.player1.decrementSpeed()
            print(self.player1.getName(), 'Score:', self.player1.getScore())
        elif (self.turn == 'p1'):
            self.turn = 'p2'
            print(self.player1.getName(), 'missed!') 

    def btnCheck2(self):
        if (self.currentLed.pin == self.ledArr[0].pin and self.currentLed.is_active and self.turn == 'p2'):
            self.hasWon()
            self.turn = 'p1'
            self.player2.playerScored()
            self.player2.decrementSpeed()
            print(self.player2.getName(), 'Score:', self.player2.getScore())
        elif (self.turn == 'p2'):
            self.turn = 'p1'
            print(self.player2.getName(), 'missed!')


    def startGame(self):
        self.readConfig()
        self.initializeGPIO()
        self.loopLeds()
    
    def hasWon(self):
        if (self.player1.getScore() >= 10):
            print(self.player1.getName(), 'has won!')
            self.run = False
            sys.exit()

        if (self.player2.getScore() >= 10):
            print(self.player2.getName(), 'has won!')
            self.run = False
            sys.exit()

    def loopLeds(self):
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

 
