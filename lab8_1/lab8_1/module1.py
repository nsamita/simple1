import sys
from PyQt5.QtCore import *
from PyQt5.QtWidgets import *
from PyQt5.QtGui import *
from lab8_1 import Simple_drawing_window

class Simple_drawing_window2(Simple_drawing_window):
    def __init__(self):
        QWidget.__init__(self,None)
        self.setWindowTitle("Simple Drawing")
        self.rabbit = QPixmap("images/rabbit.png")

    def paintEvent(self,e):
        p = QPainter()
        p.begin(self)

        p.setPen(QColor(252,158,202))
        p.setBrush(QColor(252,158,202))
        
        
        p.drawPie(50,150,60,60,0,180*16)
        p.drawPie(110,150,60,60,0,180*16)
        p.drawPolygon(
            QPoint(50,180), QPoint(170,180), QPoint(110,280),
            )
        p.drawPixmap(QRect(200,100,320,320), self.rabbit)
        p.end()
       
def main():
    app = QApplication(sys.argv)
    w = Simple_drawing_window2()
    w.show()
        
    return app.exec_()
    
if __name__ == "__main__":
    sys.exit(main()) 