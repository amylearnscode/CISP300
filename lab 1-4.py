#Lab 1-4
#This program calculates how many credits a student has left to complete in
#order to get their degree.
studentName = input("Enter student name: ")
degreeName = input("Enter name of degree: ")
creditsDegree = int(input("Enter the number of credits needed for degree: "))
creditsTaken = int(input("Enter number of credits taken so far: "))
creditsLeft = creditsDegree - creditsTaken
print ('The student\'s name is' , studentName)
print ('The degree is' , degreeName)
print ('Amount of credits left to reach degree: ', creditsLeft)
