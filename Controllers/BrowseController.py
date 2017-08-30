# -*-coding:utf8 -*
"""Controleur pour la fenêtre de navigation"""

import sys
import os
from tkinter.messagebox import *
DOSSIER_COURRANT = os.path.dirname(os.path.abspath(__file__))
DOSSIER_PARENT = os.path.dirname(DOSSIER_COURRANT)
sys.path.append(DOSSIER_PARENT)
from Controllers.Functions import Functions
from DB.dbLink import DBLink as DB
from Projects.Model import Project
from Views.quickTask import QuickTask as QT


class BrowseController:
    """Classe contenant les fonctions de contrôle utiles à la fenêtre de navigation"""

    def __init__(self):
        self.link = DB()


    def get_projects_list(self):
        """Renvoie la liste des projets ouverts"""

        #Requete permettant d'obtenir la liste des ID des projets au statut "ouvert" (1)

        ##On prépare la liste des ID et la Requete
        proj_ids = list()

        query = "SELECT IDProj \
                FROM projet \
                WHERE IDStat = (SELECT IDStat \
                                FROM statut \
                                WHERE Statut LIKE('%uvert%'))"
        result = self.link.query(query, []).fetchall()
        for idproj in result:
            proj_ids.append(idproj[0])

        #Depuis cette liste, charger chaque projet dans une autre liste
        proj_list = list()
        for pid in proj_ids:
            proj_list.append(Project(pid))

        return proj_list

    def get_projects_search_results(self, search_query):
        """Renvoie la liste des projets correspondant à une recherche"""
        ##On prépare la liste des ID et la Requete
        proj_ids = list()

        query = "SELECT IDProj \
                FROM projet \
                WHERE Intitulé REGEXP %s \
                OR NumDossier REGEXP %s \
                AND IDStat = (SELECT IDStat \
                                FROM statut \
                                WHERE Statut LIKE('%uvert%')) "
        result = self.link.query(query, [search_query, search_query]).fetchall()
        for idproj in result:
            proj_ids.append(idproj[0])

        #Depuis cette liste, charger chaque projet dans une autre liste
        proj_list = list()
        for pid in proj_ids:
            proj_list.append(Project(pid))

        return proj_list

    #def launch_quick_task(self, proj):
    #    if QT.activate is True:
    #        if askyesno("switchtask", "Cette action va terminer et enregistrer la tâche actuellement en cours. Continuer ?"):
    #            QT.timer(QT)
    #            QT.timer(QT)
    #        else:
    #            pass
    #    else:
    #        QT.project.set(proj)
    #        QT.timer(QT)







############## TESTS #################
