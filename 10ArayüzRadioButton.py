import sys
from PyQt5.QtWidgets import QApplication,QRadioButton,QWidget,QLabel,QPushButton,QHBoxLayout,QVBoxLayout


class Pencere(QWidget):
    def __init__(self):
        super().__init__()

        self.init_ui()

    def init_ui(self):
        
        self.radio_yazisi = QLabel("Hangi Dili veya Dilleri Konuşabiliyorsun ?")
        
        self.java = QRadioButton("Java")
        self.python = QRadioButton("Python")           #radiobuton tanımlama ve aşağısında layouta ekleme.
        self.php =QRadioButton("PhP")


        self.yazi_alani = QLabel(" ")

        self.buton = QPushButton("Gönder")

        v_box = QVBoxLayout()
        v_box.addWidget(self.radio_yazisi)
        v_box.addWidget(self.java)
        v_box.addWidget(self.php)
        v_box.addWidget(self.python)
        v_box.addStretch()
        v_box.addWidget(self.yazi_alani)
        v_box.addWidget(self.buton)


        self.setLayout(v_box)

        self.setWindowTitle("Radio Button")              #aşağıda radiobuton işaretlendiğinde çağılcak fonksiyon yüklendi."click fonksiyonu"
        self.buton.clicked.connect(lambda : self.click(self.java.isChecked(),self.php.isChecked(),self.python.isChecked(),self.yazi_alani))
        self.show()

    def click(self,java,php,python,yazi_alani):                #hangisine tıklarsak onun çıkışında oluşcak yazıları tanımladık.
        if java:
            yazi_alani.setText("Java Konuşabiliyorsun.")
        elif php:
            yazi_alani.setText("PhP Konuşabiliyorsun.")
        else:
            yazi_alani.setText("Python Konuşabiliyorsun.")
                    
app = QApplication(sys.argv)

pencere = Pencere()


sys.exit(app.exec())


