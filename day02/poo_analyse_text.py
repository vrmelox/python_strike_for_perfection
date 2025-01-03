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
    ligne = 0
    motOften = []
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
        motOften.append([x, number])
        ligne += 1
    for x in motOften:
        print(x)
wordCount()