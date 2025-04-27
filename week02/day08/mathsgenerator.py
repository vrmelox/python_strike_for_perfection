import time
import random


class MentalMath:
    def __init__(self):
        self.nombre_un = random.randint(1, 100)
        self.nombre_deux = random.randint(1, 100)
        self.operation = random.randint(1, 4)
        self.result = 0

    def addition(self):
        print(f"{self.nombre_un} + {self.nombre_deux} = ?")
        return self.nombre_un + self.nombre_deux

    def soustraction(self):
        print(f"{self.nombre_un} - {self.nombre_deux} = ?")
        return self.nombre_un - self.nombre_deux

    def division(self):
        if self.nombre_un > self.nombre_deux:
            print(f"{self.nombre_un} / {self.nombre_deux} = ?")
            return self.nombre_un / self.nombre_deux
        else:
            print(f"{self.nombre_deux} / {self.nombre_un} = ?")
            return self.nombre_deux / self.nombre_un

    def multiplication(self):
        print(f"{self.nombre_un} * {self.nombre_deux} = ?")
        return round((self.nombre_un * self.nombre_deux), 2)

    def game_on(self):
        match self.operation:
            case 1:
                self.result = self.addition()
            case 2:
                self.result = self.soustraction()
            case 3:
                self.result = self.division()
            case 4:
                self.result = self.multiplication()
        print("Vous avez 25 secondes...")
        result = int(input("Quel est votre réponse : "))
        if result == self.result:
            print("Vous avez vu juste !")
        else:
            print(f"Faux ! Le résultat est de : {self.result}")


jeu = MentalMath()
jeu.game_on()
