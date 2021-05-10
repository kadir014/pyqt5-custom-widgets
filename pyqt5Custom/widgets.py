#                 PyQt5 Custom Widgets                #
#                GPL 3.0 - Kadir Aksoy                #
#   https://github.com/kadir014/pyqt5-custom-widgets  #


import time
from math import ceil, sin, pi, sqrt, atan2, pow
import random
import pathlib
import requests

from PyQt5.QtCore import Qt, QEvent, QSize, QPoint, pyqtSignal
from PyQt5.QtWidgets import QApplication, QWidget, QHBoxLayout, QVBoxLayout, QLabel, QAbstractButton, QPlainTextEdit, QGraphicsOpacityEffect, QGraphicsDropShadowEffect
from PyQt5.QtGui import QColor, QPainter, QPixmap, QPen, QBrush, QMovie, QImage, QFont

from .syntaxhighlighter import SyntaxHighlighter



class Animation:
    easeOutSine  = lambda x: sin((x * pi) / 2)
    easeOutCubic = lambda x: 1 - ((1 - x)**3)
    easeOutQuart = lambda x: 1 - pow(1 - x, 4)
    easeOutCirc  = lambda x: sqrt(1 - pow(x - 1, 2))



class AnimationHandler:
    def __init__(self, widget, startv, endv, type):
        self.widget = widget
        self.type = type

        self.startv = startv
        self.endv = endv

        self.value = 0.0001

        self.reverse = False
        self.start_time = None
        self.interval = 20 / 1000

    def start(self, reverse=False):
        self.start_time = time.time()
        self.reverse = reverse
        self.value = 0.01

    def done(self):
        return self.start_time is None

    def update(self):
        if not self.done():
            if time.time() - self.start_time < self.interval:
                return

            self.start_time = time.time()
            self.value = self.type(self.value)

            if self.reverse:
                if ceil(self.current()) <= self.startv: self.start_time = None
            else:
                if self.current() >= self.endv: self.start_time = None

    def current(self):
        if self.reverse:
            return self.endv - (self.value * (self.endv-self.startv))
        else:
            return self.value * (self.endv-self.startv)



class TitleBar(QWidget):
    def __init__(self, parent, title=""):
        super().__init__(parent)

        self.parent().setWindowTitle(title)
        self.parent().setWindowFlags(Qt.FramelessWindowHint)

        setattr(self.parent(), "mousePressEvent", self.parentMousePressEvent)
        setattr(self.parent(), "mouseMoveEvent", self.parentMouseMoveEvent)
        setattr(self.parent(), "mouseReleaseEvent", self.parentMouseReleaseEvent)

        # self.event_widget = QWidget()
        # self.event_widget.setParent(self.parent())
        # self.event_widget.setGeometry(5, 5, self.parent().width()-10, self.parent().height()-10)
        # self.event_widget.raise_()
        # self.event_widget.hide()
        #
        # setattr(self.event_widget, "enterEvent", self.childEnterEvent)

        self.setFixedHeight(32)

        self.layout = QHBoxLayout()
        self.layout.setContentsMargins(14, 0, 0, 0)
        self.layout.setSpacing(0)
        self.setLayout(self.layout)

        self.title_lbl = QLabel(title)
        self.layout.addWidget(self.title_lbl)

        self.close_btn = StyledButton(text="✕")
        self.close_btn.setStyleSheet("font-size:18px;")
        self.close_btn.setFixedSize(self.height()+19, self.height())
        self.close_btn.borderRadius = 0
        self.close_btn.borderColor = QColor(245, 66, 126, 0)
        self.close_btn.backgroundColor = QColor(245, 66, 126)
        self.close_btn.circleColor = self.close_btn.borderColor.lighter(146)
        self.close_btn.hoverLighter = True
        self.close_btn.hoverFactor = 3.8

        self.max_btn = StyledButton(text="🗖")
        self.max_btn.setStyleSheet("font-size:18px;")
        self.max_btn.setFixedSize(self.height()+19, self.height())
        self.max_btn.borderRadius = 0
        self.max_btn.borderColor = QColor(245, 66, 126, 0)
        self.max_btn.backgroundColor = QColor(245, 66, 126)
        self.max_btn.circleColor = self.max_btn.borderColor.lighter(146)
        self.max_btn.hoverLighter = True
        self.max_btn.hoverFactor = 3.8

        self.min_btn = StyledButton(text="🗕")
        self.min_btn.setStyleSheet("font-size:18px;")
        self.min_btn.setFixedSize(self.height()+19, self.height())
        self.min_btn.borderRadius = 0
        self.min_btn.borderColor = QColor(245, 66, 126, 0)
        self.min_btn.backgroundColor = QColor(245, 66, 126)
        self.min_btn.circleColor = self.min_btn.borderColor.lighter(146)
        self.min_btn.hoverLighter = True
        self.min_btn.hoverFactor = 3.8

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
        if self.cur is not None:
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
        pt.setRenderHint(QPainter.Antialiasing)

        brush = QBrush(QColor(245, 66, 126))
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



