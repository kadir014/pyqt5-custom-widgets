#                 PyQt5 Custom Widgets                #
#                GPL 3.0 - Kadir Aksoy                #
#   https://github.com/kadir014/pyqt5-custom-widgets  #


import pathlib
import requests

from PyQt5.QtCore    import Qt, QSize
from PyQt5.QtWidgets import QLabel
from PyQt5.QtGui     import QPixmap, QMovie, QImage



class ImageBox(QLabel):
    def __init__(self, source=None, parent=None, keepAspectRatio=True, smoothScale=True):
        super().__init__()

        self.source = source
        self.animated = False

        self.keepAspectRatio = keepAspectRatio
        self.smoothScale = smoothScale

        if self.source is not None: self.setSource(self.source)

    def __repr__(self):
        return f"<pyqt5Custom.ImageBox(animated={self.animated})>"

    def setSource(self, source):
        self.source = source

        if isinstance(self.source, pathlib.Path):
            self.source = str(self.source)

        if isinstance(self.source, str):

            # TODO: Better URL validation
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
                    self.pixmap = QPixmap(self.orgpixmap)
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

        elif isinstance(self.source, QPixmap):
            self.animated = False
            self.orgpixmap = QPixmap(self.source)
            self.pixmap = QPixmap(self.source)
            self.setPixmap(self.pixmap)

        elif isinstance(self.source, QImage):
            self.animated = False
            self.orgpixmap = QPixmap.fromImage(self.source)
            self.pixmap = QPixmap.fromImage(self.source)
            self.setPixmap(self.pixmap)

        elif isinstance(self.source, QMovie):
            self.animated = True
            self.movie = QMovie(self.source)
            self.setMovie(self.movie)
            self.movie.start()

        else:
            raise TypeError(f"QImage(source: Union[str, pathlib.Path, QPixmap, QImage, QMovie]) -> Argument 1 has unexpected type '{type(self.source)}'")

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
