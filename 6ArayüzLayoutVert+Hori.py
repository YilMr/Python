import sys
from PyQt5 import QtWidgets,QtGui



def Pencere():
    app = QtWidgets.QApplication(sys.argv)   

    okay = QtWidgets.QPushButton("Tamam")
    cancel = QtWidgets.QPushButton("İptal")             

    h_box = QtWidgets.QHBoxLayout()
    h_box.addStretch()
                                                                    # Tüm kodun özeti olarak ilk olarak horizontal kod yazdık
                                                                    # devamında horizontalda tanımlı olanları verticala 
                                                                    #vertical ve horizontal birleşti sağ alta tamam iptal eklendi.
    h_box.addWidget(okay)
    h_box.addWidget(cancel)

    v_box = QtWidgets.QVBoxLayout()
    v_box.addStretch()
    v_box.addLayout(h_box)
    
    pencere =QtWidgets.QWidget()
    pencere.setWindowTitle("PyQt5 Ders 2")

    pencere.setLayout(v_box)                              #oluşturduğumuz buton layoutlarını pencereye yükleme komutu


    pencere.setGeometry(100,100,500,500)
    pencere.show()
    sys.exit(app.exec())

Pencere()


