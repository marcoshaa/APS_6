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
        level_3.resize(800, 596)
        level_3.setStyleSheet("background-color: rgb(0, 85, 255);")
        self.centralwidget = QtWidgets.QWidget(level_3)
        self.centralwidget.setObjectName("centralwidget")
        self.intro_Level3 = QtWidgets.QLabel(self.centralwidget)
        self.intro_Level3.setGeometry(QtCore.QRect(230, 100, 221, 101))
        font = QtGui.QFont()
        font.setPointSize(50)
        self.intro_Level3.setFont(font)
        self.intro_Level3.setObjectName("intro_Level3")
        level_3.setCentralWidget(self.centralwidget)
        self.menubar = QtWidgets.QMenuBar(level_3)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 800, 21))
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
        self.intro_Level3.setText(_translate("level_3", "nivel 3"))