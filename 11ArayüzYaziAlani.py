import sys

from PyQt5.QtWidgets  import QApplication,QWidget,QTextEdit,QVBoxLayout,QHBoxLayout,QPushButton,QLabel


class Pencere(QWidget):
    def __init__(self):
        super().__init__()

        self.init_ui()

    def init_ui(self):

        self.yazi_alani = QTextEdit()             #geniş bir yazı alanı oluşturduk...

        self.temizle = QPushButton("Temizle")

        v_box = QVBoxLayout()

        v_box.addWidget(self.yazi_alani)
        v_box.addWidget(self.temizle)

        self.setWindowTitle("Yazı Alanı")            
        
        self.setLayout(v_box)

        self.temizle.clicked.connect(self.click)       #temizleye tıklandığında click fonku çağrılcak.
                    
        self.show()

    def click(self):
        self.yazi_alani.clear()
        
app = QApplication(sys.argv)


pencere = Pencere()


sys.exit(app.exec())


