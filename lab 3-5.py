#Amy Gonzales
#February 14, 2019
#This program takes guesses for age, weight and birth
#month and decides if the answer is correct.

def main():
    age= getAge()
    weight= getWeight()
    birthMonth= getbirthMonth()
    correctAnswers(age, weight, birthMonth)

def getAge():
    age=input('Enter your guess for age ')
    return age

def getWeight():
    weight= input('Enter a guess for weight ')
    return weight

def getbirthMonth():
    birthMonth= raw_input('Guess a birth month ')
    return birthMonth

def correctAnswers(age, weight, birthMonth):
    if age <= 25:
        print 'Congrats, age is 25 or less!'
    if weight >= 128:
        print 'Congrats, weight is 128 or more!'
    if birthMonth =='April':
        print 'Congrats, April is the right month!'

main()
