def dedans(result, pro_lis, para, value):
    for x in pro_lis.keys():
        if (pro_lis[x][para] == value):
            result.append(x)
    return result

class Projets:
    def __init__(self):
        self.listprojets = {}

    def add_project(self, titre, date, status=False, observation="RAS"):
        if (titre not in self.listprojets):
            self.listprojets[titre] = {
                "titre": titre,
                "date": date,
                "status": status,
                "observation": observation
            }
        else:
            print("Le projet existe déjà")
        return self.listprojets

    def update_projet(self, titre, newtitre="", date="", status=False, observation="ras"):
        if (titre not in self.listprojets):
            print(f"Le projets {titre} n'existe pas dans votre base de données.")
            return
        if (newtitre != ""):
            self.listprojets[titre]['titre'] = newtitre
            self.listprojets[newtitre] = self.listprojets.pop(titre)
            titre = newtitre
        if (date != ""):
            self.listprojets[titre]['date'] = date
        if (status != False):
            self.listprojets[titre]['status'] = status
        if (observation != "ras"):
            self.listprojets[titre]['observation'] = observation
        return self.listprojets

    def delprojets(self, titre):
        if (titre not in self.listprojets):
            print(f"Le projet {titre} n'existe pas")
            return
        else:
            print("Projet supprimé")
            return self.listprojets.pop(titre)
    
    def showprojets(self, titre="", date="", status=""):
        dico = []
        if (titre == "" and date == "" and status == ""):
            print("Vous devez fournir au moins un paramètre")
        if (titre != ""):
            return self.listprojets[titre]
        elif (date != ""):
            result = dedans(dico, self.listprojets, "date", date)
            return result
        elif (status != ""):
            result = dedans(dico, self.listprojets, "status", status)
            return result

semestre2 = Projets()
semestre2.addprojects("Piscine paradigms", "07-02-2025", False, "Je l'ai validé avec grade A")
semestre2.addprojects("Graphical programming", "02-05-2025", False)
semestre2.addprojects("Project Week", "10-02-2025", True, "Des crédits à gratter")
semestre2.addprojects("Maths module", "17-04-2025", False, "Tous les crédits obtenus avec Grade A")
semestre2.addprojects("Deuxième année", "07-05-2025", True, "GPA 3.80")
print(semestre2.listprojets)

semestre2.updateprojets("Maths module", "Module mathématiques", status=True, observation="Brouhane")
print(semestre2.listprojets)