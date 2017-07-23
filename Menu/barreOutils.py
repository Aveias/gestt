# -*- coding: utf-8 -*-

from tkinter import *

class BarreOutils():
    
    """Notre fenÃªtre principale.
    Tous les widgets sont stockÃ©s comme attributs de cette fenÃªtre."""
    
    def __init__(self):
	# céation de la fenetre
        self.fenetre = Tk()
        # Booleen fermer : devient true quand on appuie sur le bouton deconnexion
        self.fermer = False
        # Ajout d'un titre
        self.fenetre.title("Menu")
        # Dimension et position fenetre
        self.hauteur = self.fenetre.winfo_screenheight()/1.2
        self.largeur = self.fenetre.winfo_screenwidth()/10;
        
        self.posX = self.fenetre.winfo_screenwidth() - (self.largeur)
        self.posY = self.fenetre.winfo_screenheight()/2 - (self.hauteur / 2)
        # empecher le redimensionnement de la fenetre
        self.fenetre.resizable(width=False, height=False)
        
        # convertir la chaine du paramentre de geometry( en liste de parametre entier
        L,H,X,Y = self.geoliste(self.fenetre.geometry())
        self.fenetre.geometry("%dx%d%+d%+d" % (self.largeur,self.hauteur,self.posX,self.posY)) # affecter les parametre de dimension et position
        
	# Ajout d'un label : titre barre Outils
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
        self.bouton_deconnexion = Button(self.fenetre, text="Deconnexion", command=self.deconnexion)
        self.bouton_deconnexion.pack(side="left")

        
    def deconnexion(self):
        """L'utilisateur veut fermer le programme et se deconnecter"""
        self.fenetre.destroy()
        self.fermer = True
    
    def geoliste(self,g):
        r=[i for i in range(0,len(g)) if not g[i].isdigit()]
        return [int(g[0:r[0]]),int(g[r[0]+1:r[1]]),int(g[r[1]+1:r[2]]),int(g[r[2]+1:])]
    


        
	



