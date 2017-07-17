# -*-coding:UTF-8 -*
import Auth.authentification as auth
import Auth.login as log
import Menu.barreOutils as barre
import Users.Model as U
import os


#On appelle le module d'identification - Commenté pour les pahses de test d'autres modules
login = log.Login()
login.fenetre.mainloop()


#On lance le programme
while auth.Auth.access == True:
    print("programme en cours")
    user = U.User(auth.Auth.current_user)
    print("Bonjour", user.nom, user.prenom, "vous êtes dans la boucle")
    # Instanciation d'un objet de la classe BarreOutils
    barreOutils = barre.BarreOutils()
    barreOutils.fenetre.mainloop()
    # Test de l'attribut fermer de la classe BarreOutils() -> true si appuie sur le bouton deconnexion 
    print("fermer = ",barreOutils.fermer)
    
    if barreOutils.fermer == True:
      auth.Auth.access = False
    else:
        os.system("pause")
    # Test de l'attribut access qui détermine si on entre ou pas dans la boucle while
    print("access = ", auth.Auth.access)
    
    # Fin while



