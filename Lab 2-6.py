#Amy Gonzales
#2/7/2019

#This program uses functions and variables

#the main function
def main():
    print ('Welcome to the meal calculator program')
    print   #prints a blank line
    mealPrice= input_meal()
    tip= calc_tip(mealPrice)
    tax= calc_tax(mealPrice)
    total= calc_total(mealPrice, tip, tax)
    print_info(mealPrice, tip, tax, total)

#this function will input meal price
def input_meal():
    mealPrice= float(input('Enter price of meal: '))
    return mealPrice

#this function will calculate tip at 20%
def calc_tip(mealPrice):
    if mealPrice>=0.01 and mealPrice <= 5.99:
        tip= mealPrice*.10
    elif mealPrice >= 6.00 and mealPrice <= 12.00:
        tip= mealPrice*.13
    elif mealPrice >=12.01 and mealPrice <= 17.00:
        tip= mealPrice*.16
    elif mealPrice >= 17.01 and mealPrice <=25.00:
        tip= mealPrice*.19
    elif mealPrice>= 25.01:
        tip= mealPrice*.22
    return tip

#this function will calculate tax at 6%
def calc_tax(mealPrice):
    tax= mealPrice * .06
    return tax

#this function will calculate tip, tax, and the total #cost
def calc_total(mealprice, tip, tax):
    		total = mealprice + tip + tax
    		return total


#this function will print tip, tax, the mealprice, and #the total
def print_info(mealPrice, tip, tax, total):
    print 'The mealprice is' , mealPrice
    print 'The tip is' , tip
    print 'The tax is' , tax
    print 'The total is' , total
    
    
#calls main
main()