class ImageBox(QLabel):
    def __init__(self, source, keepAspectRatio=True, smoothScale=True):
        super().__init__()

        self.source = source
        self.animated = False

        self.keepAspectRatio = keepAspectRatio
        self.smoothScale = smoothScale

        if self.source is not None: self.setSource(self.source)

    def setSource(self, source):
        self.source = source

        if self.source.startswith("http"):

            if self.source.endswith(".gif"):
                r = requests.get(self.source)

                with open("temp.gif", "wb") as f:
                    f.write(r.content)

                self.animated = True
                self.orgmovie = QMovie("temp.gif")
                self.movie = self.orgmovie
                self.setMovie(self.movie)
                self.movie.start()

            else:
                r = requests.get(self.source)

                self.animated = False
                self.orgpixmap = QPixmap.fromImage(QImage.fromData(r.content))
                self.pixmap = self.orgpixmap
                self.setPixmap(self.pixmap)

        else:
            if source.endswith(".gif"):
                self.animated = True
                self.movie = QMovie(source)
                self.setMovie(self.movie)
                self.movie.start()

            else:
                self.animated = False
                self.orgpixmap = QPixmap(source)
                self.pixmap = QPixmap(source)
                self.setPixmap(self.pixmap)

        self.resizeEvent(None)

    def resizeEvent(self, event):
        w, h = self.width(), self.height()

        t = (Qt.FastTransformation, Qt.SmoothTransformation)[self.smoothScale]
        k = (Qt.IgnoreAspectRatio, Qt.KeepAspectRatio)[self.keepAspectRatio]

        if self.animated:
            self.movie.setScaledSize(QSize(w, h))

        else:
            self.pixmap = self.orgpixmap.scaled(w, h, transformMode=t, aspectRatioMode=k)
            self.setPixmap(self.pixmap)



class ColorPreview(QWidget):
    def __init__(self):
        super().__init__()

        self.color = QColor(0, 0, 0)

        self.layout = QVBoxLayout()
        self.setLayout(self.layout)
        self.label = QLabel("#000000")
        self.layout.addWidget(self.label, alignment=Qt.AlignBottom|Qt.AlignHCenter)

        self.setFixedSize(90, 65)

    def setColor(self, color):
        self.color = color
        self.label.setText(self.color.name())

    def paintEvent(self, event):
        pt = QPainter()
        pt.begin(self)
        pt.setRenderHint(QPainter.Antialiasing)

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

    def mouseMoveEvent(self, event):
        self.mouse_x, self.mouse_y = event.x(), event.y()

        dist = sqrt(pow(self.mouse_x-self.radius, 2)+pow(self.mouse_y-self.radius, 2))

    def paintEvent(self, event):
        pt = QPainter()
        pt.begin(self)
        pt.setRenderHint(QPainter.Antialiasing)

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



