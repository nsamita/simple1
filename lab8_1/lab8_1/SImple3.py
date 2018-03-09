import sys
from PyQt5.QtCore import *
from PyQt5.QtWidgets import *
from PyQt5.QtGui import *
from lab8_1 import Simple_drawing_window

class Simple_drawing_window3(Simple_drawing_window):
    def __init__(self):
        return super().__init__()

    def paintEvent(self,e):
        p = QPainter()
        p.begin(self)

        p.setPen(QColor(236,113,166))
        p.setBrush(QColor(236,113,166))
        p.drawPie(50,80,100,100,0,360*16)

        p.setPen(QColor(100,91,80))
        p.setBrush(QColor(100,91,80))
        p.drawPie(50,150,100,100,0,360*16)

        p.setPen(QColor(95,225,121))
        p.setBrush(QColor(95,225,121))
        p.drawPie(50,220,100,100,0,360*16)

        p.setPen(QColor(225,177,95))
        p.setBrush(QColor(225,177,95))
        p.drawPolygon(QPoint(50,300), QPoint(150,300), QPoint(100,450))

        p.drawPixmap(QRect(200,100,320,320), self.rabbit)
        p.end()
       
def main():
    app = QApplication(sys.argv)
    w = Simple_drawing_window3()
    w.show()
        
    return app.exec_()
    
if __name__ == "__main__":
    sys.exit(main()) 