#Amy Gonzales
#April 3, 2019
#Lab 10-3
#This program writes stats about a blood drive to a file and can read those
#stats back from the file

#the main function
def main():
  endProgram = 'no'
  print
  while endProgram == 'no':
    option = 0
    print
    print 'Enter 1 to enter in new data and store to file'
    print 'Enter 2 to display data from the file'
    option = input('Enter now ->')
    print
    
    
    pints = [0] * 7
    totalPints = 0
    averagePints = 0

    if option == 1:
      
      pints = getPints(pints)
      totalPints = getTotal(pints, totalPints)
      averagePints = getAverage(totalPints, averagePints)
      writeToFile(averagePints, pints)
      
    else:
      readFromFile(averagePints, pints)
      
   
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
  averagePints = float(totalPints) / 7
  return averagePints


def writeToFile(averagePints, pints):
    outFile = open('blood.txt', 'a')
    print >> outFile, 'Pints Each Hour'
    counter = 0
    while counter < 7:
        outFile.write(str(pints[counter]) + '\n')
        counter = counter + 1
    print >> outFile, 'Average Pints'
    outFile.write(str(averagePints) + '\n')
    outFile.close()


def readFromFile(averagePints, pints):
    inFile = open('blood.txt', 'r')
    str1 = inFile.read()
    print str1
    pints = inFile.read()
    print pints
    print  
    str2 = inFile.read()
    print str2
    averagePints = inFile.read()
    print averagePints
    inFile.close()
 

main()
