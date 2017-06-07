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

#TODO : Récupérer les identifiants depuis un form dans une interface graphique
input_id = input("Entrer votre identifiant : ")
input_psswd = getpass("Entrer votre mot de passe : ")
input_psswd = hashlib.md5(input_psswd.encode())

#On définit les champs à récupérer en BDD comme vides
user_iD = None
user_psswd = None

#On va récupérer les infos en BDD
quer = "SELECT Nom FROM utilisateur"
link = dbo.DBLink()
result = link.query("SELECT Nom, MdP FROM utilisateur WHERE Identifiant = %s", [input_id, ])

for Nom, MdP in result:
    user_iD = Nom
    user_psswd = MdP

#Si l'user ID a été trouvé
#On compare le mot de passe entré à celui récupéré en BDD
#TODO : Définir l'autorisation de la connexion. Un fichier "auth" ? Une variable globale ?
if user_iD != None:
    if input_psswd.hexdigest() == user_psswd:
        print("Accès autorisé")
    else:
        print("Le mot de passe est invalide")
else:
    print("Cet utilisateur n'existe pas")

os.system("pause")
