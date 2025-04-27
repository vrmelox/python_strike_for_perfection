import random


class Jeupendu:
    def __init__(self):
        self.userNumber = None
        self.tentative = 0
        self.xs = None
        self.xe = None
        self.hideNumber = None

    def choixBorne(self):
        while True:
            try:
                self.xs, self.xe = map(
                    int,
                    input(
                        "On joue entre combien et combien (un espace entre les nombres) : "
                    ).split(),
                )
                if self.xs > self.xe:
                    print("Le premier nombre doit être inférieur ou égal au deuxième.")
                    continue
                break
            except ValueError:
                print("Merci d'entrer deux nombres entiers séparés par un espace.")

    def rannumber(self):
        self.hideNumber = random.randint(self.xs, self.xe)

    def jouer(self):
        while self.userNumber != self.hideNumber:
            try:
                self.userNumber = int(
                    input(f"Devinez le nombre entre {self.xs} et {self.xe}: ")
                )
                self.tentative += 1
                if self.userNumber > self.xe or self.userNumber < self.xs:
                    print(f"Remember: on joue entre {self.xs} et {self.xe}")
                    continue
                if self.userNumber < self.hideNumber:
                    print(f"Le nombre est plus grand que {self.userNumber}")
                elif self.userNumber > self.hideNumber:
                    print(f"Le nombre est plus petit que {self.userNumber}")
                else:
                    print(f"Cool, tu as trouvé juste en {self.tentative} tentatives")
                if self.tentative > (self.xe - 2):
                    print("Mon ami, faut laisser maintenant !")
                    break
            except ValueError:
                print("Merci d'entrer des nombres entiers")


pendu = Jeupendu()
pendu.choixBorne()
pendu.rannumber()
pendu.jouer()
