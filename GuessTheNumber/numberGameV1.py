'''
This is a random number guessing game to show parts of python
'''

import random

#Print a welcome screen
#print instructions
print("Welcome to Coopers guessing game! You alawys lose unless you are good.")
print("When prompted enter your guess. If you are wrong you lose, maybe. (Hint we like numbers less than 21 but more than NULL!!!!)")
print("Only use whole numbers. 'Five' does not work.")

#start the game
gameState = "guessing"

#generate a random number
secretNumber = random.randint(1,20)
secretNumber = 5 #FIXME
guessesLeft = 3

#loop
while gameState == "guessing":
    #get user guess
    try:
        userGuess = int(input("Guess the number:"))
    except TypeError as err:
        print("Please RTFM")

    #see if guess is correct?
    if secretNumber == userGuess:
        print("You are as awsome as Cooper but he still wins.")
        gameState = "won"
        continue
    elif secretNumber < userGuess:
        print("Too High")
    else:
        print("Too Low")
    
    guessesLeft -= 1
    print(f"You have {guessesLeft} guesses left")

    if not guessesLeft:
        gameState = "lost"
        print("You lost. There was actual number was %d"%(secretNumber))
        continue


