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

        #tell the user stats
        print("You have "+str(numGuess)+" guesses, the number is between "+str(minSec)+" and "+str(maxSec)+", inclusive.")

    def getGameState(self):
        return self.gameState

    def checkNumber(self, guess):
        if self.guessesLeft<=0:
            self.gameState = GameState.kLost
            return "Out of guesses!"
        elif guess > self.secretNumber:
            return "Too high! You have "+ str(self.guessesLeft)+" guesses left."
        elif guess == self.secretNumber:
            self.gameState = GameState.kWon
            return "Guessed!"
        elif guess < self.secretNumber:
            return "Too low! You have "+ str(self.guessesLeft)+" guesses left."
        self.guessesLeft = 0

    def start(self, minSec=1, maxSec=20, numGuess=3):
        #start the game
        self.gameState = GameState.kGuessing

        #generate a random number
        self.secretNumber = random.randint(minSec, maxSec)

        #set the number of tries to guess the number
        self.guessesLeft = numGuess