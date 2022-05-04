import sys
import socket
import select
import time
import hashlib
from threading import Thread

from PyQt5 import QtWidgets
from Ressource_Menu import Ui_Menu
from Ressource_Envoi import Ui_Envoi
from Ressource_Recevoir import Ui_Recevoir
from Ressource_Message_Erreur import Ui_Message_Erreur
from Ressource_Aide import Ui_Aide

hote = '0.0.0.0'
port = 12800

class Reader(Thread):
    def __init__(self, clef, label):
        Thread.__init__(self)
        self.clef = clef
        self.label = label
        self.closed = False
    def setkey(self, clef):
        self.clef = clef
    def closeconnection(self):
        self.closed = True
    def run(self):
        connexion_principale = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        connexion_principale.bind((hote, port))
        connexion_principale.listen(5)
        print("Le serveur écoute à présent sur le port {}".format(port))

        connexion_avec_client, info_connexion = connexion_principale.accept()
        msg_recu = ""
        while msg_recu != "fin" and self.closed == False:
            msg_recu = connexion_avec_client.recv(1024)
            msg_recu = msg_recu.decode()
            msg_recu = dechiffrage_vigenere(msg_recu, self.clef)
            self.label.setText(msg_recu)
            connexion_avec_client.send(chiffrage_vigenere("5/5", self.clef).encode())

        print("Fermeture de la connexion")
        connexion_principale.close()
        connexion_avec_client.close()

class Mon_Appli(QtWidgets.QDialog, Ui_Menu):
    def __init__(self,parent = None):
        super(Mon_Appli,self).__init__(parent)
        self.setupUi(self)
        # Ajout de connexion pour la gestion des évenements
        self.pushButton_Quitter.clicked.connect(self.QuitterApp)
        self.pushButton_Envoyer.clicked.connect(self.FenetreEnvoi)
        self.pushButton_Recevoir.clicked.connect(self.FenetreRecevoir)
        self.pushButton_Aide.clicked.connect(self.FenetreAide)
    # Ajout des fonctions appélées par les signaux définis plus haut
    def QuitterApp(self):
        self.reject()
    def FenetreEnvoi(self):
        self.reject()
        self.Fenvoi = Envoi()
        self.Fenvoi.show()
    def FenetreRecevoir(self):
        self.reject()
        self.FRecevoir = Recevoir()
        self.FRecevoir.show()
    def FenetreAide(self):
        self.FAide = Aide()
        self.FAide.show()


class Aide(QtWidgets.QDialog, Ui_Aide):
    def __init__(self,parent = None):
        super(Aide,self).__init__(parent)
        self.setupUi(self)
        # Ajout de connexion pour la gestion des évenements
        self.pushButton_OK.clicked.connect(self.QuitterApp)
    # Ajout des fonctions appélées par les signaux définis plus haut
    def QuitterApp(self):
        self.reject()



class Envoi(QtWidgets.QDialog, Ui_Envoi):
    def __init__(self,parent = None):
        super(Envoi,self).__init__(parent)
        self.setupUi(self)

        # Ajout de connexion pour la gestion des évenements
        self.pushButton_Retour.clicked.connect(self.QuitterApp)
        self.pushButton_Envoyer.clicked.connect(self.EnvoiMessage)
        # Ajout des fonctions appélées par les signaux définis plus haut

        self.first =  True
        self.connexion_avec_serveur = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    def QuitterApp(self):
        self.reject()
        self.application = Mon_Appli()
        self.application.show()

    def EnvoiMessage(self):
        message = self.lineEdit_2.text()
        hote = socket.gethostname()#self.lineEdit_IP.text()
        clef = self.lineEdit.text() # texte du message
        self.Ferreur = Message_Erreur()
        if len(message) == 0 :
            self.Ferreur.label_2.setText("Il n'y a pas de message")
            self.Ferreur.show()
        elif len(clef) == 0 :
            self.Ferreur.label_2.setText("Le message n'est pas crypté")
            self.Ferreur.show()
        elif len(hote) == 0 :
            self.Ferreur.label_2.setText("L'IP n'a pas été enregistré")
            self.Ferreur.show()
        else:
            if self.first == True:
                self.connexion_avec_serveur.connect((hote, port))
                print("Connexion établie avec le serveur sur le port {}".format(port))
                self.first = False

            msg_a_envoyer = self.lineEdit_2.text()
            msg_a_envoyer = chiffrage_vigenere(msg_a_envoyer,clef)
            msg_a_envoyer = msg_a_envoyer.encode()
            self.connexion_avec_serveur.send(msg_a_envoyer)
            msg_recu = self.connexion_avec_serveur.recv(1024)
            print(dechiffrage_vigenere(msg_recu.decode(), clef))

            if msg_a_envoyer == chiffrage_vigenere("fin", clef).encode():
                print("Fermeture de la connexion")
                self.connexion_avec_serveur.close()
                exit(0)

