import string
import random

print("Bienvenido al este generador de constraseñas!")

largo = int(input('\nIntroduce el largo de la contraseña: '))
UPPER = string.ascii_uppercase
LOWER = string.ascii_lowercase
NUMBERS = string.digits
PUNCTUATION = string.punctuation

TOTAL = UPPER + LOWER + NUMBERS + PUNCTUATION

temp = random.sample(TOTAL,largo)

password = "".join(temp)

print('\nTu contraseña es: "' + password + '"' '\n')