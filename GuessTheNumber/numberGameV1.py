'''
This is a random number guessing game to show parts of python
'''

import guessingGameLogic as ggl
import random
print(dir(ggl))
game = ggl.GuessingGameLogic()
print(game)
quit()

#Print a welcome screen
#print instructions
print("Welcome to Coopers guessing game! You alawys lose unless you are good.")
print("When prompted enter your guess. If you are wrong you lose, maybe. (Hint we like numbers less than 21 but more than NULL!!!!)")
print("Only use whole numbers. 'Five' does not work.")



#loop
while game.getGameState() == ggl.GameState.kGuessing:
    #get user guess
    try:
        userGuess = int(input("Guess the number:"))
    except TypeError as err:
        print("Please RTFM")

    #see if guess is correct?
    print(game.checkNumber(userGuess))


