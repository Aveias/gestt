# -*-coding:utf8 -*

import Auth.authentication as auth
import Auth.login as log
import Users.Model as U
import os

#On appelle le module d'identification
login = log.Login()
login.fenetre.mainloop()

#On lance le programme
while auth.Auth.access == True:
    print("programme en cours")
    user = U.User('test')
    print(user.nom)
    print(user.prenom)
    os.system("pause")
