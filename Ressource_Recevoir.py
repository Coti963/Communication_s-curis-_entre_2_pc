# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'C:\Users\Camille\Desktop\Recevoir.ui'
#
# Created by: PyQt5 UI code generator 5.6
#
# WARNING! All changes made in this file will be lost!

from PyQt5 import QtCore, QtGui, QtWidgets

class Ui_Recevoir(object):
    def setupUi(self, Recevoir):
        Recevoir.setObjectName("Recevoir")
        Recevoir.resize(656, 336)
        self.label = QtWidgets.QLabel(Recevoir)
        self.label.setGeometry(QtCore.QRect(20, 180, 71, 21))
        self.label.setObjectName("label")
        self.label_TeteRecu = QtWidgets.QLabel(Recevoir)
        self.label_TeteRecu.setGeometry(QtCore.QRect(90, 180, 461, 101))
        self.label_TeteRecu.setText("")
        self.label_TeteRecu.setObjectName("label_TeteRecu")
        self.pushButton_Retour = QtWidgets.QPushButton(Recevoir)
        self.pushButton_Retour.setGeometry(QtCore.QRect(200, 300, 93, 28))
        self.pushButton_Retour.setObjectName("pushButton_Retour")
        self.pushButton_Repondre = QtWidgets.QPushButton(Recevoir)
        self.pushButton_Repondre.setGeometry(QtCore.QRect(330, 300, 93, 28))
        self.pushButton_Repondre.setObjectName("pushButton_Repondre")
        self.label_2 = QtWidgets.QLabel(Recevoir)
        self.label_2.setGeometry(QtCore.QRect(0, 50, 101, 20))
        self.label_2.setObjectName("label_2")
        self.lineEdit = QtWidgets.QLineEdit(Recevoir)
        self.lineEdit.setGeometry(QtCore.QRect(110, 50, 441, 22))
        self.lineEdit.setObjectName("lineEdit")
        self.pushButton_IP = QtWidgets.QPushButton(Recevoir)
        self.pushButton_IP.setGeometry(QtCore.QRect(320, 120, 93, 28))
        self.pushButton_IP.setObjectName("pushButton_IP")
        self.label_3 = QtWidgets.QLabel(Recevoir)
        self.label_3.setGeometry(QtCore.QRect(80, 120, 21, 20))
        self.label_3.setObjectName("label_3")
        self.lineEdit_2_IP = QtWidgets.QLineEdit(Recevoir)
        self.lineEdit_2_IP.setGeometry(QtCore.QRect(100, 120, 211, 22))
        self.lineEdit_2_IP.setObjectName("lineEdit_2_IP")

        self.retranslateUi(Recevoir)
        QtCore.QMetaObject.connectSlotsByName(Recevoir)

    def retranslateUi(self, Recevoir):
        _translate = QtCore.QCoreApplication.translate
        Recevoir.setWindowTitle(_translate("Recevoir", "Recevoir"))
        self.label.setText(_translate("Recevoir", "Texte reçu :"))
        self.pushButton_Retour.setText(_translate("Recevoir", "Retour"))
        self.pushButton_Repondre.setText(_translate("Recevoir", "Répondre"))
        self.label_2.setText(_translate("Recevoir", "Clé de chiffrage : "))
        self.pushButton_IP.setText(_translate("Recevoir", "IP"))
        self.label_3.setText(_translate("Recevoir", "IP :"))


if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    Recevoir = QtWidgets.QDialog()
    ui = Ui_Recevoir()
    ui.setupUi(Recevoir)
    Recevoir.show()
    sys.exit(app.exec_())

