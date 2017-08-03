# -*- coding: utf-8 -*-

from tkinter import *
from tkinter.messagebox import *
from PIL import Image, ImageTk


class BarreOutils():

    """Notre fenêtre principale.
    Tous les widgets sont stockés comme attributs de cette fenêtre."""

    def __init__(self):
	# céation de la fenetre
        self.fenetre = Tk()
        # Booleen fermer : devient  true quand on appuie sur le bouton deconnexion
        self.fermer = False
        # Dimension et position fenetre
        self.hauteur = self.fenetre.winfo_screenheight()/1.2 # 80% de la page en hauteur
        self.largeur = self.fenetre.winfo_screenwidth()/10;  # 10% de la page en largeur

        self.posX = self.fenetre.winfo_screenwidth() - (self.largeur) # collé à droite de la page
        self.posY = self.fenetre.winfo_screenheight()/2 - (self.hauteur / 2) # centré en hauteur
        # empecher le redimensionnement de la fenetre
        self.fenetre.resizable(width=False, height=False)

        # convertir la chaine du paramentre de geometry( en liste de parametre entier
        L,H,X,Y = self.geoliste(self.fenetre.geometry())
        self.fenetre.geometry("%dx%d%+d%+d" % (self.largeur,self.hauteur,self.posX,self.posY)) # affecter les parametre de dimension et position

	# Ajout d'un label : titre barre Outils
        self.fenetre.title("Menu")
        # taille des boutons
        self.largeurBoutons = self.largeur - self.largeur * 0.08
        self.hauteurBoutons = self.hauteur / 5 - self.hauteur * 0.01

        # Liste des projets
        #liste_projets = Listbox(self.fenetre)
        #liste_projets.grid(row=2,column=1)

        #liste_projets.insert(END, "gestt")
        #liste_projets.insert(END, "ratatouille")
        #liste_projets.insert(END, "chouxfleur")
################################################################################################################
	# Bouton tache rapides
        image = Image.open('fleche.png')
        photo = ImageTk.PhotoImage(image)
        self.bouton_tache_rapide = Button(self.fenetre, image=photo,width=self.largeurBoutons,height=self.hauteurBoutons, command=self.open_taches_rapides)
        self.bouton_tache_rapide.grid(row=3,column=1, padx = self.largeur * 0.02)
        self.bouton_tache_rapide.image = photo
################################################################################################################
	# Bouton Nouveau Projet
        image = Image.open('plus4.png')
        photo = ImageTk.PhotoImage(image)
        self.bouton_deconnexion = Button(self.fenetre, image=photo,width=self.largeurBoutons,height=self.hauteurBoutons, command=self.open_nouveau_projet)
        self.bouton_deconnexion.grid(row=4,column=1)
        self.bouton_deconnexion.image = photo
################################################################################################################
	# Bouton Rapports
        image = Image.open('graphe.png')
        photo = ImageTk.PhotoImage(image)
        self.bouton_deconnexion = Button(self.fenetre, image=photo,width=self.largeurBoutons,height=self.hauteurBoutons, command=self.open_rapports)
        self.bouton_deconnexion.grid(row=5,column=1)
        self.bouton_deconnexion.image = photo
################################################################################################################
	# Bouton Naviguer
        image = Image.open('loupe.jpg')
        photo = ImageTk.PhotoImage(image)
        self.bouton_naviguer = Button(self.fenetre, image=photo,width=self.largeurBoutons,height=self.hauteurBoutons, command=self.naviguer)
        self.bouton_naviguer.grid(row=6,column=1)
        self.bouton_naviguer.image = photo
################################################################################################################
	# Bouton Deconnexion
        image = Image.open('deco.jpg')
        photo = ImageTk.PhotoImage(image)
        self.bouton_deconnexion = Button(self.fenetre, image=photo,width=self.largeurBoutons,height=self.hauteurBoutons, command=self.deconnexion)
        self.bouton_deconnexion.grid(row=7,column=1)
        self.bouton_deconnexion.image = photo
################################################################################################################
    def deconnexion(self,*args):
        """L'utilisateur veut fermer le programme et se deconnecter"""
        self.callback()
        if self.fermer == True:
            self.fenetre.destroy()
    def open_taches_rapides(self,*args):
        """L'utilisateur veut ouvrir la fenetre des taches rapides"""
        toplevel = Toplevel(self.fenetre)
        toplevel.title('Subroot')
        # TODO : ouvrir la fenetre des taches rapides
    def open_nouveau_projet(self,*args):
        """L'utilisateur veut ouvrir la fenetre des nouveaux projets"""
        # TODO : ouvrir la fenetre des nouveaux projets
    def open_rapports(self,*args):
        """L'utilisateur veut ouvrir la fenetre des rapports"""
        # TODO : ouvrir la fenetre des rapports
    def naviguer(self,*args):
        """L'utilisateur veut ouvrir la fenetre des rapports"""
        # TODO : ouvrir la fenetre de navigation
        self.fenetre.state('iconic')

    def geoliste(self,g):
        r=[i for i in range(0,len(g)) if not g[i].isdigit()]
        return [int(g[0:r[0]]),int(g[r[0]+1:r[1]]),int(g[r[1]+1:r[2]]),int(g[r[2]+1:])]

    def callback(self):
        if askyesno('Deconnexion', 'Êtes-vous sûr de vouloir vous deconnecter ?'):
            self.fermer = True
        else:
            #showinfo('Titre 3', 'Vous avez peur!')
            #showerror("Titre 4", "Aha")
            self.fermer = False

b = BarreOutils()
print(b.fenetre.geometry())
print(b.largeurBoutons)
print(b.hauteurBoutons)
b.fenetre.mainloop()
