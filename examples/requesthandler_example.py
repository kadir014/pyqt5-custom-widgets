#                 PyQt5 Custom Widgets                #
#                GPL 3.0 - Kadir Aksoy                #
#   https://github.com/kadir014/pyqt5-custom-widgets  #
#                                                     #
#    This script is one of the pyqt5Custom examples   #


import sys
import time

from PyQt5.QtCore import Qt
from PyQt5.QtWidgets import QWidget, QApplication, QHBoxLayout, QVBoxLayout, QLabel, QLineEdit
from PyQt5.QtGui import QColor, QFontDatabase

from pyqt5Custom import StyledButton, TitleBar, Spinner, RequestHandler



class MainWindow(QWidget):
    def __init__(self):
        super().__init__()

        self.setFixedSize(400, 400)
        self.setGeometry(100, 100, 400, 400)
        self.setWindowTitle("RequestHandler Example")

        QFontDatabase.addApplicationFont("data/SFPro.ttf")

        self.setAutoFillBackground(True)
        p = self.palette()
        p.setColor(self.backgroundRole(), QColor(255, 255, 255))
        self.setPalette(p)

        self.layout = QVBoxLayout()
        self.layout.setAlignment(Qt.AlignTop)
        self.setLayout(self.layout)
        self.layout.setContentsMargins(0, 0, 0, 0)

        # Creating and starting the RequestHandler object
        self.rh = RequestHandler()
        self.rh.start()

        self.btn = StyledButton("GET Request", icon="data/dlicon.png")
        self.btn.setIconSize(33, 33)
        self.btn.setMinimumSize(178, 44)
        self.btn.setStyleDict({
                "background-color" : (52, 199, 89),
                "border-color" : (2, 199, 89),
                "border-radius" :  39,
                "color" : (255, 255, 255),
                "font-family" : "SF Pro Display",
                "font-size" : 21,
            })
        self.btn.setStyleDict({
                "background-color" : (47, 212, 119),
                "border-color" : (47, 212, 119)
            }, "hover")
        self.btn.setStyleDict({
                "background-color" : (89, 227, 149),
                "border-color" : (89, 227, 149),
                "color" : (255, 255, 255),
            }, "press")

        self.layout.addSpacing(80)
        self.layout.addWidget(self.btn, alignment=Qt.AlignHCenter)

        self.search = QLineEdit()
        self.search.setFixedSize(220, 41)
        self.search.setStyleSheet("padding: 10px; padding-bottom: 3px; font-size:16px; font-family: SF Pro Display; border: none; border-bottom: 2px solid rgb(0,122,255);")
        self.search.setText("https://github.com/")
        self.layout.addWidget(self.search, alignment=Qt.AlignHCenter)

        self.layout.addSpacing(25)

        self.panel = QWidget()
        self.panel.setStyleSheet("font-size: 17px; font-family: SF Pro Default;")
        self.panel.setFixedWidth(350)
        self.panellyt = QVBoxLayout()
        self.panellyt.setContentsMargins(0, 10, 0, 10)
        self.panel.setLayout(self.panellyt)
        self.layout.addWidget(self.panel, alignment=Qt.AlignHCenter)

        self.panel.setAutoFillBackground(True)
        p = self.panel.palette()
        p.setColor(self.backgroundRole(), QColor(250, 250, 250))
        self.panel.setPalette(p)

        self.row1 = QHBoxLayout()
        self.panellyt.addLayout(self.row1)
        self.row1.setContentsMargins(10, 0, 10, 0)

        self.row2wdt = QWidget()
        self.row2 = QHBoxLayout()
        self.row2wdt.setLayout(self.row2)
        self.panellyt.addWidget(self.row2wdt)
        self.row2.setContentsMargins(10, 8, 10, 8)

        self.row2wdt.setAutoFillBackground(True)
        p = self.row2wdt.palette()
        p.setColor(self.backgroundRole(), QColor(222, 222, 222))
        self.row2wdt.setPalette(p)

        self.row3 = QHBoxLayout()
        self.panellyt.addLayout(self.row3)
        self.row3.setContentsMargins(10, 0, 10, 0)

        self.info_status_d = QLabel("HTTP Code:")
        self.info_status = QLabel("0")
        self.row1.addWidget(self.info_status_d, alignment=Qt.AlignLeft)
        self.row1.addWidget(self.info_status, alignment=Qt.AlignRight)

        self.info_conlength_d = QLabel("Response content size:")
        self.info_conlength = QLabel("0 MB")
        self.row2.addWidget(self.info_conlength_d, alignment=Qt.AlignLeft)
        self.row2.addWidget(self.info_conlength, alignment=Qt.AlignRight)

        self.info_elaps_d = QLabel("Elapsed time:")
        self.info_elaps = QLabel("0 ms")
        self.row3.addWidget(self.info_elaps_d, alignment=Qt.AlignLeft)
        self.row3.addWidget(self.info_elaps, alignment=Qt.AlignRight)


        @self.btn.clicked.connect
        def slot():
            self.btn.setIcon(Spinner(2.4, QColor(255, 255, 255)))
            # Add new GET request to the pool
            self.rh.newRequest("GET", self.search.text())

        @self.rh.requestResponsed.connect
        def slot(response):
            self.btn.setIcon("data/dlicon.png")
            self.btn.setIconSize(28, 28)

            self.info_status.setText(str(response.status_code))
            l = len(response.content) / 1048576
            if l > 1: l = int(l)

            self.info_conlength.setText(f"{l:.2} MB")
            self.info_elaps.setText(str(response.elapsed.microseconds//1000)+" ms")



if __name__ == "__main__":
    app = QApplication(sys.argv)

    mw = MainWindow()
    mw.show()

    sys.exit(app.exec_())
