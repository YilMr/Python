from PyQt5 import QtWidgets,QtGui
import sys

def Pencere():
    app = QtWidgets.QApplication(sys.argv)          #uygulama objesi mutlaka şart!



    pencere = QtWidgets.QWidget()                   #pencere oluşturma komutu
    pencere.setWindowTitle("PyQt5 Ders 1")          # pencere başlığı

  


    etiket = QtWidgets.QLabel(pencere)              #pencereye etiket ekleme ve hareket ettirme.
    etiket.setText("Bu Bir etikettir.")
    etiket.move(200,30)


    etiket2 = QtWidgets.QLabel(pencere)
    etiket2.setPixmap(QtGui.QPixmap("Red_Kitten_01.jpg"))          #resim ekledik
    etiket2.move(100,100)


    pencere.setGeometry(100,100,500,500)                           #pencere boyutu ayarlama komutu
    pencere.show()                                                 #pencereyi gösterme komutu
    sys.exit(app.exec())                                           # çarpı tuşuna basana kadar çalışır : anlamına gelen komut





Pencere()






