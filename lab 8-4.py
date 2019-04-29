#Amy Gonzales
#Lab 6-4
#3-8-2019
#This program provides an average of test scores based on user input
#This program uses input validation loops to ensure valid data is entered

def main():

    endProgram="no"
    while endProgram=="no":
        
        totalScores=0
        counter=0
        scores=0
        averageScores=0
        number=0
        number=getNumber()
        print 'Number is: ', number
        totalScores= getScores(number, totalScores)
        averageScores= getAverage(totalScores, number, averageScores)
        printAverage(averageScores)
        endProgram= raw_input("Do you want to end the program?")
        while not(endProgram=="yes" or endProgram=="no"):
                print "Please enter yes or no"
                endProgram= raw_input("Do you want to end the program?")
        


def getNumber():
    number= input("How many students took the test: ")
    while number < 0 or number > 30:
        print "Enter a number between 1 and 30"
        number= input("How many students took the test: ")
    return number

def getScores(number, totalScores):
    for counter in range(0, number):
        scores= input("Enter score: ")
        while scores < 0 or scores > 100:
            print "Enter a score between 0 and 100"
            scores= input("Enter score: ")
            
        totalScores= totalScores + scores
    return totalScores

def getAverage(totalScores, number, averageScores):
    averageScores= totalScores/number
    return averageScores

def printAverage(averageScores):
    print "Average score is ", averageScores






main()
