import sys
from PyQt5 import QtWidgets,QtGui



def Pencere():
    app = QtWidgets.QApplication(sys.argv)   

    okay = QtWidgets.QPushButton("Tamam")
    cancel = QtWidgets.QPushButton("İptal")

    h_box = QtWidgets.QHBoxLayout()

    h_box.addWidget(okay)
    h_box.addStretch()
    h_box.addWidget(cancel)

    pencere =QtWidgets.QWidget()
    pencere.setWindowTitle("PyQt5 Ders 2")

    pencere.setLayout(h_box)


    pencere.setGeometry(100,100,500,500)
    pencere.show()
    sys.exit(app.exec())

Pencere()





