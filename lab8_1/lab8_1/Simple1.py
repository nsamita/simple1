import sys
from PyQt5.QtCore import *
from PyQt5.QtWidgets import *
from PyQt5.QtGui import *


class Simple_drawing_window(QWidget):
    def __init__(self):
        QWidget.__init__(self,None)
        self.setWindowTitle("Simple Drawing")
        self.rabbit = QPixmap("images/rabbit.png")

    def paintEvent(self,e):
        p = QPainter()
        p.begin(self)
        p.setPen(QColor(255,255,0))
        p.setBrush(QColor(255,255,0))
        p.drawPie(50,150,100,100,0,360*16)
       
        p.drawPixmap(QRect(200,100,320,320), self.rabbit)
        p.end()

       
def main():
    app = QApplication(sys.argv)
    w = Simple_drawing_window()
    w.show()
        
    return app.exec_()
    
if __name__ == "__main__":
    sys.exit(main()) 