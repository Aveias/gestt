# -*-coding:utf8 -*

import DB.dbLink as db

class User:
    """Modèle utilisateur. Contient un objet utilisateur"""

    def __init__(self, id):
        self.identifiant = id

        #On va chercher l'user en base de données
        link = db.DBLink()
        query = "SELECT u.IDUtil AS idBDD, u.Nom AS nom, u.Prénom AS prenom, u.Identifiant AS identifiant, u.MdP AS MdP, u.SalaireBrut AS cout, f.Intitulé AS fonction, p.Libelle AS pole FROM utilisateur AS u JOIN fonction AS f ON f.IDFonc = u.IDFonc JOIN pole AS p ON p.IDPole = p.IDPole WHERE u.identifiant = %s"
        result = link.query(query, [self.identifiant, ])

        #On remplit l'objet à partir des éléments récupérés en BDD
        for idBDD, nom, prenom, identifiant, MdP, cout, fonction, pole in result:
            self._id_table = idBDD
            self.fonction = fonction
            self.pole = pole
            self.nom = nom
            self.prenom = prenom
            self.identifiant = identifiant
            self._mdp  = MdP
            self.cout  = cout