# this is a data class which is meant to be used by DragDropFile
class FileDetails:
    def __init__(self, path, content):
        self.path = path
        self.content = content

        self._path = pathlib.Path(self.path)

        self.name      = self._path.name
        self.pureName  = self._path.stem
        self.extension = self._path.suffix



class DragDropFile(QWidget):

    fileDropped = pyqtSignal(FileDetails)

    def __init__(self):
        super().__init__()

        self.setAcceptDrops(True)

        self.borderColor = QColor(190, 190, 190)
        self.hoverBackground = QColor(245, 245, 250)
        self.borderRadius = 26
        self.borderWidth = 6

        self.layout = QVBoxLayout()
        self.layout.setAlignment(Qt.AlignCenter)
        self.setLayout(self.layout)

        self.title_lbl = QLabel("Drop your file here!")
        self.filename_lbl = QLabel("")

        self.layout.addWidget(self.title_lbl, alignment=Qt.AlignHCenter)
        self.layout.addSpacing(7)
        self.layout.addWidget(self.filename_lbl, alignment=Qt.AlignHCenter)

        self.title_lbl.setStyleSheet("font-size:19px;")
        self.filename_lbl.setStyleSheet("font-size:14px; color: #666666;")

        self.dragEnter = False

        self.file = None

    def setTitle(self, title):
        self.title_lbl.setText(title)

    def getFile(self):
        return

    def dragEnterEvent(self, event):
        if event.mimeData().hasUrls():
            self.dragEnter = True
            event.accept()
            self.repaint()
        else:
            event.ignore()

    def dragLeaveEvent(self, event):
        self.dragEnter = False
        self.repaint()

    def dropEvent(self, event):
        mime = event.mimeData()
        file = FileDetails(mime.urls()[0].toLocalFile(), mime.text())

        self.filename_lbl.setText(file.name)

        self.fileDropped.emit(file)

        self.dragEnter = False
        self.repaint()

    def paintEvent(self, event):
        pt = QPainter()
        pt.begin(self)
        pt.setRenderHint(QPainter.Antialiasing)

        pen = QPen(self.borderColor, self.borderWidth, Qt.DotLine, Qt.RoundCap)
        pt.setPen(pen)

        if self.dragEnter:
            brush = QBrush(self.hoverBackground)
            pt.setBrush(brush)

        pt.drawRoundedRect(self.borderWidth, self.borderWidth, self.width()-self.borderWidth*2, self.height()-self.borderWidth*2, self.borderRadius, self.borderRadius)

        pt.end()



