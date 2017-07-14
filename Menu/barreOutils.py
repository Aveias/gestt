#-*-coding:UTF-8-*

from tkinter import *

class BarreOutils():
    
    """Notre fenÃªtre principale.
    Tous les widgets sont stockÃ©s comme attributs de cette fenÃªtre."""
    
    def __init__(self):
        self.fenetre = Tk()
        self.message = Label(self.fenetre, text="Barre outils")
        self.message.pack()

	# Bouton qui ouvre le menu Mes projets :
	# dans lequel les utilisateurs pourront visualiser les taches et les temps en cours sur le/ les projets en cours
		
        self.bouton_mesProjets = Button(self.fenetre, text="Mes projets", fg="red")
        self.bouton_mesProjets.pack(side="right")

        
        liste_projets = Listbox(self.fenetre)
        liste_projets.pack()

        liste_projets.insert(END, "gestt")
        liste_projets.insert(END, "ratatouille")
        liste_projets.insert(END, "chouxfleur")
                
	# Bouton Deconnexion
        self.bouton_deconnexion = Button(self.fenetre, text="Deconnexion", command=self.fenetre.destroy)
        self.bouton_deconnexion.pack(side="left")
        

b = BarreOutils()
b.fenetre.mainloop()




