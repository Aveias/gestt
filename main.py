# -*-coding:Latin-1 -*

from tkinter import *
import Auth.authentication as auth
import Auth.login as log
import os

#On appelle le module d'identification
login = log.Login()
login.fenetre.mainloop()

#On lance le programme
while auth.Auth.access == True:
    print("programme en cours")
    os.system("pause")
