#Amy Gonzales
#Lab 6-4
#3-8-2019
#This program provides an average of test scores based on user input

def main():

    endProgram, totalScores, counter, scores, averageScores, number = declaredVariables()
    while endProgram=="no":
        endProgram, totalScores, counter, scores, averageScores, number = declaredVariables()

        number=getNumber()
        totalScores= getScores(counter, scores, number, totalScores)
        averageScores= getAverage(totalScores, scores, averageScores)
        printAverage(averageScores)
        endProgram= raw_input("Do you want to end the program?")

def declaredVariables():
    endProgram="no"
    totalScores=0.0
    counter=0
    scores=0.0
    averageScores=0.0
    number=0
    return endProgram, totalScores, counter, scores, averageScores, number
def getNumber():
    number= input("How many students took the test: ")
    return number

def getScores(counter, scores,number, totalScores):
    for counter in range(0, number):
        scores= input("Enter score: ")
    totalScores= totalScores+scores

    return totalScores
def getAverage(totalScores, number, averageScores):
    averageScores= totalScores/number
    return averageScores
def printAverage(averageScores):
    print "Average score is ", averageScores






main()
