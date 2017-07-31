# -*-coding:utf8 -*

import DB.dbLink as db

class User:
    """Modèle utilisateur. Contient un objet utilisateur"""

    def __init__(self, user_id='', nom='', prenom='', identifiant='', mdp='', cout='', idfonc='', fonction='', pole='', roles=dict()):
        """Constructeur initialisant utilisateur à partir d'un ID ou des données indiquées"""

        #On load l'user depuis la BDD si demandé avec un ID
        if user_id != '':
            self._id_table = user_id
            #On va chercher l'user en base de données
            link = db.DBLink()
            query = "SELECT u.IDUtil AS id_bdd, u.Nom AS bdd_nom, u.Prénom AS bdd_prenom, u.Identifiant AS bdd_identifiant, u.MdP AS bdd_mdp, u.SalaireBrut AS bdd_cout, u.IDFonc AS bdd_id_fonc, f.Intitulé AS bdd_fonction, p.Libelle AS bdd_pole \
                    FROM utilisateur AS u \
                    JOIN fonction AS f ON f.IDFonc = u.IDFonc \
                    JOIN pole AS p ON p.IDPole = p.IDPole \
                    WHERE u.IDUtil = %s"
            result = link.query(query, [self._id_table, ])

            #On hydrate l'objet à partir des éléments récupérés en BDD
            for id_bdd, bdd_nom, bdd_prenom, bdd_identifiant, bdd_mdp, bdd_cout, bdd_id_fonc, bdd_fonction, bdd_pole in result:
                self._id_table = id_bdd
                self.fonction = bdd_fonction
                self.pole = bdd_pole
                self.nom = bdd_nom
                self.prenom = bdd_prenom
                self.identifiant = bdd_identifiant
                self._mdp = bdd_mdp
                self.cout = bdd_cout
                self.id_fonc = bdd_id_fonc

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
