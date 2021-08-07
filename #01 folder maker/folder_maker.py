import os

count = 0
userInput = int(input("Cuantas carpetas quieres crear? "))
while True:
    count += 1
    os.makedirs("#"+str(count))
    if count >= userInput:
        print("Listo!")
        break
    