class Recevoir(QtWidgets.QDialog, Ui_Recevoir):
    def __init__(self,parent = None):
        super(Recevoir,self).__init__(parent)
        self.setupUi(self)

        # Ajout de connexion pour la gestion des évenements
        self.pushButton_Retour.clicked.connect(self.QuitterApp)
        self.pushButton_Repondre.clicked.connect(self.FenetreRepondre)
        self.pushButton_IP.clicked.connect(self.FenetreIP)
        # Ajout des fonctions appélées par les signaux définis plus haut

        self.first = True
        self.reader = Reader("", self.label_TeteRecu)
        self.reader.start()

    def QuitterApp(self):
        self.reader.closeconnection()
        self.reject()
        self.application = Mon_Appli()
        self.application.show()

    def FenetreRepondre(self):
        self.reject()
        self.Fenvoi = Envoi()
        self.Fenvoi.show()

    def FenetreIP(self):
        IP = self.lineEdit_2_IP.text() #Texte de l'IP
        self.Ferreur = Message_Erreur()
        hote = self.lineEdit_2_IP.text()
        clef = self.lineEdit.text()
        #if len(IP) == 0 :
        #    self.Ferreur.label_2.setText("Il n'y a pas d'IP")
        #    self.Ferreur.show()
        if len(clef) == 0 :
            self.Ferreur.label_2.setText("La clé n'a pas été enregistré")
            self.Ferreur.show()
        else:
            #Faire le bidule pour recevoir le message
            self.reader.setkey(clef)

class Message_Erreur(QtWidgets.QDialog, Ui_Message_Erreur):
    def __init__(self,parent = None):
        super(Message_Erreur,self).__init__(parent)
        self.setupUi(self)
        # Ajout de connexion pour la gestion des évenements
        self.pushButton_Ok.clicked.connect(self.QuitterApp)
        # Ajout des fonctions appélées par les signaux définis plus haut
    def QuitterApp(self):
        self.reject()

# Défintion du script général
def chiffrage_vigenere(message,clef):
    chaine=""
    compteur_clef=0
    clef = hashlib.sha224(clef.encode()).digest()
    for lettre_messsage in  message:
        if compteur_clef==len(clef):
            compteur_clef=0
            clef = hashlib.sha224(clef).digest()
        asci_message=ord(lettre_messsage)
        if asci_message<123 and asci_message>96:
            asci_message=asci_message-97
            lettre_chifree=(asci_message+clef[compteur_clef])%26
            compteur_clef=compteur_clef+1
            lettre_chifree=chr(lettre_chifree+97)
        else:
            lettre_chifree=lettre_messsage
        chaine=chaine+lettre_chifree
    return(chaine)

def dechiffrage_vigenere(message_chiffre,clef):
    chaine=""
    compteur_clef=0
    clef = hashlib.sha224(clef.encode()).digest()
    for lettre_messsage in  message_chiffre:
        if compteur_clef==len(clef):
            compteur_clef=0
            clef = hashlib.sha224(clef).digest()
        asci_message=ord(lettre_messsage)
        if asci_message<123 and asci_message>96 :
            asci_message=asci_message-97
            decal_clef=clef[compteur_clef]
            lettre_chifree=(asci_message-decal_clef)%26
            compteur_clef=compteur_clef+1
            car_ajouter=chr(lettre_chifree+97)
        else:
            car_ajouter=lettre_messsage
        chaine=chaine+car_ajouter
    return(chaine)

def main():
    app = QtWidgets.QApplication(sys.argv)   # Appel des methodes QApplication
    application = Mon_Appli()
    application.show()  # Montrer la GUI
    rc = app.exec_()
    sys.exit(rc)   # Permet de clore et de renvoyer la valeur de fin

"""
Lancement du script général s'il n'est pas appelé dans un autre...
"""
if __name__ =="__main__":
    main()

