#Amy Gonzales
#Lab 7-3 March 13, 2019
#This lab uses the random number library and picks a winner of a dice roll
#Lab 7-3 The Dice Game
#add libraries needed
import random

#the main function
def main():
    print
    #initialize variables
    endProgram='no'
    winnerName=0
    playerOne= 'NO NAME'
    playerTwo= 'NO NAME'
    

    
    playerOne, playerTwo = inputNames(playerOne, playerTwo)


    #while loop to run program again
    while endProgram == 'no':

        #initialize variables
        winnersName='NO NAME'
        p1number=0
        p2number=0
        #call to rollDice
        winnerName = rollDice(p1number, p2number, playerOne, playerTwo, winnerName)
        displayInfo(winnerName)
#call to displayInfo


        endProgram = raw_input('Do you want to end program? (Enter yes or no): ')


#this function gets the players names
def inputNames(playerOne, playerTwo):
    playerOne= raw_input("Enter first players name: ")
    playerTwo= raw_input("Enter second players name: ")
    return playerOne, playerTwo
    

#this function will get the random values
def rollDice(p1number, p2number, playerOne, playerTwo, winnerName):
    p1number = random.randint(1, 6)
    p2number = random.randint(1, 6)
    if p1number==p2number:
        winnerName= "TIE"
    elif p1number>p2number:
            winnerName=playerOne
    elif p1number<p2number:
            winnerName=playerTwo
    return winnerName

    

#this function displays the winner
def displayInfo(winnerName):
    print "The winner is: ", winnerName


# calls main
main()
