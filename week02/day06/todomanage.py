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