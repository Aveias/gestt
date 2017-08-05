# -*-coding:utf8 -*
"""Affichage de la fenêtre de login"""
from __future__ import unicode_literals
import sys
import os
DOSSIER_COURRANT = os.path.dirname(os.path.abspath(__file__))
DOSSIER_PARENT = os.path.dirname(DOSSIER_COURRANT)
sys.path.append(DOSSIER_PARENT)
from tkinter import *
import Auth.authentification as auth
from PIL import Image,ImageTk

class Login():
    """Classe gérant l'affichage de la fenêtre de login"""


    def __init__(self):

        self.fenetre = Tk()
        
        self.fenetre.title('login')
        try:
            self.fenetre.iconbitmap("..\\icon.ico")
        except Exception:
            self.fenetre.iconbitmap("icon.ico")
        
        # Création de nos widgets
        self.message = Label(self.fenetre, text="Merci de vous identifier")
        self.message.pack()

        self.identifiant = str()
        self.input_id = Entry(self.fenetre, textvariable=self.identifiant, width=30)
        self.input_id.pack()

        self.mdp = str()
        self.input_mdp = Entry(self.fenetre, textvariable=self.mdp, width=30, show="*")
        self.input_mdp.pack()

        self.bouton_login = Button(self.fenetre, text="Log in", command=self.login)
        self.bouton_login.pack()



    def login(self):

        """L'utilisateur veut s'identifier
        On appelle la classe d'authentification"""
        grant = auth.Auth(self.input_id.get(), self.input_mdp.get())

        if auth.Auth.access == True:
            self.fenetre.destroy()

