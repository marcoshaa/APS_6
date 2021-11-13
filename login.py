from sqlite3.dbapi2 import Cursor
from PyQt5 import  uic,QtWidgets
import sqlite3

def view_second_screen():
    FristScreen.label_4.setText("")
    user_name = FristScreen.user_name.text()
    password = FristScreen.password.text()
    banco = sqlite3.connect('banco_cad.db') 
    cursor = banco.cursor()
    try:
        cursor.execute("SELECT senha FROM cadastro WHERE login = '{}'".format(user_name))
        senhaBd = cursor.fetchall()
        print(senhaBd[0][0])
        banco.close()
    except:
        print("Erro na autenticação do login!")

    if password == senhaBd[0][0] :
        FristScreen.close()
        SecondScreen.show()

    else :
        FristScreen.label_4.setText("Dados invalidos!")
    
def logout():
    SecondScreen.close()
    FristScreen.show()

def cad():
    FristScreen.close()
    TelaCad.show()

def salveCad():
    cadName = TelaCad.CAD_USER.text()
    cadLogin = TelaCad.CAD_USER2.text()
    cadSenha = TelaCad.CAD_SENHA.text()
    cadSenha2 = TelaCad.CAD_SENHA2.text()
    nAcesso = TelaCad.nAcesso.text()

    if(cadSenha == cadSenha2):
        try:
            banco = sqlite3.connect('banco_cad.db') 
            cursor = banco.cursor()#realiza query no bd
            cursor.execute('CREATE TABLE IF NOT EXISTS cadastro (nome text,login text,senha text,nivel int')
            cursor.execute("INSERT INTO cadastro VALUES('"+cadName+"','"+cadLogin+"','"+cadSenha+","+nAcesso+"')") 

            banco.commit()
            banco.close()

            TelaCad.CAD_INF.setText("CADASTRADO COM SUCESSO")

        except sqlite3.Error as falha:
            print("ERRO AO INSERIR OS DADOS: ",falha)
    else:
        TelaCad.CAD_INF.setText("Senhas divergentes")


        

app=QtWidgets.QApplication([])
FristScreen = uic.loadUi("FristScreen.ui")
TelaCad = uic.loadUi("tela_cad.ui")
FristScreen.enter_Button.clicked.connect(view_second_screen)
FristScreen.cad_Button.clicked.connect(cad)
FristScreen.password.setEchoMode(QtWidgets.QLineEdit.Password)
TelaCad.BUTT_CAD.clicked.connect(salveCad)
level1 = uic.loadUi("level.ui")
level2 = uic.loadUi("level2.ui")
level3 = uic.loadUi("level3.ui")



FristScreen.show()
app.exec()