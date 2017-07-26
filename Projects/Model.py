# -*-coding:utf8 -*

import DB.dbLink as db

class Project:
    """Modèle projet. Contient un objet projet."""

    def __init__(self, proj_id='', nom='', description='', num_dossier='', budget=0, client=1, statut=1, responsable=1):
        """Constructeur initialisant le projet à partir de son ID"""

        #On load le projet depuis la BDD si demandé avec un ID
        if proj_id != '':
            self._id_proj = proj_id
            #On va chercher le projet en base de données
            link = db.DBLink()
            query = "SELECT p.Intitulé AS bdd_nom, p.Description AS bdd_description, p.NumDossier AS num_dossier, p.Budget AS budget, \
                            c.IDClie AS client, s.IDStat AS statut, p.IDUtil AS responsable \
                    FROM projet AS p \
                    JOIN client AS c ON p.IDClient = c.IDClie \
                    JOIN statut AS s ON p.IDStat = s.IDStat \
                    WHERE p.IDProj = %s"
            result = link.query(query, [self._id_proj, ])

            #On hydrate l'objet à partir des éléments récupérés en BDD
            for bdd_nom, bdd_description, bdd_num_dossier, bdd_budget, bdd_client, bdd_statut, bdd_responsable in result:
                self.nom = bdd_nom
                self.description = bdd_description
                self.num_dossier = bdd_num_dossier
                self.budget = bdd_budget
                self.client = bdd_client
                self.statut = bdd_statut
                self.responsable = bdd_responsable

        #Sinon, on hydrate à partir des champs renseignés en paramètre
        else:
            self.nom = nom
            self.description = description
            self.num_dossier = num_dossier
            self.budget = budget
            self.client = client
            self.statut = statut
            self.responsable = responsable

    def register(self):
        """Enregistrement d'un projet"""
        link = db.DBLink()

        # Vérifier si le projet existe
        # Si oui, récupérer son ID
        # Si non, le créer et récupérer son ID


        #Enregistrement des données
        query = "INSERT INTO projet \
                (Intitulé, Description, NumDossier, Budget, IDStat, IDClient, IDUtil) \
                VALUES (%s, %s, %s, %s, %s, %s, %s)"
        link.commit(query, [self.nom, self.description, self.num_dossier, self.budget, self.statut, self.client, self.responsable])
        #Chargement de l'id ainsi créé

        query = "SELECT IDProj \
                FROM projet \
                WHERE IDProj = (SELECT MAX(IDProj) \
                                FROM projet)"
        result = link.query(query, [])

        for id_proj, in result:
            self._id_proj = id_proj

    def update(self):
        """Mise à jour du projet"""
        link = db.DBLink()
        query = "UPDATE projet \
                SET Intitulé = %s, Description = %s, NumDossier = %s, Budget = %s, IDUtil = %s, IDClient = %s, IDStat = %s \
                WHERE IDProj = %s"
        link.commit(query, [self.nom, self.description, self.num_dossier, self.budget, self.responsable, self.client, self.statut, self._id_proj])

    def delete(self):
        """supprimer l'utilisateur"""
        link = db.DBLink()

        query = "DELETE \
                FROM projet \
                WHERE IDProj = %s"
        link.commit(query, [self._id_proj, ])
