# -*-coding:utf8 -*

import DB.dbids as dbids
import mysql.connector as mariadb


class DBLink:
    """Classe permettant de faire des requetes à la base de données"""

    _db_connection = None
    _db_cur = None

    #On ouvre la connexion
    def __init__(self):
        db_ids = dbids.getIds()
        self._db_connection = mariadb.connect(host = db_ids["host"], user = db_ids["user"], password = db_ids["password"], database = db_ids["database"])
        self._db_cur = self._db_connection.cursor()

    def query(self, query, args, multi=False):
        """query standard"""
        try:
            self._db_cur.execute(query, args, multi)
        except mariadb.Error as e:
            self._db_cur = False
            print("Erreur : ", e)
        return self._db_cur

    def commit(self, query, args):
        """ajout d'un élément en bdd standard"""
        try:
            self._db_cur.execute(query, args)
            self._db_connection.commit()

        except mariadb.Error as e:

            print("Erreur : ", e)
        return self._db_cur

    def __del__(self):
        """fermeture de la connexion"""
        self._db_connection.close()

def DBTest():
    quer = "SELECT Nom FROM utilisateur"
    link = DBLink()
    result = link.query("SELECT Nom FROM utilisateur", [])

    for Nom in result:
        print(Nom)
