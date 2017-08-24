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
from Views.browseView import BrowseView as BV


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
        # Booleen QTdemarrer : devient  true quand on appuie sur le bouton demarrer de la fenetre Quicktask
        self.QTdemarrer = False
        # Booleen barreReduite : devient  true quand la barre se reduit
        self.boolBarreReduite = False

        # Dimension et position fenetre
        self.hauteur = self.fenetre.winfo_screenheight()/1.4 # 70% de la page en hauteur
        self.largeur = self.fenetre.winfo_screenwidth()/13  # 10% de la page en largeur

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
            image = Image.open(fleche2)

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
        self.fenetre.protocol("WM_DELETE_WINDOW", self.intercepteFermetureBarre)

        self.fenetre.focus_set()
        # Quand la fenetre passe de l'état iconic à normal, elle appel la fonction iconification qui supprime ses contours
        self.fenetre.bind("<Map>", self.iconification)
        # Quand on quitte la fenetre
        self.fenetre.bind("<Leave>", self.Leave)
        self.fenetre.bind("<Enter>", self.Enter)
        # Object qui contiendra un objet de la classe QuickTask
        self.q = object
        # Object qui contiendra un objet Toplevel ( une fenetre secondaire )
        self.barreReduite = Toplevel(master=self.fenetre) # on instancie la fenetre
        self.barreReduite.attributes("-topmost",1, "-alpha", 0.01)
        self.barreReduite.state("withdraw")
        # Dimension et position fenetre
        self.hauteur2 = self.fenetre.winfo_screenheight()
        self.largeur2 = self.fenetre.winfo_screenwidth()/100
        self.posX2 = self.fenetre.winfo_screenwidth() - (self.largeur2 ) # collé à droite de la page
        self.barreReduite.geometry("%dx%d%+d%+d" % (self.largeur2,self.hauteur2,self.posX2,0))
        self.barreReduite.state("withdraw")   # et on la cache
        self.barreReduite.attributes("-topmost",1, "-alpha", 0.01) # l'attribut topmost fait passer la fenetre au premier plan, l'attribut -alpha la rends transparente
        # Associer l'evenement entrée de la souris dans la fenetre à la fonction EnterBarreReduite
        self.barreReduite.bind("<Enter>", self.EnterBarreReduite)

        self.fermetureQT() # instanciation de la fenetre Quicktask et réinstanciation lors de sa fermetur

        # Compteurs servants à determiner quand le curseur sort de la fenetre
        self.cpt1 = 0 # s'incrémente quand on sort des boutons ou de la fenetre
        self.cpt2 = 0 # s'incrémente quand on sort des boutons seulement

    ### Fonctions liées aux Boutons ###
    def deconnexion(self):
        """L'utilisateur veut fermer le programme et se deconnecter"""
        self.callback()
        if self.fermer == True:
            self.fenetre.destroy()
    ### Demande de confirmation après avoir appuyer sur le bouton Deconnexion
    def callback(self):
        self.fermer = askyesno('Deconnexion', 'Êtes-vous sûr de vouloir vous deconnecter ?')
    ### Cliquer sur le bouton taches rapides déclenche cette fonction qui ouvre la fenetre QuickTask
    def open_taches_rapides(self):
        """L'utilisateur veut ouvrir la fenetre des taches rapides"""
        if self.bouton_tache_rapide["bg"] == "green":                        # si le bouton taches rapides est de couleur verte ( il est de couleur verte quand on appuie sur le bouton démarrer de la fenetre Quicktask )
            if self.q.fenetre.state() == "iconic":                              # si la fenetre Quicktask est à l'état iconic ( fenetre réduite )
                self.q.fenetre.state("normal")                                      # la fenetre Quicktask passe à l'état normal ( fenetre ouverte )
            else:                                                               # sinon
                self.q.fenetre.state("iconic")                                      # la fenetre Quicktask passe à l'état iconic
                self.fenetre.bind("<Leave>", self.Leave)
        else:                                                                # sinon ( si le bouton tache rapide n'est pas de couleur verte )
            if self.q.fenetre.state() == "withdrawn":                           # si la fenetre QuickTask est à l'état withdrawn ( cachée, invisible )
                self.q.fenetre.state("normal")                                      # la fenetre Quicktask passe à l'état normal
                self.bouton_tache_rapide.configure(bg="grey")                       # le bouton tache rapide passe à la couleur gris foncé
                self.bouton_tache_rapide.configure(relief = "sunken")               # et son aspect devient appuyé  pour signifier à l'utilisateur que la fenetre tache rapide est ouverte
            else:                                                               # sinon
                self.q.fenetre.state("withdraw")                                    # l'état de Quicktask devient withdraw
                self.bouton_tache_rapide.configure(bg="SystemButtonFace")           # le bouton tache rapide redevient de couleur et d'aspect normaux
                self.bouton_tache_rapide.configure(relief = "raised")               # et on associe les widget de la fenetre barreOutils à la fonction Leave qui détermine quand le curseur de la souris sort de la fenetre
                self.fenetre.bind("<Leave>", self.Leave)
    ### Cliquer sur le bouton nouveau projet ouvre la fenetre des nouveaux projets
    def open_nouveau_projet(self):
        """L'utilisateur veut ouvrir la fenetre des nouveaux projets"""
        # TODO : ouvrir la fenetre des nouveaux projets
    ### Cliquer sur le bouton stats ouvre la fenetre des rapports
    def open_rapports(self):
        """L'utilisateur veut ouvrir la fenetre des rapports"""
        # TODO : ouvrir la fenetre des rapports
    ### cliquer sur le bouton naviguer ouvre la fenetre de navigation
    def naviguer(self):
        """L'utilisateur veut ouvrir la fenetre des rapports"""
        self.browse = BV(mother=self.fenetre)

    ### convertir la chaine du paramentre de geometry( en liste de parametre entier
    def geoliste(self, g):
        r=[i for i in range(0,len(g)) if not g[i].isdigit()]
        return [int(g[0:r[0]]),int(g[r[0]+1:r[1]]),int(g[r[1]+1:r[2]]),int(g[r[2]+1:])]

    ### Intercepter la fermeture de la fenetre barreOutil lorsqu'on la ferme autrement qu'avec le bouton quitter
    def intercepteFermetureBarre(self):
        self.fermer = True
        self.fenetre.destroy()

    ### Définition du chemin des images afin de pouvoir créer un executable avec pyinstaller
    def resource_path(self, relative_path):
        """ Get absolute path to resource, works for dev and for PyInstaller """
    #    try:
            # PyInstaller creates a temp folder and stores path in _MEIPASS
    #        base_path = sys._MEIPASS
    #   except Exception:
        base_path = os.path.abspath(".")

        return os.path.join(base_path, relative_path)
    ### Si l'état de la fenetre n'est pas iconic, on retire les bords et le cadre windows
    def iconification(self, event):
        if not self.fenetre.state() == 'iconic':
            self.fenetre.overrideredirect(1)
    ### Intercepte la fermeture de la fenetre Quicktask / lorsqu'on clique sur la croix de la fenetre Quicktask :
    def intercepteFermetureQT(self):
        self.q.fermer = True
        self.q.fenetre.destroy() # on ferme la fenetre
        #print("quicktask.fermer= ",self.q.fermer)
        self.bouton_tache_rapide.configure(bg="SystemButtonFace") # le bouton tache rapide redevient de couleur normal
        self.bouton_tache_rapide.configure(relief = "raised")       # et de relief normal
        self.fermetureQT()                                              # on appel la fonction fermetureQT
    ### Lors de la fermture de la fenetre QT :
    def fermetureQT(self):
        self.q = QT(mother=self.fenetre)        # On renouvelle l'objet de la classe Quicktask qui ouvre une fenetre Quicktask
        self.q.fenetre.withdraw()               # On cache la fentre
        self.q.fenetre.bind("<Unmap>", self.reduce) # On associe le fait de changer l'état de la fentre ( iconic) à la fonciton reduce
        self.q.fenetre.protocol("WM_DELETE_WINDOW", self.intercepteFermetureQT) # On associe intercepte la fermeture de la fenetre Quicktask
        self.q.start_stop.bind('<ButtonPress>', self.QT_start) # On associe le fait de presser le bouton démarrer à la fonction QT_start
        self.q.QTdemarrer = False
        self.q.cancel.bind('<ButtonPress>', self.QT_cancel) # On associe le fait de presser le bouton annuler à la fonction QT_cancel
        self.fenetre.bind("<Leave>", self.Leave) # On associe le fait de sortir avec le curseur de la souris de la fenetre à la fonction Leave

    ### Lors de l'appuie sur le bouton demarrer de la fenetre Quicktask
    def QT_start(self,args):
        if self.q.QTdemarrer == False:
            self.bouton_tache_rapide.configure(bg="green")
            self.q.QTdemarrer = True
        else:
            self.bouton_tache_rapide.configure(bg="grey")
            self.bouton_tache_rapide.configure(relief = "sunken")
    ### Lors de l'appuie sur le bouton annuler de la fenetre Quicktask
    def QT_cancel(self,args):
        self.q.QTdemarrer = False
        self.bouton_tache_rapide.configure(bg="grey")
        self.bouton_tache_rapide.configure(relief = "sunken")
    ### Lorsque le curseur de la souris sors de la fenetre
    def Leave(self,args):
        print(" leave")
        if self.q.fenetre.state() == "normal":
            self.cpt1 -= 1
        self.cpt1 += 1
        print("cpt1 = ", self.cpt1)
        print("cpt2 = ", self.cpt2)

        if self.cpt1 > self.cpt2:
            i = 1
            while i >= 0.02: # Disparition de la barre en dégradé
                i = i - 0.01
                self.fenetre.attributes("-alpha", i)
                time.sleep(0.005)
            self.fenetre.attributes("-alpha", 0)
            self.fenetre.overrideredirect(0)
            self.fenetre.state("iconic")
            self.fenetre.attributes("-alpha", 1)
            if self.boolBarreReduite == False:
                 self.barreReduite.state("normal")
                 self.cpt1 = 0
                 self.cpt2 = 0
                 self.boolBarreReduite = True

    ### lorsque le curseur de la souris rentre dans la fenetre
    def Enter(self, args):
        self.fenetre.overrideredirect(1)
        self.fenetre.state("normal")
        self.cpt1 = 0
        self.cpt2 = 0
    ### lorsque le curseur de la souris sors d'un bouton
    def leaveButton(self,args):
        self.cpt2 += 1
        print(" leave button")

    ### Lorsque l'on réduit la fentre
    def reduce(self,args):
        self.fenetre.bind("<Leave>", self.Leave)
    ### Lorsque l'on appuie sur le bouton Quit de la barre d'outils
    def QuitButton(self,args):
        self.cpt1 = -1
    ### Lorsque le curseur de la souris entre dans la barre réduite
    def EnterBarreReduite(self, args):
        time.sleep(0.2)
        self.fenetre.state("normal")
        self.barreReduite.withdraw()
        self.boolBarreReduite = False



#b = BarreOutils()
#b.fenetre.mainloop()
