'''

'''
import random
from enum import Flag, Enum, auto 

class GuessResults(Enum):
    kLow = auto()
    kHigh = auto()
    kCorrect = auto()
    kQuit = auto()

class GameControl(Enum):
    kQuit = auto()

class GameState(Flag):
    kNone = 0
    kInGame = auto()
    kGameWon = auto()
    kGameLost = auto()
    kGameOver = kGameWon | kGameLost

class GameNotRunning(Exception):
    """Exception if game is not running (not started or lost/won)"""
    pass

class GameNotOver(Exception):
    """Exception to raise if game is not over and access is violated"""
    pass

class GuessingGameLogic(): 

    def __init__(self, minSec = 1, maxSec = 10, numGuess = 3, rangeDifficulty = 1, guessDifficulty = 1):
        """
        Creates a new game logic class and itilizes the game to ready.

        Parameters:
        minSec (int) minimum value for random number
        maxSex (int) maximam value for random number
        numGuess (int) number of guesses before game ends
        difficultly (float) scales number of guesses and range based on difficulty.
        """
        #Initilize variables

        #
        assert(minSec < maxSec)
        self.randRange = int(maxSec - minSec)
        self.randOffset = int(minSec) * rangeDifficulty
        self.scaledGuesses = int(numGuess * guessDifficulty + 0.5)
        assert (self.scaledGuesses > 0)


        self.reset()

    def reset(self):
        """
        Resets the game state, generates base random value, resets the guess counts and 
        makes game ready to accept guesses
        """
        self.gameState = GameState.kNone
        self.currGuess = 0
        self.guessHistory = []
        self.__secret__ = int(random.random() * self.randRange + self.randOffset +.5)

    def __str__(self):
        """
        Prints a string repr of class.
        """
        return "%s : currGuess %d of %d. Range %d to %d"%(
            str(self.__class__), 
            self.currGuess, 
            self.scaledGuesses, 
            self.randOffset, self.randRange - self.randOffset+2)

    def start(self):
        """
        Indicates game is running
        """
        self.gameState |= GameState.kInGame

    def isInGame(self):
        """
        Checks if game is running

        Returns:
        true if game is running
        """
        return bool(GameState.kInGame in self.gameState) and not self.isGameOver()

    def isGameOver(self):
        """
        Checks if game is over
        Returns True if game is over, else false if game is running or not started
        """
        return  bool(self.gameState & GameState.kGameOver)

    def isGameWon(self):
        """
        Returns true if game has been lost
        """
        return bool(GameState.kGameWon in self.gameState)
    
    def isGameLost(self):
        """
        Returns true if game has been lost
        """
        return bool(GameState.kGameLost in self.gameState)

    def getGuessHistory(self):
        """
        returns a list of tuples (guess,result) to call
        """
        return self.guessHistory

    def getGuessesRemaining(self):
        """
        returns the number of remaining guesses
        """
        return self.scaledGuesses - self.currGuess

    def getSecretNumber(self):
        """
        returns the secret number. If called outside of the will raise an exception
        """
        if not self.isGameOver():
            raise GameNotOver("Game is not over and secret can not be read")
        return self.__secret__

    def makeGuess(self, guess):
        """
        Causes the game to process a guess.
        Parameter:
        guess (int) guess for user to check against. (GameControl) controls gameplay, (None) quits
        Returns:
        k
        """
        if(not self.isInGame()):
            error = "Game is not running. Current state %s"%(self.gameState)
            raise GameNotRunning(error)

        if(isinstance(guess ,GameControl) or guess is None):
            self.gameState |= GameState.kGameLost
            return GuessResults.kQuit

        #save a history
        results = self.__checkGuess__(guess)
        self.guessHistory.append((guess, results))
        self.currGuess += 1

        if results == GuessResults.kCorrect:
            self.gameState |= GameState.kGameWon
        elif self.currGuess >= self.scaledGuesses:
            self.gameState |= GameState.kGameLost
        
        return results

    def __checkGuess__(self, guess):
        """
        takes a guess and returns the results without changing game state.
        """
        results = GuessResults.kCorrect
        if guess < self.__secret__:
            results = GuessResults.kLow
        if guess > self.__secret__:
            results = GuessResults.kHigh
        return results



if __name__ == "__main__":
    game = GuessingGameLogic()
    print(game)
    while(game.__secret__ != 1):
        game.reset()
        print(game.__secret__)
    
    game.start()
    print("good guess")
    try:
        while(True):
            print(game.makeGuess(5))
    except GameNotRunning as e:
        print(e)
    print(game.getSecretNumber())
    quit()