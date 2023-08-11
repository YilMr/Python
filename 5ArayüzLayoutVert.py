import sys
from PyQt5 import QtWidgets,QtGui



def Pencere():
    app = QtWidgets.QApplication(sys.argv)   

    okay = QtWidgets.QPushButton("Tamam")
    cancel = QtWidgets.QPushButton("İptal")             

    v_box = QtWidgets.QVBoxLayout()                      #Vertical yani Dikey layout oluşturma komutu

    v_box.addWidget(okay)
    v_box.addStretch()                                   # tamam ve iptal arasına boşluk atma komutu
    v_box.addWidget(cancel)

    pencere =QtWidgets.QWidget()
    pencere.setWindowTitle("PyQt5 Ders 2")

    pencere.setLayout(v_box)                              #oluşturduğumuz buton layoutlarını pencereye yükleme komutu


    pencere.setGeometry(100,100,500,500)
    pencere.show()
    sys.exit(app.exec())

Pencere()


