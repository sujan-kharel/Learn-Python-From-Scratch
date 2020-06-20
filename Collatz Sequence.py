import sys


def collatz(num):
    if num == 1:
        sys.exit()
    elif num % 2 == 0:
        num /= 2
        print(int(num))
    elif num % 2 == 1:
        num = (num * 3) + 1
        print(int(num))
    collatz(num)


try:
    userInput = int(input("Enter an integer value: "))
    collatz(userInput)
except ValueError:
    print("The input must be an integer")
