#Amy Gonzales
# 2/7/2019
#Lab 2

#This program demonstrates how to use variables and 
#functions.


#This program uses functions and variables

#the main function
def main():
    print ('Welcome to the tip calculator program')
    print   #prints a blank line
    name= inputName()
    print ('Hello', name)
    age= inputAge()
    print ('You are', age)
def inputName():
    name= input('What is your name?')
    return name
def inputAge():
    age= input('What is your age?')
    return age
    

#calls main
main()
