import random

min_val = 1
max_val = 6

roll_again = "yes"

while roll_again == "yes" or roll_again == "y":
    print("Tirando el dado...")
    print("Los valores son: ")

    print(random.randint(min_val, max_val))

    print(random.randint(min_val, max_val))

    roll_again = input("Quieres tirarlos de nuevo?")