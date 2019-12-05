'''
This is a random number guessing game to show parts of python
'''

import guessingGameLogic as ggl
import random
print(dir(ggl))
game = ggl.GuessingGameLogic()

#Print a welcome screen
#print instructions
print("Welcome to my guessing game!")
print("When prompted enter your guess. If you are wrong you lose, maybe.")
print("Only use whole numbers such as '5'. 'Five' does not work.")



#loop
while game.getGameState() == ggl.GameState.kGuessing:
    #get user guess
    try:
        userGuess = int(input("Guess the number:"))

    except TypeError as err:
        print("Please RTFM")
        quit()
        
    except ValueError as err:
        print("Please RTFM")
        quit()

    #see if guess is correct?
    print(game.checkNumber(userGuess))
    if game.getGameState() == ggl.GameState.kWon and input("Congratulations! Would you like to play again? (yes if so)") == "yes":
        game.start()
    if game.getGameState == ggl.GameState.kLost and input("Oh no! Would you like to try again? (yes if so)") == "yes":
        game.start()
print("Goodbye!")