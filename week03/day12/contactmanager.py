import json

class Repertoire:
    def __init__(self):
        self.list_contacts = {}

    def add_contact(self, name, number, relation="", surname="", address=""):
        if name not in self.list_contacts:
            self.list_contacts[name] = {
                "name": name,
                "number": number,
                "relation": relation,
                "surname": surname,
                "address": address
            }
        else:
            print("Ce contact existe déjà")
        return self.list_contacts
    
    def save(self):
        return json.dumps(self.list_contacts)

Google = Repertoire()
Google.add_contact("Philippe", "+2290197081988", "amis", "Akandé", "Ekpe, Pk10, Rue des Sciences 7")
repert = Google.save()
print(repert)