import random

the_uppercase = "ABCDEFGHIJKLMNOPQRSTUVWXYZ"
the_lowercase = the_uppercase.lower()
the_number = "0123456789"
the_symbol = """!"#$%&'()*+,-./:;<=>?@[\]^_{|}~`"""
charsAll = the_lowercase + the_uppercase + the_number + the_symbol

def genPass ():
    size = int(input("Je vous prie d'entrer la taille que vous souhaitez pour votre mot de passe (au moins 8): "))
    if size >= 8:
        password = ""
        password += the_uppercase[random.randint(0, len(the_uppercase)) - 1]
        password += the_lowercase[random.randint(0, len(the_lowercase)) - 1]
        password += the_number[random.randint(0, len(the_number)) - 1]
        password += the_symbol[random.randint(0, len(the_symbol)) - 1]
        while (len(password) < size):
            password += charsAll[random.randint(0, len(charsAll)) - 1]
        print(password)
    else:
        print("Erreur: au moins un mot de passe de taille 8")
genPass()
