import requests


class ExchangeRates:
    def __init__(self):
        self.key_api = "53c90981d86964cb6b31a98dc4fba2c9"
        self.api_url = "https://api.exchangeratesapi.io/v1/latest"
        self.params = {"access_key": self.key_api}
        self.rates = {}

    def getcurrencies(self):
        response = requests.get(self.api_url, params=self.params)

        if response.status_code == 200:
            data = response.json()
            self.rates = data["rates"]
        else:
            print(f"An error occured with the error_code {response.status_code}")

    def convertRates(self):
        print(
            f"Voici toutes les devises que nous convertissons :\n {self.rates.keys()}"
        )
        devise = input(
            "Entrez la devise d'arrivée, le montant et la devise de base (les trois séparés par des espaces): "
        ).split()
        try:
            if self.rates[devise[0].upper()] and self.rates[devise[2].upper()]:
                eur_base = round(self.rates[devise[2].upper()], 2)
                eur_arrivee = round(self.rates[devise[0].upper()], 2)
                base_eur = float(devise[1]) / eur_base
                result = round((base_eur * eur_arrivee), 2)
                print(f"{devise[1]} {devise[2]} en {devise[0]} = {result} {devise[0]}")
            else:
                print("Il y a une erreur. Merci de revoir")
        except KeyError:
            print("Désolé, la devise n'existe pas chez nous ou revoyez l'écriture")


kuriconv = ExchangeRates()
kuriconv.getcurrencies()
kuriconv.convertRates()
