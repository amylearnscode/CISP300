#Amy Gonzales
#Lab 12-6
#april 11, 2019
#This program translates phone numbers.

SIZE = 26
def main():
    index=0
    phone = raw_input("Enter a phone number in the form xxx-xxx-xxxx ")
    while index <= (len(phone) - 1):
        print translate(phone[index])
        index = index + 1
    
    
def translate(ch):
    letters = ("A", "B", "C", "D", "E", "F", "G","H", "I", "J", "K", "L", "M", "N","O", "P", "Q", "R", "S", "T", "U","V", "W", "X", "Y", "Z")
    digits = ("2", "2", "2", "3", "3", "3", "4","4", "4", "5", "5", "5", "6", "6","6", "7", "7", "7", "7", "8", "8","8", "9", "9", "9", "9")
    found = False
    index = 0
    translated = ch
    while not found and index < SIZE:
        if ch == letters[index]:
            found = True
            translated = digits[index]
        index = index + 1
    return translated
    
main()

 
