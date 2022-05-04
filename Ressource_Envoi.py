# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'C:\Users\Camille\Desktop\envoi.ui'
#
# Created by: PyQt5 UI code generator 5.6
#
# WARNING! All changes made in this file will be lost!

from PyQt5 import QtCore, QtGui, QtWidgets

class Ui_Envoi(object):
    def setupUi(self, Envoi):
        Envoi.setObjectName("Envoi")
        Envoi.resize(615, 351)
        self.label = QtWidgets.QLabel(Envoi)
        self.label.setGeometry(QtCore.QRect(50, 50, 91, 21))
        self.label.setObjectName("label")
        self.lineEdit = QtWidgets.QLineEdit(Envoi)
        self.lineEdit.setGeometry(QtCore.QRect(140, 50, 431, 20))
        self.lineEdit.setText("")
        self.lineEdit.setObjectName("lineEdit")
        self.label_2 = QtWidgets.QLabel(Envoi)
        self.label_2.setGeometry(QtCore.QRect(90, 170, 47, 21))
        self.label_2.setObjectName("label_2")
        self.lineEdit_2 = QtWidgets.QLineEdit(Envoi)
        self.lineEdit_2.setGeometry(QtCore.QRect(140, 170, 431, 20))
        self.lineEdit_2.setObjectName("lineEdit_2")
        self.pushButton_Retour = QtWidgets.QPushButton(Envoi)
        self.pushButton_Retour.setGeometry(QtCore.QRect(410, 320, 75, 23))
        self.pushButton_Retour.setObjectName("pushButton_Retour")
        self.pushButton_Envoyer = QtWidgets.QPushButton(Envoi)
        self.pushButton_Envoyer.setGeometry(QtCore.QRect(500, 320, 75, 23))
        self.pushButton_Envoyer.setObjectName("pushButton_Envoyer")
        self.label_3 = QtWidgets.QLabel(Envoi)
        self.label_3.setGeometry(QtCore.QRect(110, 100, 21, 21))
        self.label_3.setObjectName("label_3")
        self.lineEdit_IP = QtWidgets.QLineEdit(Envoi)
        self.lineEdit_IP.setGeometry(QtCore.QRect(140, 100, 141, 22))
        self.lineEdit_IP.setObjectName("lineEdit_IP")

        self.retranslateUi(Envoi)
        QtCore.QMetaObject.connectSlotsByName(Envoi)

    def retranslateUi(self, Envoi):
        _translate = QtCore.QCoreApplication.translate
        Envoi.setWindowTitle(_translate("Envoi", "Envoi"))
        self.label.setText(_translate("Envoi", "Clé de cryptage :"))
        self.label_2.setText(_translate("Envoi", "Texte :"))
        self.pushButton_Retour.setText(_translate("Envoi", "Retour"))
        self.pushButton_Envoyer.setText(_translate("Envoi", "Envoyer"))
        self.label_3.setText(_translate("Envoi", "IP :"))


if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    Envoi = QtWidgets.QDialog()
    ui = Ui_Envoi()
    ui.setupUi(Envoi)
    Envoi.show()
    sys.exit(app.exec_())

