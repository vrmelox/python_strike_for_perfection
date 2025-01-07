import random

def guestNumber():
    userNumber = None
    tentative = 0
    while True:
        try:
            xo, xa = map(int, input("On joue entre combien et combien (un espace entre les nombres) : ").split())
            if xo > xa:
                print("Le premier nombre doit être inférieur ou égal au deuxième.")
                continue
            break
        except ValueError:
            print("Merci d'entrer deux nombres entiers séparés par un espace.")

    number = random.randint(xo, xa)
    while(userNumber == None or userNumber != number):
        try:
            userNumber = int(input(f"Devinez le nombre entre {xo} et {xa}: "))
            tentative += 1
            if userNumber > xa or userNumber < xo:
                print(f"Remember: on joue entre {xo} et {xa}")
                continue
            if userNumber < number:
                print(f"Le nombre est plus grand que {userNumber}")
            elif userNumber > number:
                print(f"Le nombre est plus petit que {userNumber}")
            else:
                print(f"Cool, tu as trouvé juste en {tentative} tentatives")
            if tentative > (xa - 2):
                print("Mon ami, faut laisser maintenant !")
                break
        except ValueError:
            print("Merci d'entrer des nombres entiers")




guestNumber()