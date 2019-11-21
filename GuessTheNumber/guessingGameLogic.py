'''

'''
import random
from enum import Enum, auto 

class GameState(Enum):
    kGuessing = auto()
    kWon = auto()
    kLost = auto()

class GuessingGameLogic(): 

    def __init__(self, minSec = 1, maxSec = 20, numGuess = 3):
        #start the game
        self.gameState = GameState.kGuessing

        #generate a random number
        self.secretNumber = random.randint(minSec, maxSec)

        #set the number of tries to guess the number
        self.guessesLeft = numGuess
    def getGameState(self):
        return self.gameState
    def checkNumber(self, guess):
        if self.guessesLeft<=0:
            self.gameState = GameState.kLost
            return "Out of guesses!"
        elif guess > self.secretNumber:
            return "Too high!"
        elif guess == self.secretNumber:
            self.gameState = GameState.kWon
            return "Guessed!"
        elif guess < self.secretNumber:
            return "Too low!"