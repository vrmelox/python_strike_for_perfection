import tkinter as tk

def convertir():
    try:
        celsius = float(entree_celsius.get())
        conversion_type = variable.get()  # Récupère le choix de l'utilisateur

        if conversion_type == "fahrenheit":
            resultat = (celsius * 9/5) + 32
            label_resultat.config(text=f"{resultat}°F")
        elif conversion_type == "kelvin":
            resultat = celsius + 273.15
            label_resultat.config(text=f"{resultat} K")
        else:  # Cas où rien n'est sélectionné (ne devrait pas arriver avec les Radiobuttons)
            label_resultat.config(text="Veuillez choisir un type de conversion.")
    except ValueError:
        label_resultat.config(text="Veuillez entrer une valeur numérique.")


fenetre = tk.Tk()
fenetre.title("Convertisseur Celsius") # Ajoute un titre à la fenêtre

label_celsius = tk.Label(fenetre, text="Celsius:")
entree_celsius = tk.Entry(fenetre)

# Création des Radiobuttons pour le choix de la conversion
variable = tk.StringVar(value="fahrenheit") # Variable pour stocker le choix, par défaut Fahrenheit
radio_fahrenheit = tk.Radiobutton(fenetre, text="Fahrenheit", variable=variable, value="fahrenheit")
radio_kelvin = tk.Radiobutton(fenetre, text="Kelvin", variable=variable, value="kelvin")

bouton_convertir = tk.Button(fenetre, text="Convertir", command=convertir)
label_resultat = tk.Label(fenetre, text="")

# Placement des widgets avec grid pour un meilleur contrôle
label_celsius.grid(row=0, column=0, sticky="w") # sticky="w" aligne à gauche
entree_celsius.grid(row=0, column=1, padx=5) # padx ajoute un espace horizontal
radio_fahrenheit.grid(row=1, column=0, sticky="w")
radio_kelvin.grid(row=1, column=1, sticky="w")
bouton_convertir.grid(row=2, column=0, columnspan=2, pady=10) # columnspan fusionne les deux colonnes, pady ajoute un espace vertical
label_resultat.grid(row=3, column=0, columnspan=2)

fenetre.mainloop()