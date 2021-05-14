#                 PyQt5 Custom Widgets                #
#                GPL 3.0 - Kadir Aksoy                #
#   https://github.com/kadir014/pyqt5-custom-widgets  #


from PyQt5.QtCore    import Qt, QEvent, pyqtSignal
from PyQt5.QtWidgets import QWidget, QGraphicsOpacityEffect
from PyQt5.QtGui     import QColor, QPainter, QPen, QBrush

from .animation import Animation, AnimationHandler



class ToggleSwitch(QWidget):

    defaultStyles = ("win10", "ios", "android")

    toggled = pyqtSignal()

    def __init__(self, text="", style="win10", on=False):
        super().__init__()

        self.text = text

        self.on = on

        # TODO: find a better way for opacity
        self.opacity = QGraphicsOpacityEffect(self)
        self.opacity.setOpacity(1)
        self.setGraphicsEffect(self.opacity)

        if style not in ToggleSwitch.defaultStyles:
            raise Exception(f"'{style}' is not a default style.")
        self.style = style


        if self.style == "win10":
            self.onColor  = QColor(0, 116, 208)
            self.offColor = QColor(0, 0, 0)

            self.handleAlpha = True
            self.handleColor = QColor(255, 255, 255)

            self.width = 35
            self.radius = 26

        elif self.style == "ios":
            self.onColor  = QColor(73, 208, 96)
            self.offColor = QColor(250, 250, 250)

            self.handleAlpha = False
            self.handleColor = QColor(255, 255, 255)

            self.width = 21
            self.radius = 29

        elif self.style == "android":
            self.onColor  = QColor(0, 150, 136)
            self.offColor = QColor(255, 255, 255)

            self.handleAlpha = True
            self.handleColor = QColor(255, 255, 255)

            self.width = 35
            self.radius = 26

        self.setMinimumSize(self.width + (self.radius*2) + (len(self.text)*10), self.radius+2)

        self.anim = AnimationHandler(self, 0, self.width, Animation.easeOutCirc)
        if self.on: self.anim.value = 1

    def __repr__(self):
        return f"<pyqt5Custom.ToggleSwitch(isToggled={self.isToggled()})>"

    def isToggled(self):
        return self.on

    def desaturate(self, color):
        cc = getattr(self, color)
        h = cc.hue()
        if h < 0: h = 0
        s = cc.saturation()//4
        if s > 255: s = 255
        c = QColor.fromHsv(h, s, cc.value())
        setattr(self, color, c)

    def saturate(self, color):
        cc = getattr(self, color)
        h = cc.hue()
        if h < 0: h = 0
        s = cc.saturation()*4
        if s > 255: s = 255
        c = QColor.fromHsv(h, s, cc.value())
        setattr(self, color, c)

    def update(self, *args, **kwargs):
        self.anim.update()
        super().update(*args, **kwargs)

    def mousePressEvent(self, event):
        if self.isEnabled():
            if self.on:
                self.on = False
                self.anim.start(reverse=True)
            else:
                self.on = True
                self.anim.start()
            self.update()

            self.toggled.emit()

    def changeEvent(self, event):
        if event.type() == QEvent.EnabledChange:
            if self.isEnabled():
                self.saturate("onColor")
                self.saturate("offColor")
                self.saturate("handleColor")
                self.opacity.setOpacity(1.00)
            else:
                self.desaturate("onColor")
                self.desaturate("offColor")
                self.desaturate("handleColor")
                self.opacity.setOpacity(0.4)

            self.update()

        else:
            super().changeEvent(event)

    def paintEvent(self, event):
        pt = QPainter()
        pt.begin(self)
        pt.setRenderHint(QPainter.Antialiasing)

        if self.style == "win10":

            if self.on:
                pen = QPen(self.onColor, 1, Qt.SolidLine, Qt.RoundCap, Qt.RoundJoin)
                pt.setPen(pen)
                brush = QBrush(self.onColor)
                pt.setBrush(brush)


                r = self.radius
                w = self.width

                pt.drawChord(r, 1, r, r, 90*16, 180*16)
                pt.drawChord(r+w, 1, r, r, -90*16, 180*16)
                pt.drawRect(r+r//2, 1, w, r)

                if self.handleAlpha: pt.setBrush(pt.background())
                else: pt.setBrush(QBrush(self.handleColor))
                offset = r*0.4
                pt.drawEllipse(r+offset/2+self.anim.current() , 1+offset/2 , r-offset , r-offset)

            else:
                pen = QPen(self.offColor, 1, Qt.SolidLine, Qt.RoundCap, Qt.RoundJoin)
                pt.setPen(pen)

                r = self.radius
                w = self.width

                pt.drawArc(r, 1, r, r, 90*16, 180*16)
                pt.drawArc(r+w, 1, r, r, -90*16, 180*16)
                pt.drawLine(r+r//2, 1, r+w+r//2, 1)
                pt.drawLine(r+r//2, r+1, r+w+r//2, r+1)

                brush = QBrush(self.offColor)
                pt.setBrush(brush)
                offset = r*0.4
                pt.drawEllipse(r+offset/2+self.anim.current() , offset/2+1 , r-offset , r-offset)

        elif self.style == "ios":

            if self.on:
                pen = QPen(self.onColor, 1, Qt.SolidLine, Qt.RoundCap, Qt.RoundJoin)
                pt.setPen(pen)
                brush = QBrush(self.onColor)
                pt.setBrush(brush)

                r = self.radius
                w = self.width

                pt.drawChord(r, 1, r, r, 90*16, 180*16)
                pt.drawChord(r+w, 1, r, r, -90*16, 180*16)
                pt.drawRect(r+r//2, 1, w, r)

                if self.handleAlpha: pt.setBrush(pt.background())
                else: pt.setBrush(QBrush(self.handleColor))
                offset = r*0.025
                pt.drawEllipse(r+offset/2+self.anim.current() , 1+offset/2 , r-offset , r-offset)

            else:
                pen = QPen(self.offColor.darker(135), 1, Qt.SolidLine, Qt.RoundCap, Qt.RoundJoin)
                pt.setPen(pen)
                brush = QBrush(self.offColor)
                pt.setBrush(brush)

                r = self.radius
                w = self.width

                pt.drawChord(r, 1, r, r, 90*16, 180*16)
                pt.drawChord(r+w, 1, r, r, -90*16, 180*16)
                pt.drawRect(r+r//2, 1, w, r)
                pt.setPen(QPen(self.offColor))
                pt.drawRect(r+r//2-2, 2, w+4, r-2)

                if self.handleAlpha: pt.setBrush(pt.background())
                else: pt.setBrush(QBrush(self.handleColor))
                pt.setPen(QPen(self.handleColor.darker(160)))
                offset = r*0.025
                pt.drawEllipse(r+offset/2+self.anim.current() , 1+offset/2 , r-offset , r-offset)

        elif self.style == "android":

            if self.on:
                pen = QPen(self.onColor.lighter(145), 1, Qt.SolidLine, Qt.RoundCap, Qt.RoundJoin)
                pt.setPen(pen)
                brush = QBrush(self.onColor.lighter(145))
                pt.setBrush(brush)

                r = self.radius
                w = self.width

                pt.drawChord(r+r//4, 1+r//4, r//2, r//2, 90*16, 180*16)
                pt.drawChord(r+w+r//4, 1+r//4, r//2, r//2, -90*16, 180*16)
                pt.drawRect(r+r//2, 1+r//4, w, r//2)

                pt.setBrush(QBrush(self.onColor))
                pt.setPen(QPen(self.onColor))
                pt.drawEllipse(r+self.anim.current(), 1 , r, r)

            else:
                pen = QPen(self.offColor.darker(130), 1, Qt.SolidLine, Qt.RoundCap, Qt.RoundJoin)
                pt.setPen(pen)
                brush = QBrush(self.offColor.darker(130))
                pt.setBrush(brush)

                r = self.radius
                w = self.width

                pt.drawChord(r+r//4, 1+r//4, r//2, r//2, 90*16, 180*16)
                pt.drawChord(r+w+r//4, 1+r//4, r//2, r//2, -90*16, 180*16)
                pt.drawRect(r+r//2, 1+r//4, w, r//2)

                pt.setBrush(QBrush(self.offColor))
                pt.setPen(QPen(self.offColor.darker(140)))
                pt.drawEllipse(r+self.anim.current(), 1 , r, r)

        font = pt.font()
        pt.setFont(font)
        pt.setPen(QPen(Qt.black))

        pt.drawText(w+r*2+10, r//2+r//4, self.text)

        pt.end()

        if not self.anim.done(): self.update()
