# -*-coding:utf8 -*
"""Fonctions générales au logiciel"""

import sys
import os
DOSSIER_COURRANT = os.path.dirname(os.path.abspath(__file__))
DOSSIER_PARENT = os.path.dirname(DOSSIER_COURRANT)
sys.path.append(DOSSIER_PARENT)
from Auth.authentication import Auth as Auth
from Users.Model import User as User


class Functions:

    def __init__(self):

        #Initialisation AUTH POUR TESTS - A SUPPRIMER
        authy = Auth("test", "test")
        ############

        Functions.current_user = User(Auth.current_user_id)

###### TESTS ########
