# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'c:\workspaces\ws-aps\FristScreen.ui'
#
# Created by: PyQt5 UI code generator 5.15.4
#
# WARNING: Any manual changes made to this file will be lost when pyuic5 is
# run again.  Do not edit this file unless you know what you are doing.


from PyQt5 import QtCore, QtGui, QtWidgets


class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(498, 630)
        MainWindow.setStyleSheet("background-color: rgb(44, 128, 255);\n"
"background-color: rgb(255, 255, 255);")
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.enter_Button = QtWidgets.QPushButton(self.centralwidget)
        self.enter_Button.setGeometry(QtCore.QRect(150, 320, 181, 51))
        font = QtGui.QFont()
        font.setPointSize(15)
        self.enter_Button.setFont(font)
        self.enter_Button.setStyleSheet("background-color: rgb(0, 102, 0);\n"
"alternate-background-color: rgb(0, 85, 0);\n"
"border-style: outset;\n"
"border-width: 2px;\n"
"border-radius: 15px;\n"
"border-color: black;")
        self.enter_Button.setObjectName("enter_Button")
        self.user_name = QtWidgets.QLineEdit(self.centralwidget)
        self.user_name.setGeometry(QtCore.QRect(110, 160, 261, 31))
        font = QtGui.QFont()
        font.setPointSize(12)
        self.user_name.setFont(font)
        self.user_name.setStyleSheet("background-color: rgb(255, 255, 255);\n"
"border-radius: 15px;\n"
"border-style: outset;\n"
"border-width: 2px;")
        self.user_name.setObjectName("user_name")
        self.password = QtWidgets.QLineEdit(self.centralwidget)
        self.password.setGeometry(QtCore.QRect(110, 220, 261, 31))
        font = QtGui.QFont()
        font.setPointSize(12)
        self.password.setFont(font)
        self.password.setStyleSheet("background-color: rgb(255, 255, 255);\n"
"border-radius: 15px;\n"
"border-style: outset;\n"
"border-width: 2px;")
        self.password.setObjectName("password")
        self.label = QtWidgets.QLabel(self.centralwidget)
        self.label.setGeometry(QtCore.QRect(20, 510, 211, 31))
        font = QtGui.QFont()
        font.setPointSize(15)
        self.label.setFont(font)
        self.label.setObjectName("label")
        self.cad_Button = QtWidgets.QPushButton(self.centralwidget)
        self.cad_Button.setGeometry(QtCore.QRect(280, 500, 171, 41))
        font = QtGui.QFont()
        font.setPointSize(15)
        self.cad_Button.setFont(font)
        self.cad_Button.setStyleSheet("background-color: rgb(0, 102, 0);\n"
"border-radius: 15px;\n"
"border-style: outset;\n"
"border-width: 2px;\n"
"border-color: black;")
        self.cad_Button.setObjectName("cad_Button")
        self.label_2 = QtWidgets.QLabel(self.centralwidget)
        self.label_2.setGeometry(QtCore.QRect(70, 150, 71, 51))
        self.label_2.setText("")
        self.label_2.setPixmap(QtGui.QPixmap("c:\\workspaces\\ws-aps\\login.png"))
        self.label_2.setObjectName("label_2")
        self.label_3 = QtWidgets.QLabel(self.centralwidget)
        self.label_3.setGeometry(QtCore.QRect(70, 210, 51, 51))
        self.label_3.setText("")
        self.label_3.setPixmap(QtGui.QPixmap("c:\\workspaces\\ws-aps\\padlock.png"))
        self.label_3.setObjectName("label_3")
        self.label_4 = QtWidgets.QLabel(self.centralwidget)
        self.label_4.setGeometry(QtCore.QRect(40, 270, 401, 21))
        font = QtGui.QFont()
        font.setPointSize(15)
        self.label_4.setFont(font)
        self.label_4.setText("")
        self.label_4.setObjectName("label_4")
        self.bio_Button = QtWidgets.QPushButton(self.centralwidget)
        self.bio_Button.setGeometry(QtCore.QRect(150, 400, 181, 51))
        font = QtGui.QFont()
        font.setPointSize(15)
        self.bio_Button.setFont(font)
        self.bio_Button.setStyleSheet("background-color: rgb(60, 60, 179);\n"
"background-color: rgb(0, 102, 0);\n"
"alternate-background-color: rgb(0, 85, 0);\n"
"border-style: outset;\n"
"border-width: 2px;\n"
"border-radius: 15px;\n"
"border-color: black;")
        self.bio_Button.setObjectName("bio_Button")
        self.label_5 = QtWidgets.QLabel(self.centralwidget)
        self.label_5.setGeometry(QtCore.QRect(70, 0, 311, 171))
        self.label_5.setStyleSheet("")
        self.label_5.setText("")
        self.label_5.setTextFormat(QtCore.Qt.AutoText)
        self.label_5.setPixmap(QtGui.QPixmap(":/maggi/imgTela1.png"))
        self.label_5.setScaledContents(True)
        self.label_5.setObjectName("label_5")
        self.label_5.raise_()
        self.label_3.raise_()
        self.label_2.raise_()
        self.enter_Button.raise_()
        self.user_name.raise_()
        self.password.raise_()
        self.label.raise_()
        self.cad_Button.raise_()
        self.label_4.raise_()
        self.bio_Button.raise_()
        MainWindow.setCentralWidget(self.centralwidget)
        self.menubar = QtWidgets.QMenuBar(MainWindow)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 498, 26))
        self.menubar.setObjectName("menubar")
        MainWindow.setMenuBar(self.menubar)
        self.statusbar = QtWidgets.QStatusBar(MainWindow)
        self.statusbar.setObjectName("statusbar")
        MainWindow.setStatusBar(self.statusbar)

        self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "MainWindow"))
        self.enter_Button.setText(_translate("MainWindow", "ENTRAR"))
        self.user_name.setPlaceholderText(_translate("MainWindow", "LOGIN"))
        self.password.setPlaceholderText(_translate("MainWindow", "SENHA"))
        self.label.setText(_translate("MainWindow", "Não é cadastrado?"))
        self.cad_Button.setText(_translate("MainWindow", "CADASTRAR"))
        self.bio_Button.setText(_translate("MainWindow", "BIOMETRIA"))
import im_1_rc
