# -*-coding:utf8 -*
"""Controleur pour la gestion des tâches"""

import sys
import os
from tkinter import *
from datetime import datetime
DOSSIER_COURRANT = os.path.dirname(os.path.abspath(__file__))
DOSSIER_PARENT = os.path.dirname(DOSSIER_COURRANT)
sys.path.append(DOSSIER_PARENT)
from Auth.authentication import Auth
from Tasks.model import Task


class TasksController:
    """Controlleur gérant l'ajout de tâches"""

    def __init__(self):
        self.task = Task()

    def register(self, heured, heuref, comm, idpro, descr, idty,
                 day=datetime.now().strftime('%Y-%m-%d')):
        """Enregistre une tâche en base de données"""
        #Création de la tâche
        self.task = Task(heure_debut=heured, heure_fin=heuref, commentaire=comm,
                         id_util=Auth.current_user_id, id_proj=idpro, desc=descr, date=day,
                         id_type=idty)
        print(day)
        self.task.register()


    def get_list(self):
        pass


#Pour Test
Auth.current_user_id  = 1