class CodeTextEdit(QWidget):

    LANG_DISPLAY = {
            "plain"  : "Plain text",
            "python" : "Python",
            "py"     : "Python",
            "cpp"    : "C++",
            "c++"    : "C++"
        }

    def __init__(self):
        super().__init__()

        self.layout = QHBoxLayout()
        self.layout.setContentsMargins(0, 0, 0, 0)
        self.setLayout(self.layout)

        self.layout.addSpacing(37)

        self.editorlyt = QVBoxLayout()
        self.editorlyt.setSpacing(0)
        self.editorlyt.setContentsMargins(0, 0, 0, 0)
        self.layout.addLayout(self.editorlyt)

        self.editor = QPlainTextEdit()
        self.editor.setLineWrapMode(QPlainTextEdit.NoWrap)
        self.editorlyt.addWidget(self.editor)

        self.setStyleSheet("QPlainTextEdit {font-family:Consolas; font-size:14px; color:#222222;}")

        self.highlighter = SyntaxHighlighter(self.editor.document())

        self.sliderVal = 0
        self.lastdigit = 2
        vs = self.editor.verticalScrollBar()

        @vs.rangeChanged.connect
        def slot(v):
            self.sliderVal = self.editor.verticalScrollBar().value()

            if len(str(vs.maximum()+15)) > self.lastdigit:
                self.lastdigit = len(str(vs.maximum()+15))
                self.layout.insertSpacing(0, 10)

            self.update()

        @vs.valueChanged.connect
        def slot(v):
            self.sliderVal = v

            self.update()

        self.statusbar = QWidget()
        self.statusbar.setFixedHeight(26)
        self.statusbarlyt = QHBoxLayout()
        self.statusbarlyt.setContentsMargins(10, 0, 30, 0)
        self.statusbar.setLayout(self.statusbarlyt)
        self.editorlyt.addWidget(self.statusbar)

        self.cursor_lbl = QLabel("0:0")
        self.cursor_lbl.setStyleSheet("font-size:16px;")
        self.statusbarlyt.addWidget(self.cursor_lbl, alignment=Qt.AlignLeft|Qt.AlignVCenter)

        self.lang_lbl = QLabel("Plain text")
        self.lang_lbl.setStyleSheet("font-size:16px;")
        self.statusbarlyt.addWidget(self.lang_lbl, alignment=Qt.AlignRight|Qt.AlignVCenter)

        @self.editor.cursorPositionChanged.connect
        def slot():
            self.cursor_lbl.setText(f"{self.editor.textCursor().blockNumber()}:{self.editor.textCursor().positionInBlock()}")

    def setTheme(self, theme):
        self.highlighter.setTheme(theme)
        self.highlighter.setRules()

        c = self.highlighter.theme["background"]
        rgb = f"rgb({c.red()}, {c.green()}, {c.blue()})"

        cc = self.highlighter.theme["identifier"]
        crgb = f"rgb({cc.red()}, {cc.green()}, {cc.blue()})"

        self.editor.setStyleSheet(f"QPlainTextEdit {{background-color: {rgb}; color: {crgb};}}")

        self.cursor_lbl.setStyleSheet(f"color: {crgb}; font-size:16px;")
        self.lang_lbl.setStyleSheet(f"color: {crgb}; font-size:16px;")

        self.highlighter.rehighlight()
        self.update()

    def setLang(self, lang):
        self.lang_lbl.setText(CodeTextEdit.LANG_DISPLAY[lang])

        self.highlighter.setLang(lang)
        self.highlighter.setRules()
        self.highlighter.rehighlight()
        self.update()

    def loadFile(self, filepath, encoding="utf-8"):

        if filepath.endswith(".py"): lang = "python"
        elif filepath.endswith(".cpp"): lang = "cpp"
        else: lang = "plain"

        with open(filepath, "r", encoding=encoding) as f:
            self.editor.setPlainText(f.read())

        self.setLang(lang)

    def paintEvent(self, event):
        pt = QPainter()
        pt.begin(self)
        pt.setRenderHint(QPainter.Antialiasing)

        pt.setBrush(QBrush(self.highlighter.theme["lines-background"]))

        pt.drawRect(0, 0, self.width(), self.height())

        font = self.editor.font()
        pt.setFont(font)

        gap = font.pixelSize() + 3

        for i in range((self.height()//gap)):
            font = pt.font()
            pt.setFont(font)
            pt.setPen(QPen(self.highlighter.theme["lines"]))

            pt.drawText(13, i*gap, str(i+self.sliderVal))

        pt.setBrush(QBrush(self.highlighter.theme["background"]))
        pt.setPen(QPen(QColor(0, 0, 0, 0)))
        pt.drawRect(3, self.height()-self.statusbar.height(), 40, self.statusbar.height()-6)

        pt.end()



class EmbedWindow(QWidget):

    closed = pyqtSignal()

    def __init__(self, parent, pos=None):
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
        self.headerColor = QColor(245, 66, 126)
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

        self.title = QLabel("New window")
        self.title.setStyleSheet("color:white; font-size:14px; font-family:Montserrat-Regular;")

        self.close_btn = StyledButton("✕")
        self.close_btn.opacity.setOpacity(0.999)
        self.close_btn.setFixedSize(self.headerHeight, self.headerHeight)
        self.close_btn.setStyleSheet("color:white; font-size:17px;")
        self.close_btn.backgroundColor = QColor(245, 66, 126)
        self.close_btn.borderColor = QColor(245, 66, 126)
        self.close_btn.circleColor = self.close_btn.backgroundColor.lighter(146)
        self.close_btn.hoverLighter = True
        self.close_btn.borderRadius = self.borderRadius
        self.close_btn.hoverFactor = 3.8

        @self.close_btn.clicked.connect
        def slot():
            self.close()
            self.destroy()
            self.closed.emit()

        self.deta_btn = StyledButton("▲")
        self.deta_btn.opacity.setOpacity(0.999)
        self.deta_btn.setFixedSize(self.headerHeight, self.headerHeight)
        self.deta_btn.setStyleSheet("color:white; font-size:17px;")
        self.deta_btn.backgroundColor = QColor(245, 66, 126)
        self.deta_btn.borderColor = QColor(245, 66, 126)
        self.deta_btn.circleColor = self.deta_btn.backgroundColor.lighter(146)
        self.deta_btn.hoverLighter = True
        self.deta_btn.borderRadius = self.borderRadius
        self.deta_btn.hoverFactor = 3.8

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

    def setTitle(text):
        self.title.setText(text)

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
        pt.setRenderHint(QPainter.Antialiasing)

        pen = QPen(QColor(0, 0, 0, 0), 1)
        brush = QBrush(QColor(252, 252, 252))
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

        if not self.anim.done(): self.update()



class StyledButton(QAbstractButton):

    defaultStyles = ("flat", "hyper")

    def __init__(self, text="", style="flat", icon=None, fixedBottom=False):
        super().__init__()

        self.text = text

        self.layout = QHBoxLayout()
        self.layout.setContentsMargins(0, 0, 0, 0)
        self.setLayout(self.layout)

        if self.text:
            self.textLbl = QLabel(self.text)
            self.layout.addWidget(self.textLbl, alignment=Qt.AlignCenter)

        self._icon = None
        if icon is not None:
            self.setIcon(icon)

        # TODO: find a better way for opacity
        self.opacity = QGraphicsOpacityEffect(self)
        self.opacity.setOpacity(1)
        self.setGraphicsEffect(self.opacity)

        if style not in StyledButton.defaultStyles:
            raise Exception(f"'{style}' is not a default style.")
        self.style = style

        self.dropShadow = False
        self.shadow = None

        self.borderRadius = 6

        if self.style == "flat":
            self.anim = AnimationHandler(self, 0, 5, Animation.easeOutCubic)
            self.animcirc = AnimationHandler(self, 0, 100, Animation.easeOutSine)
            self.animcirc.interval = 25 / 1000

            self.borderColor = QColor(52, 189, 235)
            self.borderWidth = 2
            self.backgroundColor = QColor(255, 255, 255)

            self.hoverLighter = False
            self.hoverFactor = 1

        elif self.style == "hyper":
            self.animline = AnimationHandler(self, 0, 1, Animation.easeOutCubic)
            self.animline.value = 0

            self.borderColor = QColor(235, 52, 91)
            self.borderWidth = 4

            self.fixedBottom = fixedBottom

        self.circleColor = self.borderColor.lighter(166)

        self._press_reset = False
        self.mouse_x, self.mouse_y = 0, 0

    def setIcon(self, filepath):
        self._icon = ImageBox(filepath)
        self._icon.setFixedSize(18, 18)
        if self.text:
            self.layout.insertWidget(0, self._icon, alignment=Qt.AlignVCenter|Qt.AlignRight)
            self.layout.addSpacing(30)
        else:
            self.layout.insertWidget(0, self._icon, alignment=Qt.AlignCenter)

    def setIconSize(self, width, height):
        self._icon.setFixedSize(width, height)

    def setDropShadow(self, bshad):
        if bshad:
            self.dropShadow = True
            if self.shadow is None:
                self.shadow = QGraphicsDropShadowEffect(self)
                self.shadow.setBlurRadius(6)
                self.shadow.setColor(QColor(0, 0, 0, 100))
                self.shadow.setOffset(0, 2)
                self.setGraphicsEffect(self.shadow)

        else:
            self.dropShadow = False
            self.shadow.setColor(QColor(0, 0, 0, 0))

    def update(self, *args, **kwargs):
        if self.style == "flat":
            self.anim.update()
            self.animcirc.update()
        elif self.style == "hyper":
            self.animline.update()
        super().update(*args, **kwargs)

    def enterEvent(self, event):
        if self.style == "flat": self.anim.start()
        elif self.style == "hyper": self.animline.start()

    def leaveEvent(self, event):
        if not self._press_reset and self.style == "flat":
            self.anim.start(reverse=True)
        if self.style == "hyper":
            self.animline.start(reverse=True)
        self._press_reset = False

    def mousePressEvent(self, event):
        self.mouse_x, self.mouse_y = event.x(), event.y()
        if self.style == "flat":
            self.animcirc.start()
            if not self._press_reset:
                self.anim.start(reverse=True)
                self._press_reset = True
        super().mousePressEvent(event)

    def paintEvent(self, event):
        pt = QPainter()
        pt.begin(self)
        pt.setRenderHint(QPainter.Antialiasing)

        if self.style == "flat":
            if self.isEnabled():
                pen = QPen(self.borderColor, self.borderWidth, Qt.SolidLine, Qt.RoundCap, Qt.RoundJoin)
                if self.hoverLighter: brush = QBrush(self.backgroundColor.lighter(100+self.anim.current()*self.hoverFactor))
                else: brush = QBrush(self.backgroundColor.darker(100+self.anim.current()*self.hoverFactor))
            else:
                pen = QPen(self.borderColor.darker(106), self.borderWidth, Qt.SolidLine, Qt.RoundCap, Qt.RoundJoin)
                brush = QBrush(self.backgroundColor.darker(103))
            pt.setPen(pen)
            pt.setBrush(brush)

            pt.drawRoundedRect(1, 1, self.width()-2, self.height()-2, self.borderRadius, self.borderRadius)

            pt.setPen(QPen(QColor(0, 0, 0, 0), 0))
            c = QColor(self.circleColor.red(), self.circleColor.green(), self.circleColor.blue(), 255-(self.animcirc.current()*2.5))
            pt.setBrush(QBrush(c, Qt.SolidPattern))

            pt.drawEllipse(self.mouse_x-self.animcirc.current()/1,
                                self.mouse_y-self.animcirc.current()/1,
                                self.animcirc.current()*2,
                            self.animcirc.current()*2)

        elif self.style == "hyper":
            if self.isEnabled():
                pen = QPen(self.borderColor, self.borderWidth, Qt.SolidLine, Qt.RoundCap, Qt.RoundJoin)
            else:
                pen = QPen(self.borderColor.darker(110), self.borderWidth, Qt.SolidLine, Qt.RoundCap, Qt.RoundJoin)
            pt.setPen(pen)

            if self.fixedBottom: a = 1
            else: a = self.animline.current()

            pt.drawLine(self.width()//2, self.height(), self.width()//2+(a*(self.width()//2)), self.height())
            pt.drawLine(self.width()//2, self.height(), self.width()//2+(a*(self.width()//-2)), self.height())

        pt.end()
        if self.style == "flat":
            if not self.anim.done(): self.update()
            if not self.animcirc.done(): self.update()
        elif self.style == "hyper":
            if not self.animline.done(): self.update()



class ToggleSwitch(QWidget):

    defaultStyles = ("win10", "ios", "android")
    toggled = pyqtSignal(name="toggled")

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
