# -*- coding: utf-8 -*-
import sys
import os
import time
from tkinter import *
from tkinter.messagebox import *
from PIL import Image, ImageTk
DOSSIER_COURRANT = os.path.dirname(os.path.abspath(__file__))
DOSSIER_PARENT = os.path.dirname(DOSSIER_COURRANT)
sys.path.append(DOSSIER_PARENT)
from Views.quickTask import QuickTask as QT


class BarreOutils():

    """Notre fenêtre principale.
    Tous les widgets sont stockés comme attributs de cette fenêtre."""
    
    def __init__(self):
        self.mere = "rien"
	# céation de la fenetre
        self.fenetre = Tk()
        # Cacher la barre de menu
        self.fenetre.overrideredirect(1)
        # Booleen fermer : devient  true quand on appuie sur le bouton deconnexion
        self.fermer = False
        self.OuvrirQT = False
        self.QTdemarrer = False
        # Dimension et position fenetre
        self.hauteur = self.fenetre.winfo_screenheight()/1.4 # 70% de la page en hauteur
        self.largeur = self.fenetre.winfo_screenwidth()/13;  # 10% de la page en largeur

        self.posX = self.fenetre.winfo_screenwidth() - (self.largeur - 5) # collé à droite de la page
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

        # Chemin Images
        # Chemin des images pour créer executable
        deco = self.resource_path("Images\\quit.png")
        fleche = self.resource_path("Images\\quicktask.png")
        graphe = self.resource_path("Images\\stats.png")
        loupe = self.resource_path("Images\\browse.png")
        plus = self.resource_path("Images\\add.png")

        # Chemin en phase de test
        deco2 = "quit.png"
        fleche2 = "quicktask.png"
        graphe2 = "stats.png"
        loupe2 = "browse.png"
        plus2 = "add.png"

        # Chemin en phase de test
        deco3 = "..\\Images\\quit.png"
        fleche3 = "..\\Images\\quicktask.png"
        graphe3 = "..\\Images\\stats.png"
        loupe3 = "..\\Images\\browse.png"
        plus3 = "..\\Images\\add.png"

################################################################################################################
        try:
            image = Image.open(fleche)
        except Exception:
            image = Image.open(flech2)
            
        photo = ImageTk.PhotoImage(image)
        self.bouton_tache_rapide = Button(self.fenetre, image=photo,width=self.largeurBoutons,height=self.hauteurBoutons, command=self.open_taches_rapides)
        self.bouton_tache_rapide.grid(row=3,column=1, padx = self.largeur * 0.02)
        self.bouton_tache_rapide.image = photo
        self.bouton_tache_rapide.bind("<Leave>", self.leaveButton)
################################################################################################################
	# Bouton Nouveau Projet
        try:
            image = Image.open(plus)
        except Exception:
            image = Image.open(plus2)


        photo = ImageTk.PhotoImage(image)
        self.bouton_add = Button(self.fenetre, image=photo,width=self.largeurBoutons,height=self.hauteurBoutons, command=self.open_nouveau_projet)
        self.bouton_add.grid(row=4,column=1)
        self.bouton_add.image = photo
        self.bouton_add.bind("<Leave>", self.leaveButton)
################################################################################################################
	# Bouton Rapports
        try:
            image = Image.open(graphe)
        except Exception:
            image = Image.open(graphe2)


        photo = ImageTk.PhotoImage(image)
        self.bouton_stats = Button(self.fenetre, image=photo,width=self.largeurBoutons,height=self.hauteurBoutons, command=self.open_rapports)
        self.bouton_stats.grid(row=5,column=1)
        self.bouton_stats.image = photo
        self.bouton_stats.bind("<Leave>", self.leaveButton)
################################################################################################################
	# Bouton Naviguer
        try:
            image = Image.open(loupe)
        except Exception:
            image = Image.open(loupe2)
            
        photo = ImageTk.PhotoImage(image)
        self.bouton_naviguer = Button(self.fenetre, image=photo,width=self.largeurBoutons,height=self.hauteurBoutons, command=self.naviguer)
        self.bouton_naviguer.grid(row=6,column=1)
        self.bouton_naviguer.image = photo
        self.bouton_naviguer.bind("<Leave>", self.leaveButton)
################################################################################################################
	# Bouton Deconnexion
        try:
            image = Image.open(deco)
        except Exception:
            image = Image.open(deco2)

            
        photo = ImageTk.PhotoImage(image)
        self.bouton_deconnexion = Button(self.fenetre, image=photo,width=self.largeurBoutons,height=self.hauteurBoutons, command=self.deconnexion)
        self.bouton_deconnexion.grid(row=7,column=1)
        self.bouton_deconnexion.image = photo
        self.bouton_deconnexion.bind("<Leave>", self.leaveButton)
        self.bouton_deconnexion.bind("<ButtonPress>", self.QuitButton)
