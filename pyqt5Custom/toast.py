#                 PyQt5 Custom Widgets                #
#                GPL 3.0 - Kadir Aksoy                #
#   https://github.com/kadir014/pyqt5-custom-widgets  #


from PyQt5.QtCore    import Qt, pyqtSignal
from PyQt5.QtWidgets import QWidget, QHBoxLayout, QLabel
from PyQt5.QtGui     import QPainter, QPen, QBrush, QColor, QFont

from .animation import Animation, AnimationHandler
from .imagebox import ImageBox
from .styledbutton import StyledButton



class Toast(QWidget):
    def __init__(self, parent, text="", icon=None, closeButton=True):
        super().__init__(parent)

        self.setFixedHeight(45)

        w = self.width()
        h = self.height()
        ww = self.parent().width()
        hh = self.parent().height()
        self.setGeometry(ww/2-w/2, hh-h-5, w, h)

        self.styleDict = {
            "background-color" : (0, 0, 0, 180),
            "border-radius" : 16,

            "font-family" : None,
            "font-size" : 17,
            "color" : (255, 255, 255),

            "font-subpixel-aa" : False
        }

        self._closeButton = closeButton

        self.layout = QHBoxLayout()
        self.layout.setContentsMargins(15, 0, 7, 0)
        self.setLayout(self.layout)

        self.conwdt = QWidget()
        self.conlyt = QHBoxLayout()
        self.conlyt.setContentsMargins(0, 0, 0, 0)
        self.conwdt.setLayout(self.conlyt)
        self.layout.addWidget(self.conwdt, alignment=Qt.AlignLeft)

        self.close_btn = StyledButton("✕")
        self.layout.addWidget(self.close_btn)
        self.close_btn.setFixedSize(self.height()/1.6, self.height()/1.6)
        self.close_btn.setStyleDict({
                "border-color" : (0, 0, 0, 0),
                "background-color" : (0, 0, 0, 0),
                "color" : (255, 255, 255),
                "font-size" : 14,
                "color" : (255, 255, 255, 130),
                "border-radius" : 100,
            })
        self.close_btn.setStyleDict({
                "background-color" : (255, 255, 255, 8),
                "color" : (255, 255, 255, 255)
            }, "hover")
        self.close_btn.setStyleDict({
                "background-color" : (255, 255, 255, 15),
                "color" : (255, 255, 255, 147)
            }, "press")

        self.close_btn.clicked.connect(self.fall)

        self.text = text
        self.textLbl = QLabel(text)
        self.conlyt.addWidget(self.textLbl, alignment=Qt.AlignCenter)

        self._icon = None
        if icon is not None:
            self.setIcon(icon)

        self.risen = False
        self.hide()

        self.anim = AnimationHandler(self, 0, 1, Animation.easeOutQuart)
        self.anim.speed = 1.7

    def __repr__(self):
        return f"<pyqt5Custom.Toast()>"

    def rise(self, duration):
        if self.risen: return

        self.duration = duration
        self.risen = True
        self.anim.start()
        self.show()
        self.raise_()
        self.update()

    def fall(self):
        if not self.risen: return

        self.anim.start(reverse=True)
        self.risen = False
        self.update()

    def setStyleDict(self, styledict):
        for k in styledict:
            self.styleDict[k] = styledict[k]

    def setIcon(self, icon):
        if self._icon is not None:
            self._icon.deleteLater()

        if isinstance(icon, str):
            self._icon = ImageBox(icon)
            self._icon.setFixedSize(18, 18)
            if self.text:
                self.conlyt.insertWidget(0, self._icon, alignment=Qt.AlignVCenter|Qt.AlignRight)
                self.conlyt.removeItem(self.conlyt.itemAt(1))
                self.conlyt.addWidget(self.textLbl, alignment=Qt.AlignVCenter|Qt.AlignLeft)
            else:
                self.conlyt.insertWidget(0, self._icon, alignment=Qt.AlignRight)

        else:
            self._icon = icon
            self._icon.setFixedSize(18, 18)
            if self.text:
                self.conlyt.insertWidget(0, self._icon, alignment=Qt.AlignVCenter|Qt.AlignRight)
                self.conlyt.removeItem(self.conlyt.itemAt(1))
                self.conlyt.addWidget(self.textLbl, alignment=Qt.AlignVCenter|Qt.AlignLeft)

            else:
                self.conlyt.insertWidget(0, self._icon, alignment=Qt.AlignCenter)

    def setIconSize(self, width, height):
        self._icon.setFixedSize(width, height)

    def setText(self, text):
        self.textLbl.setText(text)

    def resizeEvent(self, event):
        w = self.width()
        h = self.height()
        ww = self.parent().width()
        hh = self.parent().height()
        self.setGeometry(ww/2-w/2, hh-h-5, w, h)

    def update(self):
        self.anim.update()
        super().update()

    def paintEvent(self, event):
        pt = QPainter()
        pt.begin(self)
        pt.setRenderHint(QPainter.Antialiasing, on=True)

        plt = self.textLbl.palette()
        plt.setColor(self.textLbl.foregroundRole(), QColor(*self.styleDict["color"]))
        self.textLbl.setPalette(plt)

        fnt = self.textLbl.font()
        fnt.setPixelSize(self.styleDict["font-size"])
        if not self.styleDict["font-subpixel-aa"]: fnt.setStyleStrategy(QFont.NoSubpixelAntialias)
        if self.styleDict["font-family"]: fnt.setFamily(self.styleDict["font-family"])
        self.textLbl.setFont(fnt)

        pt.setPen(QPen(QColor(0, 0, 0, 0)))
        pt.setBrush(QBrush(QColor(*self.styleDict["background-color"])))
        r = self.styleDict["border-radius"]
        if r > self.height() / 2: r = self.height() / 2

        pt.drawRoundedRect(0, 0, self.width(), self.height(), r, r)

        pt.end()

        if not self.anim.done():
            w = self.width()
            h = self.height()
            ww = self.parent().width()
            hh = self.parent().height()

            self.setGeometry(ww/2-w/2, hh-(self.anim.current()*(h+5))-0.01, w, h)
            #print((self.anim.current()*h))

        if not self.anim.done(): self.update()
        else:
            if self.isVisible() and not self.risen: self.hide()
