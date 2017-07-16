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

        self.input_id = inputid
        self.input_psswd = inputmdp
        self.input_psswd = hashlib.md5(self.input_psswd.encode())
        self.grantAccess()

    def grantAccess(self):
        """Authentification de l'utilisateur """
        #On définit les champs à récupérer en BDD comme vides
        user_id = None
        user_psswd = None

        #On va récupérer les infos en BDD
        link = dbo.DBLink()
        result = link.query("SELECT IDUtil, Nom, MdP FROM utilisateur WHERE Identifiant = %s", [self.input_id, ])

        for id_user, nom, mdp in result:
            user_id = id_user
            user_id = nom
            user_psswd = mdp

        #Si l'user ID a été trouvé
        #On compare le mot de passe entré à celui récupéré en BDD, si ça matche, on renvoie True
        if user_id != None:
            if self.input_psswd.hexdigest() == user_psswd:
                Auth.access = True
                Auth.current_user_id = id_user
                print("Accès autorisé")
            else:
                print("Accès refusé : Le mot de passe est incorrect")
        else:
            print("Accès refusé : cet utilisateur n'existe pas")

        return Auth.access
