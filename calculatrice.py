from tkinter import *

# création de la fenêtre
calculatrice = Tk()
calculatrice.title("Calculatrice")
calculatrice.geometry("280x400") # dimension de la fenêtre
calculatrice.configure(bg='#262626') # couleur du fond de la fenêtre
calculatrice.resizable(False, False) # permet de ne pas pouvoir redimesionner la fenêtre

# variable pour stocker le calcul
texte = StringVar()

# affichage des calculs en haut de la fenêtre
affichage = Label(calculatrice, textvariable=texte, font=("Arial", 30), bg="#262626", fg="white")
affichage.pack()

# fonction pour les boutons
def ajoute(caractere):
    texte.set(texte.get() + str(caractere)) # ajoute le caractère du bouton ou l'on a cliqué

def effacer():
    texte.set("")

def calculer():
    texte.set(str(eval(texte.get())))

# création des boutons
colonne1 = Frame(calculatrice, bg='#262626')
colonne1.pack()
# utilisation de lambda qui permet dans ce cas de créer une fonction sans nom
Button(colonne1, text="AC", width=5, height=2, font=('Arial', 16), bg='#a5a5a5', command=effacer).pack(side=LEFT, padx=1, pady=1)
Button(colonne1, text="%", width=5, height=2, font=('Arial', 16), bg='#a5a5a5', command=lambda: ajoute("/100")).pack(side=LEFT, padx=1, pady=1)
Button(colonne1, text="÷", width=5, height=2, font=('Arial', 16), bg='#ff9900', fg='white', command=lambda: ajoute("/")).pack(side=LEFT, padx=1, pady=1)

colonne2 = Frame(calculatrice, bg='#262626')
colonne2.pack()
Button(colonne2, text="7", width=5, height=2, font=('Arial', 16), bg='#a5a5a5', command=lambda: ajoute("7")).pack(side=LEFT, padx=1, pady=1)
Button(colonne2, text="8", width=5, height=2, font=('Arial', 16), bg='#a5a5a5', command=lambda: ajoute("8")).pack(side=LEFT, padx=1, pady=1)
Button(colonne2, text="9", width=5, height=2, font=('Arial', 16), bg='#a5a5a5', command=lambda: ajoute("9")).pack(side=LEFT, padx=1, pady=1)
Button(colonne2, text="X", width=5, height=2, font=('Arial', 16), bg='#ff9900', fg='white', command=lambda: ajoute("*")).pack(side=LEFT, padx=1, pady=1)

colonne3 = Frame(calculatrice, bg='#262626')
colonne3.pack()
Button(colonne3, text="4", width=5, height=2, font=('Arial', 16), bg='#a5a5a5', command=lambda: ajoute("4")).pack(side=LEFT, padx=1, pady=1)
Button(colonne3, text="5", width=5, height=2, font=('Arial', 16), bg='#a5a5a5', command=lambda: ajoute("5")).pack(side=LEFT, padx=1, pady=1)
Button(colonne3, text="6", width=5, height=2, font=('Arial', 16), bg='#a5a5a5', command=lambda: ajoute("6")).pack(side=LEFT, padx=1, pady=1)
Button(colonne3, text="-", width=5, height=2, font=('Arial', 16), bg='#ff9900', fg='white', command=lambda: ajoute("-")).pack(side=LEFT, padx=1, pady=1)

colonne4 = Frame(calculatrice, bg='#262626')
colonne4.pack()
Button(colonne4, text="1", width=5, height=2, font=('Arial', 16), bg='#a5a5a5', command=lambda: ajoute("1")).pack(side=LEFT, padx=1, pady=1)
Button(colonne4, text="2", width=5, height=2, font=('Arial', 16), bg='#a5a5a5', command=lambda: ajoute("2")).pack(side=LEFT, padx=1, pady=1)
Button(colonne4, text="3", width=5, height=2, font=('Arial', 16), bg='#a5a5a5', command=lambda: ajoute("3")).pack(side=LEFT, padx=1, pady=1)
Button(colonne4, text="+", width=5, height=2, font=('Arial', 16), bg='#ff9900', fg='white', command=lambda: ajoute("+")).pack(side=LEFT, padx=1, pady=1)

colonne5 = Frame(calculatrice, bg='#262626')
colonne5.pack()
Button(colonne5, text="0", width=11, height=2, font=('Arial', 16), bg='#a5a5a5', command=lambda: ajoute("0")).pack(side=LEFT, padx=1, pady=1)
Button(colonne5, text=",", width=5, height=2, font=('Arial', 16), bg='#a5a5a5', command=lambda: ajoute(".")).pack(side=LEFT, padx=1, pady=1)
Button(colonne5, text="=", width=5, height=2, font=('Arial', 16), bg='#ff9900', fg='white', command=calculer).pack(side=LEFT, padx=1, pady=1)

calculatrice.mainloop()