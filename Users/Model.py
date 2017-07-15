# -*-coding:utf8 -*

import DB.dbLink as db

class User:
    """Modèle utilisateur. Contient un objet utilisateur"""

    def __init__(self, id):
        """Constructeur créant utilisateur à partir d'un ID"""
        self.identifiant = id

        #On va chercher l'user en base de données
        link = db.DBLink()
        query = "SELECT u.IDUtil AS id_bdd, u.Nom AS nom, u.Prénom AS prenom, u.Identifiant AS identifiant, u.MdP AS mdp, u.SalaireBrut AS cout, u.IDFonc AS id_fonc, f.Intitulé AS fonction, p.Libelle AS pole \
                FROM utilisateur AS u \
                JOIN fonction AS f ON f.IDFonc = u.IDFonc \
                JOIN pole AS p ON p.IDPole = p.IDPole \
                WHERE u.identifiant = %s"
        result = link.query(query, [self.identifiant, ])

        #On remplit l'objet à partir des éléments récupérés en BDD
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


    def hydrate(self, nom, prenom, identifiant, mdp, cout, idfonc, fonction, pole):
        """Hydratation de l'objet"""
        self.id_fonc = idfonc
        self.fonction = fonction
        self.pole = pole
        self.nom = nom
        self.prenom = prenom
        self.identifiant = identifiant
        self._mdp = mdp
        self.cout = cout

    def register(self):
        """Enregistrement de l'utilisateur"""
        link = db.DBLink()
        query = "INSERT INTO utilisateur \
                (IDFonc, Nom, Prénom, Identifiant, MdP, SalaireBrut) \
                VALUES (%s, %s, %s, %s, %s, %s)"
        link.commit(query, [self.id_fonc, self.nom, self.prenom, self.identifiant, self._mdp, self.cout])


    def update(self):
        """Mise à jour de l'utilisateur"""
        link = db.DBLink()
        query = "UPDATE utilisateur \
                SET Nom = %s, Prénom = %s, Identifiant = %s, MdP = %s, IDFonc = %s, SalaireBrut = %s \
                WHERE IDUtil = %s"
        link.commit(query, [self.nom, self.prenom, self.identifiant, self._mdp, self.id_fonc, self.cout, self._id_table])

    def delete(self):
        """supprimer un utilisateur"""
        

    def getRoles(self):
        """liste des roles de l'utilisateur"""
