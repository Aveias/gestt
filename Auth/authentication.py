# -*-coding:utf8 -*
"""
Module permettant d'authentifier un utilisateur
Permet son accès au logiciel ou non
"""

import DB.dbLink as dbo
from getpass import getpass
import hashlib
import mysql.connector as mariadb

class Auth():
    """Classe permettant l'authentification des utilisateurs"""
    access = False

    def __init__(self, inputid,inputmdp):
        #TODO : Récupérer les identifiants depuis un form dans une interface graphique

        self.input_id = inputid
        self.input_psswd = inputmdp
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
                print("Accès autorisé")
            else:
                print("Accès refusé : Le mot de passe est incorrect")
        else:
            print("Accès refusé : cet utilisateur n'existe pas")

        return Auth.access
