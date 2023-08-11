import sys
from PyQt5 import QtWidgets



class Pencere(QtWidgets.QWidget):
    def __init__(self):
        super().__init__()

        self.init_ui()

    def init_ui(self):

        self.yazi_alani = QtWidgets.QLineEdit()
        self.temizle = QtWidgets.QPushButton("Temizle")
        self.yazdir = QtWidgets.QPushButton("Yazdir")

        v_box = QtWidgets.QVBoxLayout()

        v_box.addWidget(self.yazi_alani)
        v_box.addWidget(self.temizle)
        v_box.addWidget(self.yazdir)
        v_box.addStretch()

        self.setLayout(v_box)


        self.temizle.clicked.connect(self.click)                              #tıklandığında click func'unu çağırıyor.
        self.yazdir.clicked.connect(self.click) 

        self.show()
    
    def click(self):
        sender = self.sender()                            #hangi butona basıldığını anlıyor..

        if (sender.text() == "Temizle") :
            self.yazi_alani.clear()                          # yazı alanını siliyor,temizliyor.
        else :
           print(self.yazi_alani.text())                      #yazı alanının textini yazdır! demek bu satır.


app = QtWidgets.QApplication(sys.argv)

pencere = Pencere()

sys.exit(app.exec())

        