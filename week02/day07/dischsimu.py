import random


class dishsimu:
    def __init__(self):
        self.dishnumber = 0
        self.dishface = 0
        self.result = 0

    def choixDishNumber(self):
        while True:
            try:
                self.dishnumber = int(
                    input("Veuillez choisir le nombre de dés que vous souhaitez: ")
                )
                break
            except ValueError:
                print("Merci d'entrer un nombre valide")

    def choixDishFace(self):
        while True:
            try:
                self.dishface = int(input("Vos dés auront combien de faces : "))
                break
            except ValueError:
                print("Cher ami, entre un nombre valide: ")

    def simuleLancerDish(self):
        iterator = 1
        retour = 0
        while iterator <= self.dishnumber:
            retour = random.randint(1, self.dishface)
            print(f"Dé numéro {iterator}: {retour}")
            self.result += retour
            iterator += 1
        print(f"Résultat: {self.result}")


des = dishsimu()
des.choixDishNumber()
des.choixDishFace()
des.simuleLancerDish()
