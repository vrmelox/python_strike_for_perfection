import re
import sys
import os
def getText():
    if (len(sys.argv) != 2):
        print("Qu'en un programme, un seul fichier tienne jusqu'à la fin le programme exécuté !")
        sys.exit()
    else:
        file_path = sys.argv[1]
        if os.path.exists(file_path) and os.path.getsize(file_path) != 0:
            with open(file_path, "r") as text:
                content = text.read()
                return content
        else:
            print("Au commencement, le fichier doit existé et du texte il doit contenir.")
            sys.exit()
def wordCount():
    motOften = {}
    text = getText()
    ch = 0
    text = re.sub(r'\n', '', text)
    charatersAll = len(text)
    print(f"Pour votre texte créé, le créateur l'a doté de {charatersAll} caractères avec espace.")
    for x in text :
        if x != " ":
            ch += 1
    print(f"Le créateur, ayant horreur du vide a doté votre texte de {ch} caractères.")
    textMots = re.sub(r'[,;.?!:]', '', text.lower())
    mots = textMots.split()
    nombreMots = len(mots)
    print(f"En {nombreMots} mots, le créateur a formé ce texte.")
    phrases = re.split(r'[.?!]', text)
    phrases = [phrase.strip() for phrase in phrases if phrase.strip()]
    print(f"En {len(phrases)} phrases ce texte fut formé.")
    unikmots = set(mots)
    print(f"Sans redondance, le créateur a utilisé {len(unikmots)} unique pour façonner ce texte.")
    for x in unikmots:
        number = mots.count(x)
        motOften[x] = number
    sorted_motOften = dict(sorted(motOften.items(), key=lambda item : item[1]))
    print(f"Les dix mots les plus utilisés sont :\n")
    counter = 0
    while counter < 10 :
        for x in sorted_motOften.items():
            print(f"{x[0]} : {x[1]}")
        counter += 1
wordCount()