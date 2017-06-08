# -*-coding:Latin-1 -*
"""
Module permettant d'authentifier un utilisateur
Permet son accès au logiciel ou non
"""

import DB.dbLink as dbo
from getpass import getpass
import hashlib
import os
import mysql.connector as mariadb

class Auth():
    """Classe permettant l'authentification des utilisateurs"""
    access = False

    def __init__(self):
        #TODO : Récupérer les identifiants depuis un form dans une interface graphique
        self.input_id = input("Entrer votre identifiant : ")
        self.input_psswd = getpass("Entrer votre mot de passe : ")
        self.input_psswd = hashlib.md5(self.input_psswd.encode())
        self.grantAccess()

    def grantAccess(self):
        """Authentification de l'utilisateur """
        #On définit les champs à récupérer en BDD comme vides
        user_iD = None
        user_psswd = None

        #On va récupérer les infos en BDD
        quer = "SELECT Nom FROM utilisateur"
        link = dbo.DBLink()
        result = link.query("SELECT Nom, MdP FROM utilisateur WHERE Identifiant = %s", [self.input_id, ])

        for Nom, MdP in result:
            user_iD = Nom
            user_psswd = MdP

        #Si l'user ID a été trouvé
        #On compare le mot de passe entré à celui récupéré en BDD, si ça matche, on renvoie True
        if user_iD != None:
            if self.input_psswd.hexdigest() == user_psswd:
                Auth.access = True

        return Auth.access
