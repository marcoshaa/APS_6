# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'c:\workspaces\ws-aps\level3.ui'
#
# Created by: PyQt5 UI code generator 5.15.4
#
# WARNING: Any manual changes made to this file will be lost when pyuic5 is
# run again.  Do not edit this file unless you know what you are doing.


from PyQt5 import QtCore, QtGui, QtWidgets


class Ui_level_3(object):
    def setupUi(self, level_3):
        level_3.setObjectName("level_3")
        level_3.resize(800, 594)
        level_3.setStyleSheet("")
        self.centralwidget = QtWidgets.QWidget(level_3)
        self.centralwidget.setObjectName("centralwidget")
        self.intro_Level3 = QtWidgets.QLabel(self.centralwidget)
        self.intro_Level3.setGeometry(QtCore.QRect(0, -10, 801, 571))
        font = QtGui.QFont()
        font.setPointSize(50)
        self.intro_Level3.setFont(font)
        self.intro_Level3.setStyleSheet("\n"
"")
        self.intro_Level3.setText("")
        self.intro_Level3.setPixmap(QtGui.QPixmap(":/nivel3/armMaggi.jpg"))
        self.intro_Level3.setScaledContents(True)
        self.intro_Level3.setObjectName("intro_Level3")
        self.label = QtWidgets.QLabel(self.centralwidget)
        self.label.setGeometry(QtCore.QRect(250, 10, 201, 51))
        font = QtGui.QFont()
        font.setPointSize(20)
        font.setBold(True)
        font.setItalic(False)
        font.setUnderline(False)
        font.setWeight(75)
        font.setStrikeOut(False)
        font.setKerning(True)
        self.label.setFont(font)
        self.label.setStyleSheet("background-color: rgb(255, 255, 255);\n"
"border-style: outset;\n"
"border-width: 2px;\n"
"border-radius: 15px;\n"
"border-color: black;")
        self.label.setObjectName("label")
        self.textBrowser = QtWidgets.QTextBrowser(self.centralwidget)
        self.textBrowser.setGeometry(QtCore.QRect(20, 110, 381, 401))
        self.textBrowser.setObjectName("textBrowser")
        self.pushButton_4 = QtWidgets.QPushButton(self.centralwidget)
        self.pushButton_4.setGeometry(QtCore.QRect(530, 440, 141, 61))
        self.pushButton_4.setStyleSheet("background-color: rgb(255, 255, 255);\n"
"alternate-background-color: rgb(0, 85, 0);\n"
"border-style: outset;\n"
"border-width: 2px;\n"
"border-radius: 15px;\n"
"border-color: black;")
        self.pushButton_4.setObjectName("pushButton_4")
        level_3.setCentralWidget(self.centralwidget)
        self.menubar = QtWidgets.QMenuBar(level_3)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 800, 26))
        self.menubar.setObjectName("menubar")
        level_3.setMenuBar(self.menubar)
        self.statusbar = QtWidgets.QStatusBar(level_3)
        self.statusbar.setObjectName("statusbar")
        level_3.setStatusBar(self.statusbar)

        self.retranslateUi(level_3)
        QtCore.QMetaObject.connectSlotsByName(level_3)

    def retranslateUi(self, level_3):
        _translate = QtCore.QCoreApplication.translate
        level_3.setWindowTitle(_translate("level_3", "MainWindow"))
        self.label.setText(_translate("level_3", "Agrotóxico"))
        self.pushButton_4.setText(_translate("level_3", "PushButton"))
import imgNivel3_rc
