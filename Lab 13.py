#Amy Gonzales
#Lab 13
#Recursive multiplication lab

def main():
    x = input("Enter first number: ")
    y = input("Enter a second number: ")
    multiply(x, y)
    print "The two numbers multiplied is: ", multiply(x, y)

def multiply(x, y):
    if x==0 or y==0:
        return 0
    else:
        return x + multiply(x, y - 1)

main()
