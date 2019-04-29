#Amy Gonzales
#Lab 2-7 February 7, 2019
#This program calculates state and county tax.

def main():
    monthlySales= inputSales()
    countyTax = calcCounty(monthlySales)
    stateTax = calcState(monthlySales)
    totalTax = calcTotal(countyTax, stateTax)
    printInfo(countyTax, stateTax, totalTax)

def inputSales():
    monthlySales= input("Enter sales for the month: ")
    return monthlySales

def calcCounty(monthlySales):
    countyTax = monthlySales * .02
    return countyTax

def calcState(monthlySales):
    stateTax = monthlySales * .04
    return stateTax
    
def calcTotal(countyTax, stateTax):
    totalTax = countyTax + stateTax
    return totalTax

def printInfo(countyTax, stateTax, totalTax):
    print "County tax is: ", countyTax
    print "State tax is ", stateTax
    print "Total tax is ", totalTax

main()
