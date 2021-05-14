#                 PyQt5 Custom Widgets                #
#                GPL 3.0 - Kadir Aksoy                #
#   https://github.com/kadir014/pyqt5-custom-widgets  #


import pathlib

from PyQt5.QtCore    import Qt, pyqtSignal
from PyQt5.QtWidgets import QWidget, QVBoxLayout, QLabel
from PyQt5.QtGui     import QColor, QPainter, QPen, QBrush



class FileDetails:
    def __init__(self, path, content):
        self.path = path
        self.content = content
        self.size = len(self.content)

        self._path = pathlib.Path(self.path)

        self.name      = self._path.name
        self.pureName  = self._path.stem
        self.extension = self._path.suffix

    def __repr__(self):
        return f"<pyqt5Custom.FileDetails({self.name})>"



class DragDropFile(QWidget):

    fileDropped = pyqtSignal(FileDetails)

    def __init__(self):
        super().__init__()

        self.setAcceptDrops(True)

        self.setMinimumSize(120, 65)

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
        pt.setRenderHint(QPainter.Antialiasing, on=True)

        pen = QPen(self.borderColor, self.borderWidth, Qt.DotLine, Qt.RoundCap)
        pt.setPen(pen)

        if self.dragEnter:
            brush = QBrush(self.hoverBackground)
            pt.setBrush(brush)

        pt.drawRoundedRect(self.borderWidth, self.borderWidth, self.width()-self.borderWidth*2, self.height()-self.borderWidth*2, self.borderRadius, self.borderRadius)

        pt.end()
