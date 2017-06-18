# -*-coding:utf8 -*

import DB.dbids as dbids
import mysql.connector as mariadb


class DBLink:
    """Classe permettant de faire une requete à la base de données"""

    _db_connection = None
    _db_cur = None

    #On ouvre la connexion
    def __init__(self):
        db_ids = dbids.getIds()
        self._db_connection = mariadb.connect(host = db_ids["host"], user = db_ids["user"], password = db_ids["password"], database = db_ids["database"])
        self._db_cur = self._db_connection.cursor()

    #Query standard
    def query(self, query, args):
        self._db_cur.execute(query, args)
        return self._db_cur

    #on ferme la connexion
    def __del__(self):
        self._db_connection.close()

def DBTest():
    quer = "SELECT Nom FROM utilisateur"
    link = DBLink()
    result = link.query("SELECT Nom FROM utilisateur", [])

    for Nom in result:
        print(Nom)
