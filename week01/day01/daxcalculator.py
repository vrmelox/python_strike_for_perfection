import sys
import math


def calcul():
    print("Welcome on the Daxcalculator 1.0\n")
    while 1:
        print("Choisis un nombre")
        x = input()
        if x == "exit":
            exit()
        else:
            x = int(x)
        print("Choisis un autre nombre")
        y = input()
        if y == "exit":
            exit()
        else:
            y = int(y)
        print("Tu veux faire quelle operation ? : ")
        operation = input()
        if operation == "+" or operation == "addition":
            print(x + y)
        elif operation == "-" or operation == "soustraction":
            print(x - y)
        elif operation == "*" or operation == "multiplication":
            print(x * y)
        elif operation == "/" or operation == "division":
            if y != 0:
                print(x / y)
            else:
                print("Division par 0")
        elif operation == "exit":
            exit()
        else:
            print("Opération incorrecte")


def main():
    if len(sys.argv) != 1:
        print("We were here before you")
        exit(84)
    calcul()


main()
