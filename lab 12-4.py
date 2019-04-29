#Amy Gonzales
#Lab 12-4
#April 10, 2019
#This program adds a string of integers


index = 0
str = raw_input("Enter a sring of digits: ")
total = 0
    

while index <= len(str) - 1:
    total = total + int(str[index])
    index = index + 1
   

print "The sum of the digits is: ", total


    
