#                 PyQt5 Custom Widgets                #
#                GPL 3.0 - Kadir Aksoy                #
#   https://github.com/kadir014/pyqt5-custom-widgets  #


from PyQt5.QtCore    import Qt
from PyQt5.QtWidgets import QApplication, QWidget, QHBoxLayout, QLabel
from PyQt5.QtGui     import QColor, QPainter, QPen, QBrush, QFont

from .animation import Animation, AnimationHandler
from .styledbutton import StyledButton



class TitleBar(QWidget):
    def __init__(self, parent, title=""):
        super().__init__(parent)

        self.parent().setWindowTitle(title)
        self.parent().setWindowFlags(Qt.FramelessWindowHint)

        setattr(self.parent(), "mousePressEvent",   self.parentMousePressEvent)
        setattr(self.parent(), "mouseMoveEvent",    self.parentMouseMoveEvent)
        setattr(self.parent(), "mouseReleaseEvent", self.parentMouseReleaseEvent)

        self._resizable = True

        self.setFixedHeight(32)

        self.styleDict = {
                "background-color" : (255, 255, 255),

                "font-family" : None,
                "font-size"   : 12,
                "font-weight" : "regular",
                "color"       : (0, 0, 0),

                "render-aa"        : True,
                "font-subpixel-aa" : False
            }

        self.layout = QHBoxLayout()
        self.layout.setContentsMargins(14, 0, 0, 0)
        self.layout.setSpacing(0)
        self.setLayout(self.layout)

        self.title_lbl = QLabel(title)
        self.layout.addWidget(self.title_lbl)

        self.closeButton = StyledButton(text="✕")
        self.closeButton.setFixedSize(self.height()+19, self.height())

        self.maxButton = StyledButton(text="🗖")
        self.maxButton.setFixedSize(self.height()+19, self.height())

        self.minButton = StyledButton(text="🗕")
        self.minButton.setFixedSize(self.height()+19, self.height())

        self._styleControlButtons()

        self.closeButton.clicked.connect(self.parent().close)

        self.minButton.clicked.connect(self.parent().showMinimized)

        @self.maxButton.clicked.connect
        def slot():
            if self.parent().isMaximized():
                self.parent().showNormal()
            else:
                self.parent().showMaximized()

        self.layout.addWidget(self.minButton, alignment=Qt.AlignRight)
        self.layout.addWidget(self.maxButton)
        self.layout.addWidget(self.closeButton)

        self.pressing = False

        self.cursize = 9
        self.cur = None
        self.curs = {
            "southeast" : (1, 1),
            "east" : (1, 0),
            "south" : (0, 1)
        }

        self.ccurs = {
            "southeast" : Qt.SizeFDiagCursor,
            "northeast" : Qt.SizeBDiagCursor,
            "southwest" : Qt.SizeBDiagCursor,
            "northwest" : Qt.SizeFDiagCursor,
            "north" : Qt.SizeVerCursor,
            "south" : Qt.SizeVerCursor,
            "east" : Qt.SizeHorCursor,
            "west" : Qt.SizeHorCursor,
        }

        self.anims = list()

        self._styleControlButtons()

    def __repr__(self):
        return f"<pyqt5Custom.TitleBar()>"

    def update(self):
        for a in self.anims:
            a.update()
        super().update()

    def newAnimation(self, start=0, end=1, type=Animation.easeOutCubic):
        a = AnimationHandler(self, start, end, type)
        self.anims.append(a)
        return a

    def setWindowResizable(self, resizable):
        self._resizable = resizable

        if self._resizable:
            self.maxButton.show()

        else:
            self.maxButton.hide()

    def setStyleDict(self, styledict):
        for k in styledict:
            self.styleDict[k] = styledict[k]
        #self._styleControlButtons()

    def _styleControlButtons(self):
        self.closeButton.setStyleDict({
                "font-family" : self.styleDict["font-family"],
                "font-size" : self.styleDict["font-size"],
                "border-color" : (0, 0, 0, 0),
                "border-radius" : 0,
                "background-color" : (255, 255, 255)
            })
        self.closeButton.setStyleDict({
                "background-color" : (224, 0, 0),
                "color": (255, 255, 255)
            }, "hover")
        self.closeButton.setStyleDict({
                "background-color" : (255, 0, 0),
                "color" : (255, 255, 255)
            }, "press")

        self.maxButton.setStyleDict({
                "font-family" : self.styleDict["font-family"],
                "font-size" : self.styleDict["font-size"],
                "border-color" : (0, 0, 0, 0),
                "border-radius" : 0,
                "background-color" : (255, 255, 255)
            })
        self.maxButton.setStyleDict({
                "background-color" : (236, 236, 236),
            }, "hover")
        self.maxButton.setStyleDict({
                "background-color" : (218, 218, 218),
            }, "press")

        self.minButton.setStyleDict({
                "font-family" : self.styleDict["font-family"],
                "font-size" : self.styleDict["font-size"],
                "border-color" : (0, 0, 0, 0),
                "border-radius" : 0,
                "background-color" : (255, 255, 255)
            })
        self.minButton.setStyleDict({
                "background-color" : (236, 236, 236),
            }, "hover")
        self.minButton.setStyleDict({
                "background-color" : (218, 218, 218),
            }, "press")

    def setTitle(self, title):
        self.parent().setWindowTitle(title)
        self.title_lbl.setText(title)

    def title(self):
        return self.title_lbl.text()

    def parentMousePressEvent(self, event):
        self._start = self.mapToGlobal(event.pos())
        self._orw = self.parent().width()
        self._orh = self.parent().height()
        self._orx = self.parent().x()
        self._ory = self.parent().y()

        if event.x() > self.parent().width() - self.cursize:
            if event.y() > self.parent().height() - self.cursize:
                self.cur = "southeast"

            elif event.y() < self.cursize:
                self.cur = "northeast"

            else:
                self.cur = "east"

        elif event.x() < self.cursize:
            if event.y() > self.parent().height() - self.cursize:
                self.cur = "southwest"

            elif event.y() < self.cursize:
                self.cur = "northwest"

            else:
                self.cur = "west"

        elif event.y() > self.parent().height() - self.cursize:
            self.cur = "south"

        elif event.y() < self.cursize:
            self.cur = "north"

        else:
            self.cur = None

    def parentMouseReleaseEvent(self, event):
        self.cur = None
        QApplication.restoreOverrideCursor()

    def parentMouseMoveEvent(self, event):
        if self.cur is not None and self._resizable:
            QApplication.restoreOverrideCursor()
            QApplication.setOverrideCursor(self.ccurs[self.cur])

            end = self.mapToGlobal(event.pos())
            self._movement = end - self._start

            if self.cur in ("east", "southeast", "south"):
                x = self._movement.x() * self.curs[self.cur][0]
                y = self._movement.y() * self.curs[self.cur][1]

                if self.parent().width() + x < self.parent().minimumWidth():
                    end.setX(end.x()-x)
                    x = 0

                if self.parent().height() + y < self.parent().minimumHeight():
                    end.setY(end.y()-y)
                    y = 0

                self.parent().setGeometry(self.parent().x(),
                                          self.parent().y(),
                                          self._orw + x,
                                          self._orh + y)
                self.parent().update()

                self._orw += x
                self._orh += y

            elif self.cur == "northeast":
                x = self._movement.x()
                y = self._movement.y()

                self.parent().setGeometry(self.parent().x(),
                                          self._ory + y,
                                          self._orw + x,
                                          self.parent().height() - y)
                self.parent().setFixedSize(self._orw+x, self.parent().height()-y)
                self.parent().update()

                self._orw += x
                self._ory += y

            elif self.cur == "southwest":
                x = self._movement.x()
                y = self._movement.y()

                #if x > 2: x = 2
                #if x < -2: x = -2

                # self.parent().setFixedSize(self.parent().width()-x,
                #                            self._orh + y)
                #
                # self.parent().move(self._orx - x,
                #                    self.parent().y())

                self.parent().setGeometry(self._orx - x,
                                          self.parent().y(),
                                          self.parent().width()-x,
                                          self._orh + y)
                #self.parent().update()

                self._orx += x
                self._orh += y
                #self._ory += y

            #self.parent().setGeometry(self.parent().x(), self.parent().y(), self._orw+x, self.parent().height())

            self._start = end

    def paintEvent(self, event):
        pt = QPainter()
        pt.begin(self)
        pt.setRenderHint(QPainter.Antialiasing, on=self.styleDict["render-aa"])

        fnt = self.title_lbl.font()
        fnt.setPixelSize(self.styleDict["font-size"])
        if not self.styleDict["font-subpixel-aa"]: fnt.setStyleStrategy(QFont.NoSubpixelAntialias)
        if self.styleDict["font-family"]: fnt.setFamily(self.styleDict["font-family"])
        self.title_lbl.setFont(fnt)

        plt = self.title_lbl.palette()
        plt.setColor(self.title_lbl.foregroundRole(), QColor(*self.styleDict["color"]))
        self.title_lbl.setPalette(plt)

        brush = QBrush(QColor(*self.styleDict["background-color"]))
        pen = QPen(QColor(0, 0, 0, 0), 0)
        pt.setBrush(brush)
        pt.setPen(pen)

        pt.drawRect(0, 0, self.width(), self.height())

        pt.end()

        f = False
        for a in self.anims:
            if not a.done():
                f = True
                break

        if f: self.update()

    def mousePressEvent(self, event):
        if event.x() < self.parent().width() - 10:
            self.start = self.mapToGlobal(event.pos())
            self.pressing = True
        else:
            self.parentMousePressEvent(event)

    def mouseReleaseEvent(self, event):
        self.pressing = False
        self.parentMouseReleaseEvent(event)

    def mouseMoveEvent(self, event):
        if self.pressing:
            end = self.mapToGlobal(event.pos())
            self.movement = end - self.start
            self.parent().setGeometry(self.mapToGlobal(self.movement).x(),
                                      self.mapToGlobal(self.movement).y(),
                                      self.parent().width(),
                                      self.parent().height())
            self.start = end
        else:
            self.parentMouseMoveEvent(event)
