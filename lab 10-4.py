#Amy Gonzales
#April 4,2019
#Lab 10-4
#This program compares energy costs after "going green".
#It sends the savings array to a text file.


def main():
 
    endProgram = "no"
    notGreenCost = [0] * 12
    goneGreenCost = [0] * 12
    savings = [0] * 12
    months = ['January', 'February', 'March', 'April', 'May', 'June', 'July', 'August', 'September', 'October', 'November', 'December']
    option = 0
    while endProgram == "no":
            getNotGreen(notGreenCost, months)
            getGoneGreen(goneGreenCost, months)
            energySaved(notGreenCost, goneGreenCost, savings)
            writeToFile(months, savings)
            option = input("Press 1 to display info, or 2 to read from file: ")
            if option == 1:
                    displayInfo(notGreenCost, goneGreenCost, savings, months)
            elif option == 2:
                    readFromFile(months, savings)
            endProgram = raw_input('Do you want to end program? (Enter no or yes): ')
    while not (endProgram == 'yes' or endProgram == 'no'):
      print 'Please enter a yes or no'
      endProgram = raw_input('Do you want to end program? (Enter no or yes): ') 

def writeToFile(months, savings):
    outFile = open('savings.txt', 'a')
    print >> outFile, 'Savings'
    counter = 0
    while counter < 12:
        outFile.write(str(months[counter]) + '\n')
        outFile.write(str(savings[counter]) + '\n')
        counter = counter + 1
    outFile.close()


def readFromFile(months, savings):
    inFile = open('savings.txt', 'r')
    str1 = inFile.read()
    print str1
    months = inFile.read()
    print months
    print  
    savings = inFile.read()
    print savings
    inFile.close()
            
def getNotGreen(notGreenCost, months):
    counter = 0
    while counter < 12:
        print months[counter]
        notGreenCost[counter] = input("Enter NOT GREEN cost: ")
        counter = counter + 1
    return notGreenCost

def getGoneGreen(goneGreenCost, months):
    counter = 0
    while counter < 12:
        print months[counter]
        goneGreenCost[counter] = input("Enter GONE GREEN cost: ")
        counter = counter + 1
    return goneGreenCost

def energySaved(notGreenCost, goneGreenCost, savings):
    counter=0
    while counter < 12:
        savings[counter] = notGreenCost[counter]- goneGreenCost[counter]
        counter = counter + 1
    return savings

def displayInfo(notGreenCost, goneGreenCost, savings, months):
    counter = 0
    while counter < 12:
        print "Information for: ", months[counter]
        print "Savings is $ ", savings[counter]
        print "Not green cost is $ ", notGreenCost[counter]
        print "Gone green cost is $ ", goneGreenCost[counter]
        counter = counter + 1

main()
    
    
 







