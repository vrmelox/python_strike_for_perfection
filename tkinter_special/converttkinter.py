import tkinter as tk


def convertir():
    celsius = float(entree_celsius.get())
    fahrenheit = (celsius * 9 / 5) + 32
    label_resultat.config(text=f"{fahrenheit}°F")


fenetre = tk.Tk()
label_celsius = tk.Label(fenetre, text="Celsius:")
entree_celsius = tk.Entry(fenetre)
bouton_convertir = tk.Button(fenetre, text="Convertir", command=convertir)
label_resultat = tk.Label(fenetre, text="")

label_celsius.pack()
entree_celsius.pack()
bouton_convertir.pack()
label_resultat.pack()

fenetre.mainloop()
