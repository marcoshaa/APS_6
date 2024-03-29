# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'c:\workspaces\ws-aps\tela_cad.ui'
#
# Created by: PyQt5 UI code generator 5.15.4
#
# WARNING: Any manual changes made to this file will be lost when pyuic5 is
# run again.  Do not edit this file unless you know what you are doing.


from PyQt5 import QtCore, QtGui, QtWidgets


class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(510, 600)
        font = QtGui.QFont()
        font.setPointSize(15)
        MainWindow.setFont(font)
        MainWindow.setStyleSheet("")
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.CAD_USER = QtWidgets.QLineEdit(self.centralwidget)
        self.CAD_USER.setGeometry(QtCore.QRect(110, 120, 261, 31))
        font = QtGui.QFont()
        font.setPointSize(12)
        self.CAD_USER.setFont(font)
        self.CAD_USER.setStyleSheet("background-color: rgb(255, 255, 255);\n"
"border-radius: 15px;\n"
"border-style: outset;\n"
"border-width: 2px;")
        self.CAD_USER.setObjectName("CAD_USER")
        self.CAD_USER2 = QtWidgets.QLineEdit(self.centralwidget)
        self.CAD_USER2.setGeometry(QtCore.QRect(110, 170, 261, 31))
        font = QtGui.QFont()
        font.setPointSize(12)
        self.CAD_USER2.setFont(font)
        self.CAD_USER2.setStyleSheet("background-color: rgb(255, 255, 255);\n"
"border-radius: 15px;\n"
"border-style: outset;\n"
"border-width: 2px;")
        self.CAD_USER2.setObjectName("CAD_USER2")
        self.CAD_SENHA = QtWidgets.QLineEdit(self.centralwidget)
        self.CAD_SENHA.setGeometry(QtCore.QRect(110, 240, 261, 31))
        font = QtGui.QFont()
        font.setPointSize(12)
        self.CAD_SENHA.setFont(font)
        self.CAD_SENHA.setStyleSheet("background-color: rgb(255, 255, 255);\n"
"border-radius: 15px;\n"
"border-style: outset;\n"
"border-width: 2px;")
        self.CAD_SENHA.setEchoMode(QtWidgets.QLineEdit.Password)
        self.CAD_SENHA.setObjectName("CAD_SENHA")
        self.CAD_SENHA2 = QtWidgets.QLineEdit(self.centralwidget)
        self.CAD_SENHA2.setGeometry(QtCore.QRect(110, 290, 261, 31))
        font = QtGui.QFont()
        font.setPointSize(12)
        self.CAD_SENHA2.setFont(font)
        self.CAD_SENHA2.setStyleSheet("background-color: rgb(255, 255, 255);\n"
"border-radius: 15px;\n"
"border-style: outset;\n"
"border-width: 2px;")
        self.CAD_SENHA2.setEchoMode(QtWidgets.QLineEdit.Password)
        self.CAD_SENHA2.setObjectName("CAD_SENHA2")
        self.label_5 = QtWidgets.QLabel(self.centralwidget)
        self.label_5.setGeometry(QtCore.QRect(70, 110, 61, 51))
        self.label_5.setText("")
        self.label_5.setPixmap(QtGui.QPixmap("c:\\workspaces\\ws-aps\\login.png"))
        self.label_5.setObjectName("label_5")
        self.label_6 = QtWidgets.QLabel(self.centralwidget)
        self.label_6.setGeometry(QtCore.QRect(70, 160, 61, 51))
        self.label_6.setText("")
        self.label_6.setPixmap(QtGui.QPixmap("c:\\workspaces\\ws-aps\\login.png"))
        self.label_6.setObjectName("label_6")
        self.label_7 = QtWidgets.QLabel(self.centralwidget)
        self.label_7.setGeometry(QtCore.QRect(70, 230, 51, 51))
        self.label_7.setStyleSheet("")
        self.label_7.setText("")
        self.label_7.setPixmap(QtGui.QPixmap("c:\\workspaces\\ws-aps\\padlock.png"))
        self.label_7.setObjectName("label_7")
        self.label_3 = QtWidgets.QLabel(self.centralwidget)
        self.label_3.setGeometry(QtCore.QRect(70, 280, 51, 51))
        self.label_3.setText("")
        self.label_3.setPixmap(QtGui.QPixmap("c:\\workspaces\\ws-aps\\padlock.png"))
        self.label_3.setObjectName("label_3")
        self.BUTT_CAD = QtWidgets.QPushButton(self.centralwidget)
        self.BUTT_CAD.setGeometry(QtCore.QRect(160, 440, 161, 61))
        font = QtGui.QFont()
        font.setPointSize(15)
        self.BUTT_CAD.setFont(font)
        self.BUTT_CAD.setStyleSheet("background-color: rgb(85, 170, 0);\n"
"\n"
"border-radius: 15px;\n"
"border-style: outset;\n"
"border-width: 2px;\n"
"border-color: black;")
        self.BUTT_CAD.setObjectName("BUTT_CAD")
        self.label = QtWidgets.QLabel(self.centralwidget)
        self.label.setGeometry(QtCore.QRect(0, 0, 511, 571))
        self.label.setText("")
        self.label.setPixmap(QtGui.QPixmap(":/imgCad/telacad.png"))
        self.label.setScaledContents(True)
        self.label.setObjectName("label")
        self.label_2 = QtWidgets.QLabel(self.centralwidget)
        self.label_2.setGeometry(QtCore.QRect(60, 350, 271, 41))
        font = QtGui.QFont()
        font.setPointSize(14)
        self.label_2.setFont(font)
        self.label_2.setStyleSheet("background-color: rgb(255, 255, 255);\n"
"border-radius: 15px;\n"
"border-style: outset;\n"
"border-width: 2px;")
        self.label_2.setObjectName("label_2")
        self.nAcesso = QtWidgets.QLineEdit(self.centralwidget)
        self.nAcesso.setGeometry(QtCore.QRect(340, 350, 51, 41))
        font = QtGui.QFont()
        font.setPointSize(12)
        self.nAcesso.setFont(font)
        self.nAcesso.setStyleSheet("background-color: rgb(255, 255, 255);\n"
"border-radius: 15px;\n"
"border-style: outset;\n"
"border-width: 2px;")
        self.nAcesso.setEchoMode(QtWidgets.QLineEdit.Password)
        self.nAcesso.setPlaceholderText("")
        self.nAcesso.setObjectName("nAcesso")
        self.label.raise_()
        self.label_7.raise_()
        self.label_3.raise_()
        self.label_6.raise_()
        self.label_5.raise_()
        self.CAD_USER.raise_()
        self.CAD_USER2.raise_()
        self.CAD_SENHA.raise_()
        self.CAD_SENHA2.raise_()
        self.BUTT_CAD.raise_()
        self.label_2.raise_()
        self.nAcesso.raise_()
        MainWindow.setCentralWidget(self.centralwidget)
        self.menubar = QtWidgets.QMenuBar(MainWindow)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 510, 26))
        self.menubar.setObjectName("menubar")
        self.menuVOLTAR = QtWidgets.QMenu(self.menubar)
        self.menuVOLTAR.setObjectName("menuVOLTAR")
        MainWindow.setMenuBar(self.menubar)
        self.ola = QtWidgets.QStatusBar(MainWindow)
        self.ola.setObjectName("ola")
        MainWindow.setStatusBar(self.ola)
        self.menubar.addAction(self.menuVOLTAR.menuAction())

        self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "MainWindow"))
        self.CAD_USER.setPlaceholderText(_translate("MainWindow", "DIGITE O NOME "))
        self.CAD_USER2.setPlaceholderText(_translate("MainWindow", "DIGITE O LOGIN"))
        self.CAD_SENHA.setPlaceholderText(_translate("MainWindow", "INSIRA A SENHA"))
        self.CAD_SENHA2.setPlaceholderText(_translate("MainWindow", "CONFIRME A SENHA"))
        self.BUTT_CAD.setText(_translate("MainWindow", "CADASTRAR"))
        self.label_2.setText(_translate("MainWindow", "Defina o nivel de acesso"))
        self.menuVOLTAR.setTitle(_translate("MainWindow", "VOLTAR"))
import imgcad_rc
