#                 PyQt5 Custom Widgets                #
#                GPL 3.0 - Kadir Aksoy                #
#   https://github.com/kadir014/pyqt5-custom-widgets  #


import random

from PyQt5.QtCore    import Qt, QRect, pyqtSignal
from PyQt5.QtWidgets import QWidget, QHBoxLayout, QVBoxLayout, QLabel, QGraphicsDropShadowEffect
from PyQt5.QtGui     import QColor, QPainter, QPen, QBrush

from .animation import Animation, AnimationHandler
from .styledbutton import StyledButton


class EmbedWindow(QWidget):

    closed = pyqtSignal()

    def __init__(self, parent, pos=None, title="New window"):
        super().__init__(parent)

        if pos is None:
            pos = (random.randint(0, self.parent().width()-285), random.randint(0, self.parent().height()-190))
        self.setFixedSize(285, 190)
        self.setGeometry(pos[0], pos[1], 285, 190)

        self.shadow = QGraphicsDropShadowEffect(self)
        self.shadow.setBlurRadius(8)
        self.shadow.setColor(QColor(0, 0, 0, 110))
        self.shadow.setOffset(0, 2)
        self.setGraphicsEffect(self.shadow)

        self.borderRadius = 12
        self.headerColor = QColor(255, 255, 255)
        self.headerHeight = 36

        self.pressed = None
        self.pressed_pos = None

        self.layout = QVBoxLayout()
        self.layout.setContentsMargins(0, 0, 0, 0)
        self.layout.setAlignment(Qt.AlignTop)
        self.setLayout(self.layout)

        self.header = QWidget()
        self.header.setFixedHeight(self.headerHeight)
        self.header_lyt = QHBoxLayout()
        self.header_lyt.setContentsMargins(0, 0, 0, 0)
        self.header_lyt.setSpacing(0)
        self.header.setLayout(self.header_lyt)

        self.contentwdt = QWidget()
        self.content = QVBoxLayout()
        self.contentwdt.setLayout(self.content)
        self.content_visible = True
        self.last_height = self.height()

        self.layout.addWidget(self.header)
        self.layout.addWidget(self.contentwdt)

        self.title = QLabel(title)
        self.title.setStyleSheet("color:black; font-size:14px;")

        self.close_btn = StyledButton("✕")
        self.close_btn.setFixedSize(self.headerHeight, self.headerHeight)
        self.close_btn.setStyleDict({
                "border-color" : (0, 0, 0, 0),
                "border-radius" : 50
            })

        @self.close_btn.clicked.connect
        def slot():
            self.close()
            self.closed.emit()

        self.deta_btn = StyledButton("▲")
        self.deta_btn.setFixedSize(self.headerHeight, self.headerHeight)
        self.deta_btn.setStyleDict({
                "border-color" : (0, 0, 0, 0),
                "border-radius" : 50
            })

        @self.deta_btn.clicked.connect
        def slot():
            if self.content_visible:
                self.content_visible = False
                self.contentwdt.hide()
                self.last_height = self.height()
                self.deta_btn.textLbl.setText("▼")
                self.anim.start(reverse=True)

            else:
                self.content_visible = True
                self.contentwdt.show()
                self.deta_btn.textLbl.setText("▲")
                self.anim.start()

        self.header_lyt.addSpacing(10)
        self.header_lyt.addWidget(self.title, alignment=Qt.AlignVCenter)
        self.header_lyt.addWidget(self.deta_btn, alignment=Qt.AlignVCenter|Qt.AlignRight)
        self.header_lyt.addWidget(self.close_btn, alignment=Qt.AlignVCenter)

        self.anim = AnimationHandler(self, 0, 1, Animation.easeOutSine)
        self.anim.interval = 10/1000
        self.anim.value = 1

    def __repr__(self):
        return f"<pyqt5Custom.EmbedWindow(parent={self.parent()})>"

    def setTitle(text):
        self.title.setText(text)

    def title(self):
        return self.title.text()

    def setControlsVisible(b):
        if not b:
            self.close_btn.hide()
            self.deta_btn.hide()

        else:
            self.close_btn.show()
            self.deta_btn.show()

    def update(self, *args, **kwargs):
        self.anim.update()
        super().update(*args, **kwargs)

    def mousePressEvent(self, event):
        self.startpos = self.pos()
        self.__mousePressPos = None
        self.__mouseMovePos = None
        if event.button() == Qt.LeftButton:
            self.__mousePressPos = event.globalPos()
            self.__mouseMovePos = event.globalPos()

    def mouseMoveEvent(self, event):
        if event.buttons() == Qt.LeftButton and event.y() <= self.headerHeight:
            currPos = self.mapToGlobal(self.pos())
            globalPos = event.globalPos()
            diff = globalPos - self.__mouseMovePos
            newPos = self.mapFromGlobal(currPos + diff)
            self.move(newPos)

            self.__mouseMovePos = globalPos

            self.raise_()

    def mouseReleaseEvent(self, event):
        if self.__mousePressPos is not None:
            moved = event.globalPos() - self.__mousePressPos
            if moved.manhattanLength() > 3:
                event.ignore()
                return

    def paintEvent(self, event):
        pt = QPainter()
        pt.begin(self)
        pt.setRenderHint(QPainter.Antialiasing, on=True)

        pen = QPen(QColor(0, 0, 0, 0), 1)
        brush = QBrush(QColor(255, 255, 255))
        pt.setBrush(brush)
        pt.setPen(pen)

        self.setFixedHeight(((self.last_height-36)*self.anim.current())+36)
        pt.drawRoundedRect(0, 0, self.width(), self.height()*self.anim.current(), self.borderRadius, self.borderRadius)

        brush = QBrush(self.headerColor)
        pt.setBrush(brush)

        pt.drawRoundedRect(0, 0, self.width(), self.headerHeight, self.borderRadius, self.borderRadius)
        if self.content_visible:
            pt.drawRect(0, self.headerHeight/2, self.width()*2, self.headerHeight/2)

        pt.end()
        self.show()

        if not self.anim.done(): self.update()
