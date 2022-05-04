# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'C:\Users\Camille\Desktop\Menu.ui'
#
# Created by: PyQt5 UI code generator 5.6
#
# WARNING! All changes made in this file will be lost!

from PyQt5 import QtCore, QtGui, QtWidgets

class Ui_Menu(object):
    def setupUi(self, Menu):
        Menu.setObjectName("Menu")
        Menu.resize(522, 244)
        self.pushButton_Envoyer = QtWidgets.QPushButton(Menu)
        self.pushButton_Envoyer.setGeometry(QtCore.QRect(220, 70, 75, 23))
        self.pushButton_Envoyer.setObjectName("pushButton_Envoyer")
        self.pushButton_Recevoir = QtWidgets.QPushButton(Menu)
        self.pushButton_Recevoir.setGeometry(QtCore.QRect(220, 110, 75, 23))
        self.pushButton_Recevoir.setObjectName("pushButton_Recevoir")
        self.pushButton_Quitter = QtWidgets.QPushButton(Menu)
        self.pushButton_Quitter.setGeometry(QtCore.QRect(440, 210, 75, 23))
        self.pushButton_Quitter.setObjectName("pushButton_Quitter")
        self.pushButton_Aide = QtWidgets.QPushButton(Menu)
        self.pushButton_Aide.setEnabled(True)
        self.pushButton_Aide.setGeometry(QtCore.QRect(10, 210, 75, 23))
        self.pushButton_Aide.setMaximumSize(QtCore.QSize(93, 28))
        self.pushButton_Aide.setObjectName("pushButton_Aide")

        self.retranslateUi(Menu)
        QtCore.QMetaObject.connectSlotsByName(Menu)

    def retranslateUi(self, Menu):
        _translate = QtCore.QCoreApplication.translate
        Menu.setWindowTitle(_translate("Menu", "Menu"))
        self.pushButton_Envoyer.setText(_translate("Menu", "Envoyer"))
        self.pushButton_Recevoir.setText(_translate("Menu", "Recevoir"))
        self.pushButton_Quitter.setText(_translate("Menu", "Quitter"))
        self.pushButton_Aide.setText(_translate("Menu", "Aide"))


if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    Menu = QtWidgets.QDialog()
    ui = Ui_Menu()
    ui.setupUi(Menu)
    Menu.show()
    sys.exit(app.exec_())