################################################################################################################
        # si fermeture de la fenetre autrement que par le bouton deconexion
        self.fenetre.protocol("WM_DELETE_WINDOW", self.IntercepteFermeture)

        self.fenetre.focus_set()
        # Quand la fenetre passe de l'état iconic à normal, elle appel la fonction iconification qui supprime ses contours
        self.fenetre.bind("<Map>", self.iconification)
        # Quand on quitte la fenetre
        self.fenetre.bind("<Leave>", self.Leave)
        self.fenetre.bind("<Enter>", self.Enter)
        # attribut permettant de savoir si la fenetre tache rapide est deja ouverte
        self.q = object
        
        self.fermetureQT() # instanciation de la fenetre Quicktask et réinstanciation lors de sa fermetur

        self.cpt1 = 0
        self.cpt2 = 0
        
    ### Fonctions liées aux Boutons ###  
    def deconnexion(self):
        """L'utilisateur veut fermer le programme et se deconnecter"""
        self.callback()
        if self.fermer == True:
            self.fenetre.destroy()
     
    def open_taches_rapides(self):
        """L'utilisateur veut ouvrir la fenetre des taches rapides"""
        self.fenetre.bind("<Leave>", self.LeaveQT)
        if self.bouton_tache_rapide["bg"] == "green":
            if self.q.fenetre.state() == "iconic":
                self.q.fenetre.state("normal")
            else:
                self.q.fenetre.state("iconic")
                self.fenetre.bind("<Leave>", self.Leave)
        else:
            if self.q.fenetre.state() == "withdrawn":
                self.q.fenetre.state("normal")
                self.bouton_tache_rapide.configure(bg="grey")
                self.bouton_tache_rapide.configure(relief = "sunken")
            else:
                self.q.fenetre.state("withdraw")
                self.bouton_tache_rapide.configure(bg="SystemButtonFace")
                self.bouton_tache_rapide.configure(relief = "raised")
                self.fenetre.bind("<Leave>", self.Leave)
    
    def open_nouveau_projet(self):
        """L'utilisateur veut ouvrir la fenetre des nouveaux projets"""
        # TODO : ouvrir la fenetre des nouveaux projets

    def open_rapports(self):
        """L'utilisateur veut ouvrir la fenetre des rapports"""
        # TODO : ouvrir la fenetre des rapports

    def naviguer(self):
        """L'utilisateur veut ouvrir la fenetre des rapports"""
        # TODO : ouvrir la fenetre de navigation
        self.fenetre.overrideredirect(0)
        self.fenetre.state('iconic')

    ### convertir la chaine du paramentre de geometry( en liste de parametre entier ###
    def geoliste(self, g):
        r=[i for i in range(0,len(g)) if not g[i].isdigit()]
        return [int(g[0:r[0]]),int(g[r[0]+1:r[1]]),int(g[r[1]+1:r[2]]),int(g[r[2]+1:])]

    ### Intercepter la fermeture d'un fenetre lorsqu'on ferme la fenetre autrement qu'avec le bouton quitter ###
    def IntercepteFermeture(self):
        self.fermer = True
        self.fenetre.destroy()

    ### Demande de confirmation après avoir appuyer sur le bouton Deconnexion   
    def callback(self):
        self.fermer = askyesno('Deconnexion', 'Êtes-vous sûr de vouloir vous deconnecter ?')

    ### Définition du chemin des images afin de pouvoir créer un executable avec pyinstaller
    def resource_path(self, relative_path):
        """ Get absolute path to resource, works for dev and for PyInstaller """
    #    try:
            # PyInstaller creates a temp folder and stores path in _MEIPASS
    #        base_path = sys._MEIPASS
    #   except Exception:
        base_path = os.path.abspath(".")

        return os.path.join(base_path, relative_path)
    def iconification(self, event):
        if not self.fenetre.state() == 'iconic':
            self.fenetre.overrideredirect(1)
    def intercepteFermeture(self):
        self.q.fermer = True
        self.q.fenetre.destroy()
        print("quicktask.fermer= ",self.q.fermer)
        self.bouton_tache_rapide.configure(bg="SystemButtonFace")
        self.bouton_tache_rapide.configure(relief = "raised")
        self.fermetureQT()
    def fermetureQT(self):
        self.q = QT(mother=self.fenetre)
        self.q.fenetre.withdraw()
        self.q.fenetre.bind("<Unmap>", self.reduce)
        self.q.fenetre.protocol("WM_DELETE_WINDOW", self.intercepteFermeture)
        self.q.start_stop.bind('<ButtonPress>', self.QT_start)
        self.q.QTdemarrer = False
        self.q.cancel.bind('<ButtonPress>', self.QT_cancel)
        self.fenetre.bind("<Leave>", self.Leave)
        
        
    def QT_start(self,args):
        if self.q.QTdemarrer == False:
            self.bouton_tache_rapide.configure(bg="green")
            self.q.QTdemarrer = True
        else:
            self.bouton_tache_rapide.configure(bg="grey")
            self.bouton_tache_rapide.configure(relief = "sunken")
    def QT_cancel(self,args):
        self.q.QTdemarrer = False
        self.bouton_tache_rapide.configure(bg="grey")
        self.bouton_tache_rapide.configure(relief = "sunken")
    def Leave(self,args):
        print(" leave")
        self.cpt1 += 1
        time.sleep(0.2)
        print("cpt1 = ", self.cpt1)
        print("cpt2 = ", self.cpt2)
        
        if self.cpt1 > self.cpt2:
             self.fenetre.overrideredirect(0)
             self.fenetre.state("iconic")
             self.cpt1 = 0
             self.cpt2 = 0
    def Enter(self, args):
        self.fenetre.overrideredirect(1)
        self.fenetre.state("normal")
        self.cpt1 = 0
        self.cpt2 = 0
            
    def leaveButton(self,args):
        self.cpt2 += 1
        print(" leave button")
    def LeaveQT(self,args):
        print("ne rien faire")

    def reduce(self,args):
        print("cacaaaaaaaaaaaaaaaaaaaaaaaaa")
        self.fenetre.bind("<Leave>", self.Leave)
    def QuitButton(self,args):
        self.cpt1 = -1
        
       
            
        
            
    
#b = BarreOutils()
#b.fenetre.mainloop()


