#                 PyQt5 Custom Widgets                #
#                GPL 3.0 - Kadir Aksoy                #
#   https://github.com/kadir014/pyqt5-custom-widgets  #


import time
from math import sqrt, atan2, pow, pi

from PyQt5.QtCore    import Qt, pyqtSignal
from PyQt5.QtWidgets import QWidget, QVBoxLayout, QLabel
from PyQt5.QtGui     import QColor, QPainter, QPen, QBrush



class ColorPreview(QWidget):
    def __init__(self):
        super().__init__()

        self.color = QColor(0, 0, 0)

        self.layout = QVBoxLayout()
        self.setLayout(self.layout)
        self.label = QLabel("#000000")
        self.layout.addWidget(self.label, alignment=Qt.AlignBottom|Qt.AlignHCenter)

        self.setFixedSize(90, 65)

    def __repr__(self):
        return f"<pyqt5Custom.ColorPreview()>"

    def setColor(self, color):
        self.color = color
        self.label.setText(self.color.name())

    def paintEvent(self, event):
        pt = QPainter()
        pt.begin(self)
        pt.setRenderHint(QPainter.Antialiasing, on=True)

        pt.setPen(QPen(QColor(0, 0, 0, 0)))
        pt.setBrush(QBrush(QColor(225, 225, 225)))

        pt.drawRoundedRect(0, 0, self.width(), self.height(), 9, 9)

        pt.setBrush(QBrush(self.color))

        pt.drawRoundedRect(15, 15, self.width()-30, self.height()-45, 4, 4)

        pt.end()


# TODO: Complete optimized color wheel & picker are and cursor
class ColorPicker(QWidget):

    colorChanged = pyqtSignal(QColor)

    def __init__(self):
        super().__init__()

        self.color = None

        self.radius = 110
        self.setFixedSize(self.radius*2, self.radius*2)

        self.mouse_x, self.mouse_y = 0, 0

    def __repr__(self):
        return f"<pyqt5Custom.ColorPicker()>"

    def mouseMoveEvent(self, event):
        self.mouse_x, self.mouse_y = event.x(), event.y()

        dist = sqrt(pow(self.mouse_x-self.radius, 2)+pow(self.mouse_y-self.radius, 2))

    def paintEvent(self, event):
        pt = QPainter()
        pt.begin(self)
        pt.setRenderHint(QPainter.Antialiasing, on=True)

        for i in range(self.width()):
            for j in range(self.height()):
                color = QColor(255, 255, 255, 255)
                h = (atan2(i-self.radius, j-self.radius)+pi)/(2.*pi)
                s = sqrt(pow(i-self.radius, 2)+pow(j-self.radius, 2))/self.radius
                v = 1.0

                rr = 0.65

                ww = self.width()/(rr*5.72)
                hh = self.height()/(rr*5.72)

                if rr < s < 1.0:
                    color.setHsvF(h, s, v, 1.0)
                    pt.setPen(color)
                    pt.drawPoint(i, j)

                elif ww < i < self.width()-ww and hh < j < self.height()-hh:
                    h = 0.8
                    s = (i - ww) / (self.width()-ww*2)
                    v = 1-((j - hh) / (self.height()-hh*2))

                    hh = int(h*360)
                    ss = int(s*255)
                    vv = int(v*255)
                    color.setHsv(hh, ss, vv)
                    pt.setPen(color)
                    pt.drawPoint(i, j)

        pt.end()
