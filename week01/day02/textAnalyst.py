import re
import sys
import os


def getText():
    if len(sys.argv) != 2:
        print("Erreur: vous devez fournir un seul document .txt")
        sys.exit()
    else:
        file_path = sys.argv[1]
        if os.path.exists(file_path) and os.path.getsize(file_path) != 0:
            with open(file_path, "r") as text:
                content = text.read()
                return content
        else:
            print("Le document doit contenir du texte")
            sys.exit()


def motFreken(motOften):
    sorted_motOften = dict(
        sorted(motOften.items(), key=lambda item: item[1], reverse=True)
    )
    print(f"Les dix mots les plus utilisés sont :")
    counter = 0
    for x in sorted_motOften.items():
        print(f"{x[0]} : {x[1]}")
        counter += 1
        if counter == 10:
            break


def wordCount():
    motOften = {}
    text = getText()
    ch = 0
    text = re.sub(r"\n", "", text)
    charatersAll = len(text)
    print(f"Votre texte contient {charatersAll} caractères avec espace.")
    for x in text:
        if x != " ":
            ch += 1
    print(f"Votre texte contient {ch} caractères (sans espace).")
    textMots = re.sub(r"[,;.?!:]", "", text.lower())
    mots = textMots.split()
    nombreMots = len(mots)
    print(f"Le texte contient {nombreMots} mots")
    phrases = re.split(r"[.?!]", text)
    phrases = [phrase.strip() for phrase in phrases if phrase.strip()]
    print(f"Le texte est constitué de {len(phrases)} phrases.")
    unikmots = set(mots)
    print(f"Le texte contient {len(unikmots)} mots unique.")
    for x in unikmots:
        number = mots.count(x)
        motOften[x] = number
    motFreken(motOften)


wordCount()
