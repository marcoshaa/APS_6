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
        self.intro_Level3.setStyleSheet("")
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
        self.textBrowser.setGeometry(QtCore.QRect(20, 110, 471, 401))
        font = QtGui.QFont()
        font.setPointSize(12)
        self.textBrowser.setFont(font)
        self.textBrowser.setObjectName("textBrowser")
        self.pushButton_4 = QtWidgets.QPushButton(self.centralwidget)
        self.pushButton_4.setGeometry(QtCore.QRect(610, 390, 141, 61))
        font = QtGui.QFont()
        font.setPointSize(15)
        self.pushButton_4.setFont(font)
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
        self.textBrowser.setHtml(_translate("level_3", "<!DOCTYPE HTML PUBLIC \"-//W3C//DTD HTML 4.0//EN\" \"http://www.w3.org/TR/REC-html40/strict.dtd\">\n"
"<html><head><meta name=\"qrichtext\" content=\"1\" /><style type=\"text/css\">\n"
"p, li { white-space: pre-wrap; }\n"
"</style></head><body style=\" font-family:\'MS Shell Dlg 2\'; font-size:12pt; font-weight:400; font-style:normal;\">\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\">    O grupo AMAGGI não faz apenas o consumo de agrotóximos como o Glisofato; eles realizam a venda de produtos para reabiliar o solo e manutenção da plantação. </p>\n"
"<p style=\"-qt-paragraph-type:empty; margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><br /></p>\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\">Prdutos Quimicos utilizados:<br /><span style=\" font-family:\'Ubuntu\',\'Helvetica\',\'Arial\',\'sans-serif\'; font-weight:296; color:#363636; background-color:#ffffff;\">– Hexano</span></p>\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px; line-height:150%; background-color:#ffffff;\"><span style=\" font-family:\'Ubuntu\',\'Helvetica\',\'Arial\',\'sans-serif\'; font-weight:296; color:#363636;\">– Poliuretano</span></p>\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px; line-height:150%; background-color:#ffffff;\"><span style=\" font-family:\'Ubuntu\',\'Helvetica\',\'Arial\',\'sans-serif\'; font-weight:296; color:#363636;\">– Glifosfato</span></p>\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px; line-height:150%; background-color:#ffffff;\"><span style=\" font-family:\'Ubuntu\',\'Helvetica\',\'Arial\',\'sans-serif\'; font-weight:296; color:#363636;\">– Aflatoxina</span></p>\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px; line-height:150%; background-color:#ffffff;\"><span style=\" font-family:\'Ubuntu\',\'Helvetica\',\'Arial\',\'sans-serif\'; font-weight:296; color:#363636;\">– Ácido Clorídrico</span></p>\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px; line-height:150%; background-color:#ffffff;\"><span style=\" font-family:\'Ubuntu\',\'Helvetica\',\'Arial\',\'sans-serif\'; font-weight:296; color:#363636;\">– Álcool Etílico</span></p>\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px; line-height:150%; background-color:#ffffff;\"><span style=\" font-family:\'Ubuntu\',\'Helvetica\',\'Arial\',\'sans-serif\'; font-weight:296; color:#363636;\">– Solução Acetônica</span></p>\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px; line-height:150%; background-color:#ffffff;\"><span style=\" font-family:\'Ubuntu\',\'Helvetica\',\'Arial\',\'sans-serif\'; font-weight:296; color:#363636;\">– Ácido Sulfúrico</span></p>\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px; line-height:150%; background-color:#ffffff;\"><span style=\" font-family:\'Ubuntu\',\'Helvetica\',\'Arial\',\'sans-serif\'; font-weight:296; color:#363636;\">– Eter Petróleo</span></p>\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px; line-height:150%; background-color:#ffffff;\"><span style=\" font-family:\'Ubuntu\',\'Helvetica\',\'Arial\',\'sans-serif\'; font-weight:296; color:#363636;\">– Hidróxido Sódio</span></p>\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px; line-height:150%; background-color:#ffffff;\"><span style=\" font-family:\'Ubuntu\',\'Helvetica\',\'Arial\',\'sans-serif\'; font-weight:296; color:#363636;\">– NO2 Amônia</span></p>\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px; line-height:150%; background-color:#ffffff;\"><span style=\" font-family:\'Ubuntu\',\'Helvetica\',\'Arial\',\'sans-serif\'; font-weight:296; color:#363636;\">– Ácido Sulfonico</span></p>\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px; line-height:150%; background-color:#ffffff;\"><span style=\" font-family:\'Ubuntu\',\'Helvetica\',\'Arial\',\'sans-serif\'; font-weight:296; color:#363636;\">– Hipoclorito Sódio</span></p>\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px; line-height:150%; background-color:#ffffff;\"><span style=\" font-family:\'Ubuntu\',\'Helvetica\',\'Arial\',\'sans-serif\'; font-weight:296; color:#363636;\">– Álcool Metílico</span></p>\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px; line-height:150%; background-color:#ffffff;\"><span style=\" font-family:\'Ubuntu\',\'Helvetica\',\'Arial\',\'sans-serif\'; font-weight:296; color:#363636;\">– Cloreto Trifeniltetra</span></p>\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px; line-height:150%; background-color:#ffffff;\"><span style=\" font-family:\'Ubuntu\',\'Helvetica\',\'Arial\',\'sans-serif\'; font-weight:296; color:#363636;\">– Hidróxido Sódio</span></p>\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px; line-height:150%; background-color:#ffffff;\"><span style=\" font-family:\'Ubuntu\',\'Helvetica\',\'Arial\',\'sans-serif\'; font-weight:296; color:#363636;\">– Iodeto Potássio</span></p></body></html>"))
        self.pushButton_4.setText(_translate("level_3", "SAIR"))
import imgNivel3_rc
