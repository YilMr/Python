from PyQt5 import QtWidgets,QtGui
import sys

  
def Pencere():
    app = QtWidgets.QApplication(sys.argv)                        #uygulama objesi mutlaka şart!
    pencere =QtWidgets.QWidget()
    pencere.setWindowTitle("PyQt5 Ders 2")


    buton = QtWidgets.QPushButton(pencere)
    buton.setText("Bu Bir Butondur")
    buton.move(190,30)

    etiket = QtWidgets.QLabel(pencere)
    etiket.setText("Hello")
    etiket.move(200,80)

    pencere.setGeometry(100,100,500,500)
    pencere.show()
    sys.exit(app.exec())


Pencere()






