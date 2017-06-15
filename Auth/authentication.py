# -*-coding:Latin-1 -*
"""
Module permettant d'authentifier un utilisateur
Permet son acc�s au logiciel ou non
"""

import DB.dbLink as dbo
from getpass import getpass
import hashlib
import mysql.connector as mariadb

class Auth():
    """Classe permettant l'authentification des utilisateurs"""
    access = False

    def __init__(self, inputid,inputmdp):
        #TODO : R�cup�rer les identifiants depuis un form dans une interface graphique
        self.input_id = inputid
        self.input_psswd = inputmdp
        self.input_psswd = hashlib.md5(self.input_psswd.encode())
        self.grantAccess()

    def grantAccess(self):
        """Authentification de l'utilisateur """
        #On d�finit les champs � r�cup�rer en BDD comme vides
        user_iD = None
        user_psswd = None

        #On va r�cup�rer les infos en BDD
        quer = "SELECT Nom FROM utilisateur"
        link = dbo.DBLink()
        result = link.query("SELECT Nom, MdP FROM utilisateur WHERE Identifiant = %s", [self.input_id, ])

        for Nom, MdP in result:
            user_iD = Nom
            user_psswd = MdP

        #Si l'user ID a �t� trouv�
        #On compare le mot de passe entr� � celui r�cup�r� en BDD, si �a matche, on renvoie True
        if user_iD != None:
            if self.input_psswd.hexdigest() == user_psswd:
                Auth.access = True
                print("Acc�s autoris�")
            print("Acc�s refus�")
        else:
            print("Acc�s refus�")

        return Auth.access
