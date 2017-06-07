# -*-coding:Latin-1 -*
"""
Module permettant d'authentifier un utilisateur
Permet son acc�s au logiciel ou non
"""

import DB.dbLink as dbo
from getpass import getpass
import hashlib
import os
import mysql.connector as mariadb

#TODO : R�cup�rer les identifiants depuis un form dans une interface graphique
input_id = input("Entrer votre identifiant : ")
input_psswd = getpass("Entrer votre mot de passe : ")
input_psswd = hashlib.md5(input_psswd.encode())

#On d�finit les champs � r�cup�rer en BDD comme vides
user_iD = None
user_psswd = None

#On va r�cup�rer les infos en BDD
quer = "SELECT Nom FROM utilisateur"
link = dbo.DBLink()
result = link.query("SELECT Nom, MdP FROM utilisateur WHERE Identifiant = %s", [input_id, ])

for Nom, MdP in result:
    user_iD = Nom
    user_psswd = MdP

#Si l'user ID a �t� trouv�
#On compare le mot de passe entr� � celui r�cup�r� en BDD
#TODO : D�finir l'autorisation de la connexion. Un fichier "auth" ? Une variable globale ?
if user_iD != None:
    if input_psswd.hexdigest() == user_psswd:
        print("Acc�s autoris�")
    else:
        print("Le mot de passe est invalide")
else:
    print("Cet utilisateur n'existe pas")

os.system("pause")
