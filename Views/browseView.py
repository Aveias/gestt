# -*-coding:utf8 -*
"""Fenêtre de navigation"""

from tkinter import *
from tkinter.ttk import *
import sys
import os
DOSSIER_COURRANT = os.path.dirname(os.path.abspath(__file__))
DOSSIER_PARENT = os.path.dirname(DOSSIER_COURRANT)
sys.path.append(DOSSIER_PARENT)
from Controllers.BrowseController import BrowseController
from Users.Model import User

class BrowseView:

    def __init__(self, mother):

        self.ctrl = BrowseController()
        self.search_input = ""

        #On lance la fenêtre par rapport à la fenêtre mère
        BrowseView.root = Toplevel(mother)
        BrowseView.root.title("Naviguer")

        #Initialisation des variables
        #self.mother = mother

        tabs = Notebook(BrowseView.root, name="projets")

        #Création des onglets
        ##Projets
        pr_tab = Frame(tabs)

        #recherche
        search_frame = Frame(pr_tab)
        self.search_input = Entry(search_frame)
        self.search_input.pack(side=LEFT)
        Button(search_frame, text="Rechercher", command=self.search).pack(side=RIGHT)
        search_frame.pack()

        ###Treeview listant les projets
        Label(pr_tab, text="Liste des projets").pack()
        ####Headers
        self.pr_list = Treeview(pr_tab, selectmode="browse", show="headings", columns=("nom", "chef", "client", "num"))
        self.pr_list.heading("nom", text="Nom")
        self.pr_list.heading("chef", text="Chef de projet")
        self.pr_list.heading("client", text="client")
        self.pr_list.heading("num", text="N° dossier")
        ####Insertion du contenu
        projects = self.ctrl.get_projects_list()
        for proj in projects:
            cdp = User(proj.responsable)
            self.pr_list.insert("", 1, values=(proj.nom, (cdp.nom, cdp.prenom),
                                          proj.client, proj.num_dossier))

        self.pr_list.pack()

        Button(pr_tab, text="Voir le projet").pack()
        Button(pr_tab, text="Démarrer une tâche rapide pour ce projet").pack()


        ##Tâches
        ta_tab = Frame(tabs)

        #Ajout des onglets au notebook et affichage
        tabs.add(pr_tab, text="Projets")
        tabs.add(ta_tab, text="Tâches")

        tabs.pack()

    def search(self):
        #on récupère les résultats
        projects = self.ctrl.get_projects_search_results(self.search_input.get())
        #on vide l'arbre
        self.pr_list.delete(*self.pr_list.get_children())
        #on le rerempli avec les résultats
        for proj in projects:
            cdp = User(proj.responsable)
            self.pr_list.insert("", 1, values=(proj.nom, (cdp.nom, cdp.prenom),
                                          proj.client, proj.num_dossier))


#test
