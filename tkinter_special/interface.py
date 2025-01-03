from tkinter import *
import time

text = input("Ce que tu veux afficher en 8 secondes: ")
time.sleep(8)
root=Tk()
root.title("Bienvenue sur ma fenêtre")
root.minsize(700, 600)
root.maxsize(1200, 720)

#root.geometry("800x800+0+0")
#root.resizable(False, False)
root.positionfrom("user")
root.config(bg="hotpink")

#les positions--------------Grid------------#

lbl = Label(root, text=text).pack()


root.mainloop()