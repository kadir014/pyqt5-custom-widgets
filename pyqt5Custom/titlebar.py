#                 PyQt5 Custom Widgets                #
#                GPL 3.0 - Kadir Aksoy                #
#   https://github.com/kadir014/pyqt5-custom-widgets  #


from PyQt5.QtCore    import Qt
from PyQt5.QtWidgets import QApplication, QWidget, QHBoxLayout, QLabel
from PyQt5.QtGui     import QColor, QPainter, QPen, QBrush, QFont

from .styledbutton import StyledButton



class TitleBar(QWidget):
    def __init__(self, parent, title=""):
        super().__init__(parent)

        self.parent().setWindowTitle(title)
        self.parent().setWindowFlags(Qt.FramelessWindowHint)

        setattr(self.parent(), "mousePressEvent",   self.parentMousePressEvent)
        setattr(self.parent(), "mouseMoveEvent",    self.parentMouseMoveEvent)
        setattr(self.parent(), "mouseReleaseEvent", self.parentMouseReleaseEvent)

        # self.event_widget = QWidget()
        # self.event_widget.setParent(self.parent())
        # self.event_widget.setGeometry(5, 5, self.parent().width()-10, self.parent().height()-10)
        # self.event_widget.raise_()
        # self.event_widget.hide()
        #
        # setattr(self.event_widget, "enterEvent", self.childEnterEvent)

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

        self.close_btn = StyledButton(text="✕")
        self.close_btn.setFixedSize(self.height()+19, self.height())

        self.max_btn = StyledButton(text="🗖")
        self.max_btn.setFixedSize(self.height()+19, self.height())

        self.min_btn = StyledButton(text="🗕")
        self.min_btn.setFixedSize(self.height()+19, self.height())

        self._styleControlButtons()

        self.close_btn.clicked.connect(self.parent().close)

        self.min_btn.clicked.connect(self.parent().showMinimized)

        @self.max_btn.clicked.connect
        def slot():
            if self.parent().isMaximized():
                self.parent().showNormal()
            else:
                self.parent().showMaximized()

        self.layout.addWidget(self.min_btn, alignment=Qt.AlignRight)
        self.layout.addWidget(self.max_btn)
        self.layout.addWidget(self.close_btn)

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

    def __repr__(self):
        return f"<pyqt5Custom.TitleBar()>"

    def setWindowResizable(self, resizable):
        self._resizable = resizable

        if self._resizable:
            self.max_btn.show()

        else:
            self.max_btn.hide()

    def setStyleDict(self, styledict):
        for k in styledict:
            self.styleDict[k] = styledict[k]
        self._styleControlButtons()

    def _styleControlButtons(self):
        self.close_btn.setStyleDict({
                "font-family" : self.styleDict["font-family"],
                "font-size" : self.styleDict["font-size"],
                "border-color" : (0, 0, 0, 0),
                "border-radius" : 0,
                "background-color" : (255, 255, 255)
            })
        self.close_btn.setStyleDict({
                "background-color" : (224, 0, 0),
                "color": (255, 255, 255)
            }, "hover")
        self.close_btn.setStyleDict({
                "background-color" : (255, 0, 0),
                "color" : (255, 255, 255)
            }, "press")

        self.max_btn.setStyleDict({
                "font-family" : self.styleDict["font-family"],
                "font-size" : self.styleDict["font-size"],
                "border-color" : (0, 0, 0, 0),
                "border-radius" : 0,
                "background-color" : (255, 255, 255)
            })
        self.max_btn.setStyleDict({
                "background-color" : (236, 236, 236),
            }, "hover")
        self.max_btn.setStyleDict({
                "background-color" : (218, 218, 218),
            }, "press")

        self.min_btn.setStyleDict({
                "font-family" : self.styleDict["font-family"],
                "font-size" : self.styleDict["font-size"],
                "border-color" : (0, 0, 0, 0),
                "border-radius" : 0,
                "background-color" : (255, 255, 255)
            })
        self.min_btn.setStyleDict({
                "background-color" : (236, 236, 236),
            }, "hover")
        self.min_btn.setStyleDict({
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

        brush = QBrush(QColor(*self.styleDict["background-color"]))
        pen = QPen(QColor(0, 0, 0, 0), 0)
        pt.setBrush(brush)
        pt.setPen(pen)

        pt.drawRect(0, 0, self.width(), self.height())

        pt.end()

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
