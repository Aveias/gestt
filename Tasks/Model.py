import DB.dbLink as db

class Task:
    """Modèle tache. Contient une tache."""

    def __init__(self, tache_id='', heure_debut='', heure_fin='', commentaire='', id_util='', id_proj='', desc='', date='', id_type=''):
        """Constructeur initialisant l'entrée de temps à partir de son ID"""

        #On load la tache depuis la BDD si demandée avec un ID
        if tache_id != '':
            self._id_tache = tache_id
            #On va chercher la tâche en base de données
            link = db.DBLink()
            query = "SELECT t.HeureDebut, t.HeureFin, t.Commentaire, t.IDUtil, t.IDDate, t.IDProj, t.IDDesc, da.LaDate, de.Libellé, ty.Libellé, ty.IDType \
                    FROM tache AS t \
                    JOIN dates AS da ON t.IDDate = da.IDDate \
                    JOIN description AS de ON t.IDDesc = de.IDDesc \
                    JOIN type AS ty ON de.IDType = ty.IDType \
                    WHERE IDTach = %s"
            result = link.query(query, [self._id_tache, ])

            #On hydrate l'objet à partir des éléments récupérés en BDD
            for HeureDebut, HeureFin, Commentaire, IDUtil, IDDate, IDProj, IDDesc, bdddate, bdddesc, typ, idtyp in result:
                self.heure_debut = HeureDebut
                self.heure_fin = HeureFin
                self.commentaire = Commentaire
                self.id_util = IDUtil
                self.id_date = IDDate
                self.id_proj = IDProj
                self.id_desc = IDDesc
                self.date = bdddate
                self.description = bdddesc
                self.type = typ
                self.id_type = idtyp

        #Sinon, on hydrate à partir des champs renseignés en paramètre
        else:
            self.heure_debut = heure_debut
            self.heure_fin = heure_fin
            self.commentaire = commentaire
            self.id_util = id_util
            self.date = date
            self.id_proj = id_proj
            self.description = desc
            self.id_type = id_type
            self.type = self.get_type()

    def registerDescription(self):
        """Enregistrement de la description en BDD"""
        link = db.DBLink()

        query = "SELECT IDDesc \
                FROM description \
                WHERE Libellé = %s AND IDType = %s"
        result = link.query(query, [self.description, self.id_type, ])
        if result.with_rows:
            #Si la description existe en BDD on recupère l'ID
            for IDDesc, in result:
                self.id_desc = IDDesc
        else:
            #Sinon on l'enregistre
            query = "INSERT INTO description \
                    (Libellé, IDType) \
                    VALUES (%s, %s)"
            result = link.commit(query, [self.description, self.id_type])

            #Récupération de l'ID ainsi créé
            self.id_desc = result.lastrowid

    def registerDate(self):
        """Enregistrement de la date en BDD"""
        link = db.DBLink()

        #On vérifie si la date existe
        query = "SELECT IDDate \
                FROM dates \
                WHERE LaDate = %s "
        result = link.query(query, [self.date, ])

        #Si oui, on récupère son ID
        if result.with_rows:
            for IDDate, in result:
                self.id_date = IDDate
        else:
            #Sinon, on enregistre en BDD
            query = "INSERT INTO dates \
                    (LaDate) \
                    VALUES (%s)"
            result = link.commit(query, [self.date, ])

            #Récupération de l'ID
            self.id_date = result.lastrowid


    def register(self):
        """Enregistrement d'une tache en BDD"""
        link = db.DBLink()


        #Gestion des données de date et description
        self.registerDate()
        self.registerDescription()

        #Pis on insère la tâche
        query = "INSERT INTO tache \
                ( HeureDebut, HeureFin, Commentaire, IDUtil, IDDate, IDProj, IDDesc) \
                VALUES (%s, %s, %s, %s, %s, %s, %s)"
        result = link.commit(query, [self.heure_debut, self.heure_fin, self.commentaire, self.id_util, self.id_date, self.id_proj, self.id_desc])


        #Chargement de l'ID ainsi créé
        self._id_tache = result.lastrowid


    def update(self):
        """Mise à jour de la tache"""
        link = db.DBLink()

        #On met à jour les ID de date et description si besoin
        self.registerDate()
        self.registerDescription()

        #pis la tâche
        query = "UPDATE tache \
                SET HeureDebut = %s, HeureFin = %s, Commentaire = %s, IDUtil = %s, IDDate = %s, IDProj = %s, IDDesc = %s \
                WHERE IDTach = %s"
        link.commit(query, [self.heure_debut, self.heure_fin, self.commentaire, self.id_util, self.id_date, self.id_proj, self.id_desc, self._id_tache])

    def delete(self):
        """supprimer l'utilisateur"""
        link = db.DBLink()

        query = "DELETE \
                FROM tache \
                WHERE IDTach = %s"
        link.commit(query, [self._id_tache, ])

    def get_type(self):
        """Récupère la date à partir de l'ID"""
        link = db.DBLink()

        query = "SELECT Libellé \
                FROM type \
                WHERE IDType = %s"
        result = link.query(query, [self.id_type])

        for le_type, in result:
            return le_type
