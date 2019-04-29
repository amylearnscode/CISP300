#Amy Gonzales
#Lab 1-6
#This program requires user to enter day of week and steps taken and calculates
#calories burned.

dayWeek = input("Enter day of the week.")
stepsTaken = float(input("Enter number of steps taken."))

milesWalked = stepsTaken/2000
calorieLoss = milesWalked*65

print("Today is: ", dayWeek)
print("Calories burned: ", calorieLoss)
