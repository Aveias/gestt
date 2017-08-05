# -*-coding:utf8 -*
"""Fenêtre de rapide : Vue"""
#TODO: Rajouter une checkbox pour ajout d'une entrée de temps manuel (sans chrono)
#TODO: Passer toutes les vérifications des champs dans le controleur


import sys
import os
from tkinter import *
from datetime import datetime, timedelta
DOSSIER_COURRANT = os.path.dirname(os.path.abspath(__file__))
DOSSIER_PARENT = os.path.dirname(DOSSIER_COURRANT)
sys.path.append(DOSSIER_PARENT)
from DB.dbLink import DBLink as db
from Controllers.TasksController import TasksController as TasksCont



class QuickTask:
    """Fenêtre d'ajout rapide de tâche"""

    def __init__(self, mother, project_name='Sélectionner...', activate=False):
        #Initialisation des variables
        QuickTask.activate = activate
        link = db() #On aura besoin de la BDD pour récupérer projets et types

        QuickTask.fenetre = Toplevel(mother)
        QuickTask.fenetre.title("Tâche rapide")

        ###Titre
        Label(QuickTask.fenetre, text="Ajout d'une tâche").pack()
        self.msg = Label(QuickTask.fenetre, text='')
        self.msg.pack()

        ###Champ de projet
        Label(QuickTask.fenetre, text="Nom du projet :").pack()
        # Create a Tkinter variable
        QuickTask.project = StringVar(QuickTask.fenetre)
        self.proj_choices = dict()
        #Récupération des types et insertion comme options
            # Attention : si deux projets ouverts ont le même intitulé,
            # seul le plus récent sera pris en compte
        projects = link.query("SELECT IDProj, Intitulé FROM projet WHERE IDStat = 1", []).fetchall()
        for elem in projects:
            self.proj_choices[elem[1]] = elem[0]

        QuickTask.project.set(project_name) # set the default option
        OptionMenu(QuickTask.fenetre, QuickTask.project, *self.proj_choices).pack()

        ###Champ de type
            # Create a Tkinter variable
        QuickTask.type_value = StringVar(QuickTask.fenetre)
        self.ty_choices = dict()
            #Récupération des types et insertion comme options
        types = link.query("SELECT * FROM type ", []).fetchall()
        for elem in types:
            self.ty_choices[elem[1]] = elem[0]

        QuickTask.type_value.set("Sélectionner...") # set the default option
        Label(QuickTask.fenetre, text="Type de tâche :").pack()
        OptionMenu(QuickTask.fenetre, QuickTask.type_value, *self.ty_choices).pack()

        ###Champ de description
        Label(QuickTask.fenetre, text="Description :").pack()
        QuickTask.input_desc = Entry(QuickTask.fenetre)
        QuickTask.input_desc.pack()

        ###Champ de commentaire
        Label(QuickTask.fenetre, text="Commentaire :").pack()
        QuickTask.input_comm = Text(QuickTask.fenetre, width=25, height=3)
        QuickTask.input_comm.pack()

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
            QuickTask.h_debut_value = datetime.now() - timedelta(minutes=decalage)
            QuickTask.heure_debut['state'] = NORMAL
            QuickTask.heure_debut.insert(0, QuickTask.h_debut_value.strftime('%H:%M'))
            QuickTask.heure_debut['state'] = DISABLED
            #Modification des labels
            QuickTask.start_stop['text'] = "Terminer"
            self.min_label['text'] = "Tâche terminée il y a "
            #On change le statut du bouton, on active l'annulation, on vide le champ décalage
            QuickTask.activate = not QuickTask.activate
            QuickTask.cancel['state'] = NORMAL
            QuickTask.input_min.delete(0, 'end')
            QuickTask.input_min.insert(0, 0)

        else: #Si on le finit
            #Vérifions que les champs sont bien remplis
            if QuickTask.project.get() != 'Sélectionner...' \
            and QuickTask.type_value.get() != 'Sélectionner...' \
            and QuickTask.input_desc.get() != '':
                #On gère l'heure de fin
                QuickTask.h_fin_value = datetime.now() - timedelta(minutes=decalage)
                #Et on vérifie que l'heure de début est inférieure à celle de fin
                ecart_temps =  QuickTask.h_fin_value - QuickTask.h_debut_value

                if QuickTask.h_fin_value > QuickTask.h_debut_value \
                and ecart_temps.seconds > 60:
                #tout est ok ?  on va enregistrer
                    #On modifie le champ d'heure de fin
                    QuickTask.heure_fin['state'] = NORMAL
                    QuickTask.heure_fin.insert(0, QuickTask.h_fin_value.strftime('%H:%M'))
                    QuickTask.heure_fin['state'] = DISABLED
                    #Et les labels
                    QuickTask.start_stop['text'] = "Démarrer"
                    self.min_label['text'] = "Tâche commencée il y a "
                    # appel à la fonction controleur enregistrant la tâche en BDD
                    controller = TasksCont()
                    controller.register(QuickTask.heure_debut.get(), QuickTask.heure_fin.get(),
                                        QuickTask.input_comm.get('1.0', 'end'),
                                        self.proj_choices[QuickTask.project.get()],
                                        QuickTask.input_desc.get(),
                                        self.ty_choices[QuickTask.type_value.get()])
                    #On change le statut du bouton et on vide les champs
                    QuickTask.activate = not QuickTask.activate
                    QuickTask.heure_debut['state'] = NORMAL
                    QuickTask.heure_debut.delete(0, 'end')
                    QuickTask.heure_debut['state'] = DISABLED
                    QuickTask.heure_fin['state'] = NORMAL
                    QuickTask.heure_fin.delete(0, 'end')
                    QuickTask.heure_fin['state'] = DISABLED
                    QuickTask.input_comm.delete('1.0', 'end')
                    QuickTask.input_min.delete(0, 'end')
                    QuickTask.input_min.insert(0, 0)

                    #Désactivation du bouton annuler et vidage de champs
                    QuickTask.cancel['state'] = DISABLED
                    QuickTask.input_desc.delete(0, 'end')

                    #On affiche un message disant OK
                    self.msg['text'] = "Tâche enregistrée"
                else:
                    self.msg['text'] = "L'heure de fin doit être supérieure ou égale à l'heure de début"

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
