import random 
import sys

names = input("Porfavor introduce tu nombre: ").split(" ")

if not (len(names) > 1):
    print("Porfavor introduce tu nombre completo: ")
    sys.exit()
firstLetter = names[0][0]
threeLetterSurname = names[-1][:3]
number = '{:03d}'.format(random.randrange(1, 999))
username = (firstLetter + threeLetterSurname + number)
print(username)