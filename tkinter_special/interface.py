from tkinter import *
import time

text = """Au commencement Dieu crea. Je ne dois pas etre en retard, sinon ce ne serait pas bien
mais je dois essayer de voir ce qu'il ne pas pas."""
root=Tk()
root.title("Bienvenue sur ma fenêtre")
root.minsize(700, 600)
root.maxsize(1200, 720)

#root.geometry("800x800+0+0")
#root.resizable(False, False)
#root.positionfrom("user")
root.config(bg="hotpink")

#les positions--------------Grid------------#

# lbl = Label(root, text=text).pack()

Entry_name = Entry(root, width=45, show="*")
button_aurevoir = Button(root, text="Aurevoir", background="cyan")
Entry_name.pack()
button_aurevoir.pack()

root.mainloop()