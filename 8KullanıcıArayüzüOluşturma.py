from mimetypes import init
import sys
from PyQt5 import QtWidgets
import sqlite3

class Pencere(QtWidgets.QWidget):
    def __init__(self):
        
        super().__init__()
        self.baglanti_olustur()                #veritabınına bağlanmak için fonku tanıttık,sonradna fonku kendimiz tanımlayacağız
        self.init_ui()
    
    def baglanti_olustur(self):
        baglanti = sqlite3.connect("database.db")      #database veritabanı oluşturduk
        self.cursor = baglanti.cursor()                 #cursor ile veritabına işlem yapma komutu ekledik

        self.cursor.execute("Create Table if not exists uyeler (Kullanıcı_adı TEXT,Parola Text)")  #uyeler adlı tablo oluşturduk

        baglanti.commit()      # veritabanını güncelleme komutu

    def init_ui(self):
        self.kullanici_adi = QtWidgets.QLineEdit()
        self.sifre = QtWidgets.QLineEdit()
        self.sifre.setEchoMode(QtWidgets.QLineEdit.Password)         #şifrenin "*******"" şeklinde görülmesini sağlayan komut dizisi
        self.giris = QtWidgets.QPushButton("Giriş Yap")
        self.yazi_alani = QtWidgets.QLabel(" ")

        v_box = QtWidgets.QVBoxLayout()

        v_box.addWidget(self.kullanici_adi)
        v_box.addWidget(self.sifre)
        v_box.addWidget(self.yazi_alani)
        v_box.addStretch()
        v_box.addWidget(self.giris)


        h_box = QtWidgets.QHBoxLayout()
        h_box.addStretch()
        h_box.addLayout(v_box)
        h_box.addStretch()

       
        self.setLayout(h_box)

        self.setWindowTitle("Kullanıcı Girişi ")
        self.giris.clicked.connect(self.login)           #giriş butonuna tıklandığında login fonksiyonu çağırılır.

        self.show()
    
    def login(self):
        adi = self.kullanici_adi.text()                                
        password = self.sifre.text()             #bu 2 değeri databaseye göndermek için aldık

        self.cursor.execute("Select * From uyeler where Kullanıcı_adı = ? and parola = ? ",(adi,password)) 
        data = self.cursor.fetchall()                                                                          
                                                 #2 değeri databasede sorgulattık
        if len(data) == 0 :
            self.yazi_alani.setText("Böyle Bir kullanıcı Yok\nLütfen tekrar Deneyin...")      
        else : 
            self.yazi_alani.setText("Hoşgeldiniz " + adi)   
                                                 #duruma göre çıkış ürettik.


         #login foknsiyonu da kısaca veritabına bağlanıyor ve duruma göre arayüze yazı yazdırıyor.


app = QtWidgets.QApplication(sys.argv)


pencere = Pencere()


sys.exit(app.exec())



