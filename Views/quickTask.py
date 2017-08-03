# -*-coding:utf8 -*
"""Fenêtre de rapide : Vue"""
#TODO: Rajouter une checkbox pour ajout d'une entrée de temps manuel (sans chrono)


from __future__ import unicode_literals
import sys
import os
from tkinter import *
from datetime import datetime, timedelta
DOSSIER_COURRANT = os.path.dirname(os.path.abspath(__file__))
DOSSIER_PARENT = os.path.dirname(DOSSIER_COURRANT)
sys.path.append(DOSSIER_PARENT)
from DB.dbLink import DBLink as db



class QuickTask:
    """Fenêtre d'ajout rapide de tâche"""

    def __init__(self, project_name='Sélectionner...', activate=False):
        #Initialisation des variables
        QuickTask.activate = activate
        link = db() #On aura besoin de la BDD pour récupérer projets et types

        QuickTask.fenetre = Tk()
        QuickTask.fenetre.title("Tâche rapide")

        ###Titre
        Label(QuickTask.fenetre, text="Ajout d'une tâche").pack()
        self.msg = Label(QuickTask.fenetre, text='')
        self.msg.pack()

        ###Champ de projet
        Label(QuickTask.fenetre, text="Nom du projet :").pack()
        # Create a Tkinter variable
        QuickTask.project = StringVar(QuickTask.fenetre)
        proj_choices = dict()
        #Récupération des types et insertion comme options
        projects = link.query("SELECT IDProj, Intitulé FROM projet ", [])
        for pro_id, pro_nom in projects:
            proj_choices[pro_nom] = pro_id

        QuickTask.project.set(project_name) # set the default option
        OptionMenu(QuickTask.fenetre, QuickTask.project, *proj_choices).pack()

        ###Champ de type
        # Create a Tkinter variable
        QuickTask.type_value = StringVar(QuickTask.fenetre)
        choices = dict()
        #Récupération des types et insertion comme options
        types = link.query("SELECT * FROM type ", [])
        for ty_id, ty_nom in types:
            choices[ty_nom] = ty_id

        QuickTask.type_value.set("Sélectionner...") # set the default option
        Label(QuickTask.fenetre, text="Type de tâche :").pack()
        OptionMenu(QuickTask.fenetre, QuickTask.type_value, *choices).pack()

        ###Champ de description
        Label(QuickTask.fenetre, text="Description :").pack()
        QuickTask.input_desc = Entry(QuickTask.fenetre)
        QuickTask.input_desc.pack()

        ###Minutes de décalage pour le bouton démarrer/arrêter
        Label(QuickTask.fenetre, text="Décalage : ").pack()
        self.min_label = Label(QuickTask.fenetre, text="Tâche commencée il y a ")
        self.min_label.pack()
        QuickTask.input_min = Entry(QuickTask.fenetre)
        QuickTask.input_min.insert(0, 0)
        QuickTask.input_min.pack()
        Label(QuickTask.fenetre, text="minute(s)").pack()

        ###Champs heures de début/fin
        Label(QuickTask.fenetre, text="Heure de début : ").pack()
        QuickTask.heure_debut = Entry(QuickTask.fenetre, state=DISABLED)
        QuickTask.heure_debut.pack()

        Label(QuickTask.fenetre, text="Heure de fin : ").pack()
        QuickTask.heure_fin = Entry(QuickTask.fenetre, state=DISABLED)
        QuickTask.heure_fin.pack()

        ###Bouton démarrer/arrêter
        QuickTask.start_stop = Button(QuickTask.fenetre, text="Démarrer", command=self.timer)
        QuickTask.start_stop.pack()

        #Bouton annuler
        QuickTask.cancel = Button(QuickTask.fenetre, command=self.stop, text="Annuler", state=DISABLED)
        QuickTask.cancel.pack()

    def timer(self):
        """Actions à engager lorsqu'on débute/arrête une tâche"""

        #Prise en compte du décalage de temps et remise à zéro du compteur
        decalage = int(QuickTask.input_min.get())

        #Action à déclencher en fonction de si on démarre ou finit l'enregistrement
        if not QuickTask.activate: #Si on démarre l'enregistrement
            #Gestion de l'heure de départ
            QuickTask.start_time = datetime.now() - timedelta(minutes=decalage)
            QuickTask.heure_debut['state'] = NORMAL
            QuickTask.heure_debut.insert(0, QuickTask.start_time.strftime('%H:%M'))
            QuickTask.heure_debut['state'] = DISABLED
            #Modification des labels
            QuickTask.start_stop['text'] = "Terminer"
            self.min_label['text'] = "Tâche terminée il y a "
            #On change le statut du bouton et on active l'annulation
            QuickTask.activate = not QuickTask.activate
            QuickTask.cancel['state'] = NORMAL

        else: #Si on le finit
            #Vérifions que les champs sont bien remplis
            if QuickTask.project.get() != 'Sélectionner...' \
            and QuickTask.type_value.get() != 'Sélectionner...' \
            and QuickTask.input_desc.get() != '':
            #Oui ? ok on va pour enregistrer
                QuickTask.end_time = datetime.now() - timedelta(minutes=decalage)
                QuickTask.start_stop['text'] = "Démarrer"
                self.min_label['text'] = "Tâche commencée il y a "
                #TODO: appel à la fonction controleur enregistrant la tâche en BDD
                #On change le statut du bouton et on vide les champs
                QuickTask.activate = not QuickTask.activate
                QuickTask.heure_debut['state'] = NORMAL
                QuickTask.heure_debut.delete(0, 'end')
                QuickTask.heure_debut['state'] = DISABLED

                #Désactivation du bouton annuler et vidage de champs
                QuickTask.cancel['state'] = DISABLED
                QuickTask.input_desc.delete(0, 'end')

                #On affiche un message disant OK
                self.msg['text'] = "Tâche enregistrée"

            else:
            #non ? on affiche un message et on valide rien du tout, namého
                self.msg['text'] = "Tous les champs doivent êtres remplis pour enregistrer la tâche"

    def stop(self):
        """Annulation d'une tâche démarrée"""

        #Gestion des labels
        QuickTask.start_stop['text'] = "Démarrer"
        self.min_label['text'] = "Tâche commencée il y a "
        #On change le statut du bouton et on vide les champs
        QuickTask.activate = not QuickTask.activate
        QuickTask.heure_debut['state'] = NORMAL
        QuickTask.heure_debut.delete(0, 'end')
        QuickTask.heure_debut['state'] = DISABLED
        #Désactivation du bouton annuler
        QuickTask.cancel['state'] = DISABLED

        #AFfichage du message
        self.msg['text'] = "Enregistrement de la tâche annulé"







#Test de la fenêtre
fen = QuickTask()
fen.fenetre.mainloop()
