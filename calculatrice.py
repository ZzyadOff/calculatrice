from tkinter import *

# création de la fenêtre
calculatrice = Tk()
calculatrice.title("Calculatrice")
calculatrice.geometry("290x410") # dimension de la fenêtre
calculatrice.configure(bg='#1e1e1e') # couleur du fond de la fenêtre
calculatrice.resizable(False, False) # permet de ne pas pouvoir redimesionner la fenêtre

# variable pour stocker le calcul
texte = StringVar()

# affichage des calculs en haut de la fenêtre
affichage = Label(calculatrice, textvariable=texte, font=("Arial", 32), bg="#1e1e1e", fg="white", anchor="e", padx=15, pady=15)
affichage.pack(fill=X)

# fonction pour les boutons
def ajoute(caractere):
    texte.set(texte.get() + str(caractere)) # ajoute le caractère du bouton ou l'on a cliqué

def effacer():
    texte.set("")

def calculer():
    try:
        texte.set(str(eval(texte.get())))
    except:
        texte.set("Erreur")

# dictionnaire de styles des boutons
btn_op = {"bg": "#ff9f0a", "fg": "white", "activebackground": "#cc7f08", "activeforeground": "white", "bd": 0, "font": ('Arial', 16), "height": 2}
btn_num = {"bg": "#333333", "fg": "white", "activebackground": "#555555", "activeforeground": "white", "bd": 0, "font": ('Arial', 16), "height": 2}
btn_top = {"bg": "#a5a5a5", "fg": "black", "activebackground": "#d4d4d2", "activeforeground": "black", "bd": 0, "font": ('Arial', 16), "height": 2}

# création des boutons
colonne1 = Frame(calculatrice, bg='#1e1e1e')
colonne1.pack(pady=2)
# utilisation de lambda qui permet dans ce cas de créer une fonction sans nom
Button(colonne1, text="AC", width=5, **btn_top, command=effacer).pack(side=LEFT, padx=2)
Button(colonne1, text="%", width=5, **btn_top, command=lambda: ajoute("/100")).pack(side=LEFT, padx=2)
Button(colonne1, text="÷", width=5, **btn_op, command=lambda: ajoute("/")).pack(side=LEFT, padx=2)

colonne2 = Frame(calculatrice, bg='#1e1e1e')
colonne2.pack(pady=2)
Button(colonne2, text="7", width=5, **btn_num, command=lambda: ajoute("7")).pack(side=LEFT, padx=2)
Button(colonne2, text="8", width=5, **btn_num, command=lambda: ajoute("8")).pack(side=LEFT, padx=2)
Button(colonne2, text="9", width=5, **btn_num, command=lambda: ajoute("9")).pack(side=LEFT, padx=2)
Button(colonne2, text="X", width=5, **btn_op, command=lambda: ajoute("*")).pack(side=LEFT, padx=2)

colonne3 = Frame(calculatrice, bg='#1e1e1e')
colonne3.pack(pady=2)
Button(colonne3, text="4", width=5, **btn_num, command=lambda: ajoute("4")).pack(side=LEFT, padx=2)
Button(colonne3, text="5", width=5, **btn_num, command=lambda: ajoute("5")).pack(side=LEFT, padx=2)
Button(colonne3, text="6", width=5, **btn_num, command=lambda: ajoute("6")).pack(side=LEFT, padx=2)
Button(colonne3, text="-", width=5, **btn_op, command=lambda: ajoute("-")).pack(side=LEFT, padx=2)

colonne4 = Frame(calculatrice, bg='#1e1e1e')
colonne4.pack(pady=2)
Button(colonne4, text="1", width=5, **btn_num, command=lambda: ajoute("1")).pack(side=LEFT, padx=2)
Button(colonne4, text="2", width=5, **btn_num, command=lambda: ajoute("2")).pack(side=LEFT, padx=2)
Button(colonne4, text="3", width=5, **btn_num, command=lambda: ajoute("3")).pack(side=LEFT, padx=2)
Button(colonne4, text="+", width=5, **btn_op, command=lambda: ajoute("+")).pack(side=LEFT, padx=2)

colonne5 = Frame(calculatrice, bg='#1e1e1e')
colonne5.pack(pady=2)
Button(colonne5, text="0", width=11, **btn_num, command=lambda: ajoute("0")).pack(side=LEFT, padx=2)
Button(colonne5, text=",", width=5, **btn_num, command=lambda: ajoute(".")).pack(side=LEFT, padx=2)
Button(colonne5, text="=", width=5, **btn_op, command=calculer).pack(side=LEFT, padx=2)

calculatrice.mainloop()
