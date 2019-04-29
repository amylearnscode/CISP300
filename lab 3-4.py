#Amy Gonzales
#Lab 3-4

#This program will demonstrate how to use
#decision statements in Python

#This program determines if a bonus should be awarded

#The main function
def main():
    print 'Welcome to the program'
    monthlySales = getSales()  # gets sales
    isBonus(monthlySales) #determines bonus
    isDayoff(monthlySales) #determines day off
    

#This function gets the monthly sales
def getSales():
    monthlySales = input('Enter the monthly sales $')
    monthlySales = float(monthlySales)
    return monthlySales

def isBonus(monthlySales):
    if monthlySales >= 100000:
        print "You earned a $5000 bonus!!"

def isDayoff(monthlySales):
    if monthlySales >= 112500:
        print "You earned a day off!!"

#calls main
main()
