# -*-coding:Latin-1 -*
"""Affichage de la fenêtre de login"""

from tkinter import *
import Auth.authentication as auth

class Login():
    """Classe gérant l'affichage de la fenêtre de login"""


    def __init__(self):

        self.fenetre = Tk()

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
