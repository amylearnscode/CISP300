#Lab 5-4
#Amy Gonzales
#February 27, 2019
#This program adds a daily bottle count and produces a total bottle
#count and total payout

#the main function
def main():
   endProgram = 'no'
   while endProgram == 'no':
    totalBottles = getBottles()
    totalPayout = calcPayout(totalBottles)
    printInfo(totalBottles, totalPayout)
    endProgram = raw_input('Do you want to end the program? (Enter yes or no): ')
def getBottles():
    totalBottles = 0
    todayBottles = 0
    counter = 1
    while counter <= 7:
       todayBottles = input('Enter number of bottles for today: ')
       totalBottles = totalBottles + todayBottles
       counter = counter + 1
    return totalBottles
def calcPayout(totalBottles):
    totalPayout = 0
    totalPayout = totalBottles * .10
    return totalPayout
def printInfo(totalBottles, totalPayout):
    print 'The total number of bottles collected is', totalBottles
    print 'The total paid out is $', totalPayout

 
        


        
#calls main
main()
