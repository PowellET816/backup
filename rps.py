# Ethan Powell 
# rock paper scissors 
# rps.py
# added coment for github
import random
# variables
pScpre = 0
cScore = 0
ties= 0
cMoves = ["Rock", "Paper", "Scissors"]
# welcome message

print(" Hi, Lets play Rock Paper Scissors")

pName = input("what is your name? ")

def printScore():


	print("Score: ")

	print(pName + ": " + srt(pScore))

	print("Computer Score: " + str(cScore))

	print("Tiles: " + srt(tiles))

while True:

	pMove = input("Enter 'r' for rock 'p' for paper and 's' for scissors oe 'q' to quit")

	printScore()
	print(pName + " picked rock")

	if pMove == 'q':
        break
    cMove = random.choice(cMoves)


    if pMove == "r":
    	if pMove == "rock":
    		print("computer picks Rock")
    		prrint("tie")


    elif cMove == "p":
    	pass

    elif pMove == "s":
    	pass

    else:
    	print("that is not an option ")

