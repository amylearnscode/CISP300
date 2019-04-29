#Amy Gonzales
#March 21, 2019
#Lab 8-5
#This program uses while loops for input validation and calculates
#cell phone minute usage

def main():
        endProgram = "no"
        minutesAllowed = 0
        minutesUsed = 0
        totalDue = 0
        minutesOver = 0

        while endProgram=="no":
            minutesAllowed = getAllowed(minutesAllowed)
            minutesUsed = getUsed(minutesUsed)
            totalDue, minutesOver = calcTotal(minutesAllowed, minutesUsed, totalDue, minutesOver)
            printData(minutesAllowed, minutesUsed, totalDue, minutesOver)
            endProgram = raw_input("Do you want to end the program? yes or no")
            while not (endProgram=="yes" or endProgram=="no"):
                print "Please enter a yes or no"
                endProgram = raw_input("Do you want to end the program? (Enter no to process a new set of scores): ")

def getAllowed(minutesAllowed):
    minutesAllowed = input("Enter minutes allowed between 200 and 800: ")
    while minutesAllowed < 200 or minutesAllowed > 800:
        print "Minutes must be between 200 and 800. "
        minutesAllowed= input("Enter minutes allowed between 200 and 800: ")
    return minutesAllowed

def getUsed(minutesUsed):
    minutesUsed = input("Enter number of minutes used: ")
    while minutesUsed < 0:
        print "Please enter minutes of at least 0"
        print "How many minutes were used?"
    return minutesUsed

def calcTotal(minutesAllowed, minutesUsed, totalDue, minutesOver):
    extra = 0
    if minutesUsed <= minutesAllowed:
        totalDue = 74.99
        minutesOver = 0
        print "You were not over your minutes"
    elif minutesUsed>= minutesAllowed:
        minutesOver = minutesUsed - minutesAllowed
        
        extra = minutesOver*.20
        totalDue = 74.99 + extra
        print "You were over your minutes by ", minutesOver
    return totalDue, minutesOver

def printData(minutesAllowed, minutesUsed, totalDue, minutesOver):
    print "----Monthly Use Report-----"
    print "Minutes allowed were: ", minutesAllowed
    print "Minutes used were: ", minutesUsed
    print "Minutes over were: ", minutesOver
    print "Total due is: ", totalDue

main()
    


    
