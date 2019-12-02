'''
This is a random number guessing game to show parts of python
'''

import guessingGameLogic as ggl

game = None
gamesWon = 0
gamesLost = 0
gamesPlayed = 0
gamePlaying = True
gameSelectedRange = None
gameDifficulies = ((1,10, 4), (1,100, 7), (1,1000, 10))

def welcome():
    print("Welcome to the number guessing game")
    print("When promted enter your guess.")
    help()

def help():
    print("Use 'Help' to get help")
    print("Use 'Quit' to quit")
    print("Use 'List' to get a list")
    print("use 'Reset' to restart the game")

def farwell():
    print("Thanks for playing")
    print("You won %d of %d games"%(gamesWon, gamesPlayed))

def getDifficulty():
    global gamePlaying
    global game
    game = None
    while game == None:
        try:
            userInput = input("Please select a difficulty (1-3) or quit:")
            userInput = userInput.lower()
            if userInput == 'quit':
                gamePlaying = False
                break
            try:
                difficulty = int(userInput)
                assert(difficulty > 0)
                assert(difficulty < 41)
                createGame(difficulty-1)
            except:
                pass
        except KeyboardInterrupt:
            print("Please use quit")


def createGame(difficulty):
    global game
    global gamesPlayed
    global gameSelectedRange
    gameSelectedRange = gameDifficulies[difficulty]
    game = ggl.GuessingGameLogic(*gameSelectedRange)
    gamesPlayed +=1

def listGuesses():
    gusses = game.getGuessHistory()
    currGuess = 1
    for guess in gusses:
        if guess[1] == ggl.GuessResults.kLow:
            result = "Too Low"
        elif guess[1] == ggl.GuessResults.kHigh:
            result = "Too High"
        elif guess[1] == ggl.GuessResults.kCorrect:
            result = "Correct"
        print("%d: %d is %s"%(currGuess, guess[0], result))
        currGuess +=1

def getUserGuess():
    validGuess = None
    while not validGuess:
        try:
            userInput = input("Please enter guess (or cmd) between %d and %d: "%(gameSelectedRange[0], gameSelectedRange[1])).lower()
            if userInput == "help":
                help()
            elif userInput == "quit":
                validGuess = ggl.GameControl.kQuit
            elif userInput == "list":
                listGuesses()
            else:
                try:
                    validGuess = int(userInput)
                except:
                    print("Invalid argument %s"%(userInput))
        except KeyboardInterrupt:
            print("Please use quit")    
    return validGuess


def playRound():
    global gamesWon, gamesLost
    game.start()
    while not game.isGameOver():
        guess = getUserGuess()
        result = game.makeGuess(guess)

        if(result == ggl.GuessResults.kLow):
            print("%d was too low. %d guesses remaing"%(guess, game.getGuessesRemaining()))
        if(result == ggl.GuessResults.kHigh):
            print("%d was too high. %d guesses remaing"%(guess, game.getGuessesRemaining()))
        if(result == ggl.GuessResults.kCorrect):
            print("You got it in %d guesses."%(len(game.getGuessHistory())))

    secretNumber = game.getSecretNumber()
    totalGuesses = len(game.getGuessHistory())
    if game.isGameWon():
        print("Great job you won. The correct number was %d. You got it in %d guesses"%(secretNumber, totalGuesses))
        gamesWon +=1
    else:
        print("You lost. The correct number was %d. You tried %d guesses"%(secretNumber, totalGuesses))
        gamesLost +=1

def main():
    welcome()
    while gamePlaying:
        getDifficulty()
        if game:
            playRound()
    farwell()

if __name__ == "__main__":
    main()
    quit()
