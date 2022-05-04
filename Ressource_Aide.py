# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'C:\Users\Camille\Desktop\Aide.ui'
#
# Created by: PyQt5 UI code generator 5.6
#
# WARNING! All changes made in this file will be lost!

from PyQt5 import QtCore, QtGui, QtWidgets

class Ui_Aide(object):
    def setupUi(self, Aide):
        Aide.setObjectName("Aide")
        Aide.resize(1135, 408)
        self.label = QtWidgets.QLabel(Aide)
        self.label.setGeometry(QtCore.QRect(20, 20, 1091, 311))
        self.label.setObjectName("label")
        self.pushButton_OK = QtWidgets.QPushButton(Aide)
        self.pushButton_OK.setGeometry(QtCore.QRect(480, 370, 101, 28))
        self.pushButton_OK.setObjectName("pushButton_OK")

        self.retranslateUi(Aide)
        QtCore.QMetaObject.connectSlotsByName(Aide)

    def retranslateUi(self, Aide):
        _translate = QtCore.QCoreApplication.translate
        Aide.setWindowTitle(_translate("Aide", "Aide"))
        self.label.setText(_translate("Aide", "Voici le menu des aides, nous allons pour commencer vous décrire comment envoyer et réceptionner un message.\n"
"\n"
"Pour commencer il est nécessaire pour recevoir un message d’aller dans la page recevoir, d’entrer la clé de cryptage convenue entre les deux utilisateurs, l’ip, et de cliquer sur recevoir,\n"
" ainsi le programme rentrera dans une boucle ou il écoutera en continue.\n"
"\n"
"Pour envoyer un message, il faut ici aussi entrer la clé, puis l’ip, et enfin le message à envoyer. Pour l’envoyer il faut, après cela, cliquer sur le bouton envoyer. \n"
"Il est maintenant possible de renvoyer des messages en recliquant sur envoyer et en modifiant le message.\n"
"\n"
"Pour fermer la connexion il est nécessaire de fermer le programme.        "))
        self.pushButton_OK.setText(_translate("Aide", "Ok"))


if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    Aide = QtWidgets.QDialog()
    ui = Ui_Aide()
    ui.setupUi(Aide)
    Aide.show()
    sys.exit(app.exec_())

