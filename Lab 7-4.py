import random
def main():
    counter=0
    number1=0
    number2=0
    right=0
    averageRight=0
    answer=0
    studentName= getName()
     
     while counter < 10:
        number1, number2 = getNumbers()
        answer=getAnswer(number1, number2, answer)
        right= checkAnswer(number1, number2, answer, right)
        counter = counter + 1
    averageRight= results(right, averageRight)
    displayInfo(right, averageRight, studentName)

def getName():
    studentName= raw_input("What is your name? ")
    return studentName

def getNumbers():
    number1 = random.randint(1, 500)
    number2 = random.randint(1, 500)
    return number1, number2

def getAnswer(number1, number2, answer):
    print "What is the answer to the following equation?"
    print number1
    print "+"
    print number2
    answer = input("What is the sum?")
    return answer

def checkAnswer(number1, number2, answer, right):
    if answer == number1 + number2:
        print "Right!"
        right = right+ 1
    else:
        print "Wrong!"
        return right

    def results(right, averageRight):
    averageRight= float(right)/10
    return averageRight
    
def displayInfo(right, averageRight, studentName):
    print "Your name is: ", studentName
    print "Number of problems right: ", right
    print "Your average right is: ", averageRight
main()
    
