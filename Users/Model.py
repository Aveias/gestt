# -*-coding:utf8 -*

import DB.dbLink as db

class User:
    """Modèle utilisateur. Contient un objet utilisateur"""

    def __init__(self, id='', nom='', prenom='', identifiant='', mdp='', cout='', idfonc='', fonction='', pole='', roles=dict()):
        """Constructeur initialisant utilisateur à partir d'un ID ou des données indiquées"""

        #On load l'user depuis la BDD si demandé avec un ID
        if id != '':
            self._id_table = id
            #On va chercher l'user en base de données
            link = db.DBLink()
            query = "SELECT u.IDUtil AS id_bdd, u.Nom AS nom, u.Prénom AS prenom, u.Identifiant AS identifiant, u.MdP AS mdp, u.SalaireBrut AS cout, u.IDFonc AS id_fonc, f.Intitulé AS fonction, p.Libelle AS pole \
                    FROM utilisateur AS u \
                    JOIN fonction AS f ON f.IDFonc = u.IDFonc \
                    JOIN pole AS p ON p.IDPole = p.IDPole \
                    WHERE u.IDUtil = %s"
            result = link.query(query, [self._id_table, ])

            #On hydrate l'objet à partir des éléments récupérés en BDD
            for id_bdd, nom, prenom, identifiant, mdp, cout, id_fonc, fonction, pole in result:
                self._id_table = id_bdd
                self.fonction = fonction
                self.pole = pole
                self.nom = nom
                self.prenom = prenom
                self.identifiant = identifiant
                self._mdp = mdp
                self.cout = cout
                self.id_fonc = id_fonc

            #Récupération de la liste des roles
            self.roles = dict()
            self.get_roles()

        #Sinon, on hydrate à partir des champs renseignés en paramètre
        else :
            self.id_fonc = idfonc
            self.fonction = fonction
            self.pole = pole
            self.nom = nom
            self.prenom = prenom
            self.identifiant = identifiant
            self._mdp = mdp
            self.cout = cout
            self.roles = roles

    def register(self):
        """Enregistrement de l'utilisateur"""
        link = db.DBLink()
        #Enregistrement des données utilisateur
        query = "INSERT INTO utilisateur \
                (IDFonc, Nom, Prénom, Identifiant, MdP, SalaireBrut) \
                VALUES (%s, %s, %s, %s, %s, %s)"
        link.commit(query, [self.id_fonc, self.nom, self.prenom, self.identifiant, self._mdp, self.cout])
        #Chargement de l'id ainsi créé
        query = "SELECT IDUtil \
                FROM utilisateur \
                WHERE identifiant = %s"
        result = link.query(query, [self.identifiant, ])

        for IDUtil, in result:
            self._id_table = IDUtil
        #Enregistrement des roles
        self.update_roles()

    def update(self):
        """Mise à jour de l'utilisateur"""
        link = db.DBLink()
        query = "UPDATE utilisateur \
                SET Nom = %s, Prénom = %s, Identifiant = %s, MdP = %s, IDFonc = %s, SalaireBrut = %s \
                WHERE IDUtil = %s"
        link.commit(query, [self.nom, self.prenom, self.identifiant, self._mdp, self.id_fonc, self.cout, self._id_table])

    def delete(self):
        """supprimer l'utilisateur courant"""
        link = db.DBLink()

        query = "DELETE \
                FROM roleattribution \
                WHERE IDUtil = %s"
        link.commit(query, [self._id_table, ])

        query = "DELETE \
                FROM utilisateur \
                WHERE IDUtil = %s"
        link.commit(query, [self._id_table, ])


    def get_roles(self):
        """liste des roles de l'utilisateur"""
        link = db.DBLink()
        query = "SELECT a.IDRole AS id_role, r.Libellé AS role \
                FROM roleattribution AS a \
                JOIN role AS r ON a.IDRole = r.IDRole \
                WHERE a.IDUtil = %s"
        result = link.query(query, [self._id_table, ])

        for id_role, role in result:
            self.roles[role] = id_role

    def update_roles(self):
        """enregistrement/mise à jour des roles de l'uitlisateur"""
        link = db.DBLink()

        #On commence par supprimer les roles actuels s'ils existent
        query = "DELETE \
                FROM roleattribution \
                WHERE IDUtil = %s"
        link.commit(query, [self._id_table, ])

        #Puis on enregistre les nouveaux
        for rol_id in self.roles.values():
            query = "INSERT INTO roleattribution \
                        (IDUtil, IDRole) \
                        VALUES(%s, %s)"
            link.commit(query, [self._id_table, rol_id])
