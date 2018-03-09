import sys
from PyQt5.QtCore import *
from PyQt5.QtWidgets import *
from PyQt5.QtGui import *
from PyQt5.QtMultimedia import QSound
import random

class Animation_area(QWidget):
    def __init__(self):
        QWidget.__init__(self, None)
        self.setMinimumSize(500, 500)

        self.arena_w = 500
        self.arena_h = 500
        self.lastMouseX = 0
        self.lastMouseY = 0
        self.mouseX = 0
        self.mouseY = 0
        self.myPenWidth = 5
        self.myPenColor = Qt.black
        imageSize = QSize(500, 500)
        self.image = QImage(imageSize, QImage.Format_RGB32)
        self.lastPoint = QPoint()
        self.clearImage()

    def drawLineTo(self, endPoint):
        painter = QPainter(self.image)
        painter.setPen(QPen(self.myPenColor, self.myPenWidth,
                                  Qt.SolidLine, Qt.RoundCap,Qt.RoundJoin))
        painter.drawLine(self.lastPoint, endPoint)
        self.update()
        self.lastPoint = QPoint(endPoint)

    def mousePressEvent(self, event):
            self.lastPoint = event.pos()


    def mouseMoveEvent(self, event):
            self.drawLineTo(event.pos())

    def mouseReleaseEvent(self, event):
            self.drawLineTo(event.pos())

    def paintEvent(self, event):
        painter = QPainter(self)
        painter.drawImage(event.rect(), self.image)



    def update_value(self):
        self.update()

    def clearImage(self):
        self.image.fill(qRgb(255, 255, 255))
        self.modified = True
        self.update()


class Simple_animation_window(QWidget):
    def __init__(self):
        QWidget.__init__(self, None)

        self.anim_area = Animation_area()

        layout = QVBoxLayout()
        layout.addWidget(self.anim_area)

        self.label = QLabel("Drag the mouse to draw")
        self.button = QPushButton("Clear")
        self.button.clicked.connect(self.clear_screen)

        layout.addWidget(self.label)
        layout.addWidget(self.button)

        self.setLayout(layout)
        self.setMinimumSize(530, 600)

    def clear_screen(self):
        self.anim_area.clearImage()

def main():
    app = QApplication(sys.argv)
    w = Simple_animation_window()
    w.show()

    return app.exec_()

if __name__ == '__main__':
    sys.exit(main())