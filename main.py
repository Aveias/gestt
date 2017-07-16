# -*-coding:utf8 -*

import Auth.authentication as auth
import Auth.login as log
import Users.Model as U
import os

#On appelle le module d'identification - Commenté pour les pahses de test d'autres modules
login = log.Login()
login.fenetre.mainloop()

#On lance le programme
while auth.Auth.access == True:
    print("programme en cours")
    user = U.User(auth.Auth.current_user_id)
    print("Bonjour", user.nom, user.prenom, "vous êtes dans la boucle")

    os.system("pause")
