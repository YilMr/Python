import sys
from PyQt5.QtWidgets import QApplication,QCheckBox,QWidget,QLabel,QPushButton,QHBoxLayout,QVBoxLayout


class Pencere(QWidget):
    def __init__(self):
        super().__init__()

        self.init_ui()

    def init_ui(self):
        self.checkbox = QCheckBox("Pyhton'u Seviyor musunuz ?")          #checkbox oluşturma komutu
        self.yazi_alani = QLabel(" ")                                      
        self.buton = QPushButton("Bana Tıkla")              #buton oluşturduk.checkbox işleminden sonra tıklancak fonk çağrılcak

        v_box = QVBoxLayout()

        v_box.addWidget(self.checkbox)
        v_box.addWidget(self.yazi_alani)
        v_box.addWidget(self.buton)

        self.setLayout(v_box)

        self.setWindowTitle("CheckBox")

        #şimdi checkboxa tıklanınca bir şeyler yazdıran fonksiyonu tanımlayacağız..(tabi checkbox'a tıklancak sonra butona basılcak)
        
        self.buton.clicked.connect(lambda : self.click(self.checkbox.isChecked(),self.yazi_alani))

        self.show()

    def click(self,checkbox,yazi_alani):
        if checkbox:                                             #func : checkbox işaretlenince 1.durumu yazdırıyor.
            yazi_alani.setText("Python'u Seviyorsun, Helal.")
        else :                                                   #eğer işaretlenmezse else durumunu yazdırıyor.
            yazi_alani.setText("Niye sevmiyorsun;?")


app = QApplication(sys.argv)

pencere = Pencere()


sys.exit(app.exec())








    
