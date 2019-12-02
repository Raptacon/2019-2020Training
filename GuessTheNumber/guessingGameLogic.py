'''

'''
import random
from enum import Enum, auto 

class GameState(Enum):
    kGuessing = auto()
    kWon = auto()
    kLost = auto()

    kGuessTooHigh = auto()
    kGuessTooLow = auto()

class GuessingGameLogic(): 

    def __init__(self, minSec = 1, maxSec = 20, numGuess = 3):
        #start the game
        self.gameState = GameState.kGuessing

        #generate a random number
        self.secretNumber = random.randint(minSec, maxSec)

        #set the number of tries to guess the number
        self.guessesLeft = numGuess

    def getGameState(self): #returns the game state. Also used for guess result (High, low, won, lost)
        return self.gameState
    
    def setUserGuess(self, userGuess): #assignes user guess
        self.userGuess = userGuess
    
    def setGuessResult(self): #processes user guess and set game state accordingly
        if self.secretNumber == self.userGuess:
            self.gameState = GameState.kWon
        elif self.secretNumber < self.userGuess:
            self.gameState = GameState.kGuessTooHigh
        else:
            self.gameState = GameState.kGuessTooLow

        self.guessesLeft -= 1
        
        if self.guessesLeft <= 0 and not self.gameState == GameState.kWon:
            self.gameState = GameState.kLost
    
    def getGuessesLeft(self): #returns how many guesses the user has left
        return self.guessesLeft
    
    def getSecretNumber(self): #returns the secret number if lost. does not return if the game is not lost
        if self.gameState == GameState.kLost:
            return self.secretNumber
    
    def continueGuessing(self): #resets the game state once the user has been told the result
        self.gameState = GameState.kGuessing