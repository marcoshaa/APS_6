from PyQt5 import  uic,QtWidgets


def view_second_screen():
    FristScreen.label_4.setText("")
    user_name = FristScreen.user_name.text()
    password = FristScreen.password.text()
    if user_name == "ADM" and password == "adm" :
        FristScreen.close()
        SecondScreen.show()

    else :
        FristScreen.label_4.setText("Dados invalidos!")
    
def logout():
    SecondScreen.close()
    FristScreen.show()


app=QtWidgets.QApplication([])
FristScreen = uic.loadUi("FristScreen.ui")
SecondScreen = uic.loadUi("Second_Screen.ui")

FristScreen.show()
app.exec()