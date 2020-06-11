
import random
import sys

existNumber = int(input("enter a number between 0-10: "))

randomNumber = random.randint(0, 10)

while existNumber != randomNumber:
    (print("exist number:", existNumber, " must match random number: ", randomNumber))

    response = input("enter anything to continue or enter 'q' to exist: \n")
    if response == 'q':
        sys.exit("peace out!")

    randomNumber = random.randint(0, 10)

print("exist number:", existNumber, " and random number:", randomNumber, "matched.")


