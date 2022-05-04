# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'C:\Users\Thierry\Desktop\2019_2020\ISN\Projets\Camille\Message_Erreur.ui'
#
# Created by: PyQt5 UI code generator 5.6
#
# WARNING! All changes made in this file will be lost!

from PyQt5 import QtCore, QtGui, QtWidgets

class Ui_Message_Erreur(object):
    def setupUi(self, Message_Erreur):
        Message_Erreur.setObjectName("Message_Erreur")
        Message_Erreur.resize(400, 300)
        self.label = QtWidgets.QLabel(Message_Erreur)
        self.label.setGeometry(QtCore.QRect(170, 90, 71, 51))
        self.label.setObjectName("label")
        self.label_2 = QtWidgets.QLabel(Message_Erreur)
        self.label_2.setGeometry(QtCore.QRect(130, 130, 173, 16))
        self.label_2.setObjectName("label_2")
        self.pushButton_Ok = QtWidgets.QPushButton(Message_Erreur)
        self.pushButton_Ok.setGeometry(QtCore.QRect(160, 180, 75, 23))
        self.pushButton_Ok.setObjectName("pushButton_Ok")

        self.retranslateUi(Message_Erreur)
        QtCore.QMetaObject.connectSlotsByName(Message_Erreur)

    def retranslateUi(self, Message_Erreur):
        _translate = QtCore.QCoreApplication.translate
        Message_Erreur.setWindowTitle(_translate("Message_Erreur", "Dialog"))
        self.label.setText(_translate("Message_Erreur", "ATENTION !!!"))
        self.label_2.setText(_translate("Message_Erreur", ""))
        self.pushButton_Ok.setText(_translate("Message_Erreur", "Ok"))


if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    Message_Erreur = QtWidgets.QDialog()
    ui = Ui_Message_Erreur()
    ui.setupUi(Message_Erreur)
    Message_Erreur.show()
    sys.exit(app.exec_())

