#Amy Gonzales
#February 28, 2019
#Lab 5-5
#This program asks input for food order and returns a total cost

def main():
    endProgram, endOrder, totalBurger, totalFry, totalSoda, total, tax, subtotal, option, burgerCount, fryCount, sodaCount= declareVariables()
    while endProgram=="no":
        totalBurger, totalFry, totalSoda, total, tax, subtotal= resetVariables()
        while endOrder=="no":
            option=input("enter 1 for burger, 2 for fries, 3 for soda ")
            if option==1:
                #call getBurger
                totalBurger= getBurger(totalBurger, burgerCount)
            elif option==2:
                totalFry= getFry(totalFry, fryCount)
            elif option==3:
                totalSoda= getSoda(totalSoda, sodaCount)

            endOrder= raw_input("do you want to end the order?")
            if endOrder=="yes":
                total= calcTotal(totalBurger, totalFry, totalSoda, total, tax, subtotal)
                printReceipt(total)
                endProgram=raw_input("do you want to end the program?")
                



def declareVariables():
    endProgram="no"
    endOrder="no"
    totalBurger=0
    totalFry=0
    totalSoda=0
    total=0
    tax=0
    subtotal=0
    option=0
    burgerCount=0
    fryCount=0
    sodaCount=0
    return endProgram, endOrder, totalBurger, totalFry, totalSoda, total, tax, subtotal, option, burgerCount, fryCount, sodaCount

def resetVariables():
    totalBurger=0
    totalFry=0
    totalSoda=0
    total=0
    tax=0
    subtotal=0
    return totalBurger, totalFry, totalSoda, total, tax, subtotal

def getBurger(totalBurger, burgerCount):
    burgerCount= input("how many burgers? ")
    totalBurger= totalBurger+burgerCount*.99
    return totalBurger

def getFry(totalFry, fryCount):
    fryCount= input("how many fries? ")
    totalFry= totalFry+fryCount*.79
    return totalFry

def getSoda(totalSoda, sodaCount):
    sodaCount= input("how many sodas? ")
    totalSoda= totalSoda+sodaCount*1.09
    return totalSoda
def calcTotal(totalBurger, totalFry, totalSoda, total, tax, subtotal):
    subtotal= totalBurger+totalFry+totalSoda
    tax= subtotal*0.06
    total= subtotal+tax
    return total

def printReceipt(total):
    print "your total is", total





main()
