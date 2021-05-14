#                 PyQt5 Custom Widgets                #
#                GPL 3.0 - Kadir Aksoy                #
#   https://github.com/kadir014/pyqt5-custom-widgets  #


import time
from math import sin, cos, radians

from PyQt5.QtCore    import Qt, pyqtSignal
from PyQt5.QtWidgets import QWidget, QHBoxLayout
from PyQt5.QtGui     import QPainter, QPen

from .animation import Animation, AnimationHandler



class Spinner(QWidget):
    def __init__(self, width, color):
        super().__init__()

        self.w = width
        self.color = color

        self.angle = 0
        self.speed = 4.8

        self.animType = 1

        self.play = True

        self.last_call = time.time()

    def __repr__(self):
        return f"<pyqt5Custom.Spinner()>"

    def paintEvent(self, event):
        pt = QPainter()
        pt.begin(self)
        pt.setRenderHint(QPainter.Antialiasing, on=True)

        w = self.w
        pen = QPen(self.color, w)
        pt.setPen(pen)

        if self.animType == 0:
            pt.drawArc(w, w, self.width()-w*2, self.height()-w*2, self.angle, 90*16)

        elif self.animType == 1:
            sa = ((sin(radians(self.angle/16))+1)/2)*(180*16) + ((sin(radians((self.angle/16)+130))+1)/2)*(180*16)
            pt.drawArc(w, w, self.width()-w*2, self.height()-w*2, self.angle, sa)

        pt.end()

        ep = (time.time()-self.last_call)*1000
        self.last_call = time.time()

        self.angle += self.speed*ep
        if self.angle > 360*16:
            self.angle = 0

        elif self.angle < 0:
            self.angle = 360*16

        if self.play: self.update()
