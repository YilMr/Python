import sys
from PyQt5 import QtWidgets


class Pencere(QtWidgets.QWidget):                                                #sıfırdan class oluşturup o classa fonk yükleyipöyle çağırdık..
    def __init__(self) -> None:
        super().__init__()

        self.init_ui()

    def init_ui(self):
        self.yazı_alanı = QtWidgets.QLabel("Bana Henüz Tıklanmadı...")
        self.buton = QtWidgets.QPushButton("Bana Tıkla...")
        self.say = 0

        v_box = QtWidgets.QVBoxLayout()
        v_box.addWidget(self.buton)
        v_box.addWidget(self.yazı_alanı)
        v_box.addStretch()
                                                            #bildiğimiz layout komutları felan
        h_box = QtWidgets.QHBoxLayout()
        h_box.addStretch()
        h_box.addLayout(v_box)
        h_box.addStretch()

        self.setLayout(h_box)


        self.buton.clicked.connect(self.click)                #Butona basıldığında self.click adlı fonksiyonu çağırdık..

        self.show()


    def click(self):                                     #click fonksiyonunu tanımdaladık..
        self.say += 1
        self.yazı_alanı.setText("Bana " +  str(self.say) +   " Defa Tıklandı..")



app = QtWidgets.QApplication(sys.argv)

pencere = Pencere()

sys.exit(app.exec())





