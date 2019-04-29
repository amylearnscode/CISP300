#Amy Gonzales
#Lab 9-4
#March 26, 2019
#This lab practices arrays and loops


#Lab 9-4 Blood Drive


def main():
  endProgram = 'no'
  print
  while endProgram == 'no':
    print
    
    totalPints = 0
    averagePints = 0
    highPints = 0
    lowPints = 0
    totalPints = 0
    pints = [0] * 7

    
    
    pints = getPints(pints)
    totalPints = getTotal(pints, totalPints)
    averagePints = getAverage(totalPints, averagePints)
    highPints = getHigh(pints, highPints)
    lowPints = getLow(pints, lowPints)
    displayInfo(averagePints, highPints, lowPints)

   
    endProgram = raw_input('Do you want to end program? (Enter no or yes): ')
    while not (endProgram == 'yes' or endProgram == 'no'):
      print 'Please enter a yes or no'
      endProgram = raw_input('Do you want to end program? (Enter no or yes): ')

def getPints(pints):
  counter = 0
  while counter < 7:
      pints[counter] = input('Enter pints collected: ')
      counter = counter + 1
  return pints
      
def getTotal(pints, totalPints):
    counter = 0
    while counter < 7:
        totalPints = totalPints + pints[counter]
        counter = counter + 1
    return totalPints
def getAverage(totalPints, averagePints):
    averagePints = float(totalPints / 7)
    return averagePints
def getHigh(pints, highPints):
    highPints = pints[0]
    counter = 1
    while counter < 7:
        if pints[counter] > highPints:
            highPints = pints[counter]
        counter = counter+1
    return highPints

def getLow(pints, lowPints):
    lowPints = pints[0]
    counter = 1
    while counter < 7:
        if pints[counter] < lowPints:
            lowPints = pints[counter]
        counter = counter+1
    return lowPints 

def displayInfo(averagePints, highPints, lowPints):
    print "Average pints is: ", averagePints
    print "High pints is: ", highPints
    print "Low pints is: ", lowPints

main()

