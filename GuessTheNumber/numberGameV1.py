'''
This is a random number guessing game to show parts of python
'''

import guessingGameLogic as ggl
import random
game = ggl.GuessingGameLogic()

#Print a welcome screen
#print instructions
print("Welcome to Coopers guessing game! You alawys lose unless you are good.")
print("When prompted enter your guess. If you are wrong you lose, maybe. (Hint we like numbers less than 21 but more than NULL!!!!)")
print("Only use whole numbers. 'Five' does not work.")



#main game loop
while game.getGameState() == ggl.GameState.kGuessing:
    #get user guess
    try:
        game.setUserGuess(int(input("Guess the number:")))
    except TypeError as err:
        print("Please RTFM")

    #process guess
    game.setGuessResult()

    #see if guess is correct?
    game.getGameState()

    #Print output based on game state returned
    if game.getGameState() == ggl.GameState.kWon: #If you won
        print("You are as awsome as Cooper but he still wins.")
    elif game.getGameState() == ggl.GameState.kGuessTooHigh: #if your guess is too high
        print("Too High")
        game.continueGuessing()
    elif game.getGameState() == ggl.GameState.kGuessTooLow: #if your guess is too low
        print("Too Low")
        game.continueGuessing()
    elif game.getGameState() == ggl.GameState.kLost: #if you lost
        print("You lost. There was actual number was %d"%(game.getSecretNumber()))
    
    if game.getGameState() == ggl.GameState.kGuessing: #print guesses left if you are still guessing
        print(f"You have {game.getGuessesLeft()} guesses left")