#                 PyQt5 Custom Widgets                #
#                GPL 3.0 - Kadir Aksoy                #
#   https://github.com/kadir014/pyqt5-custom-widgets  #
#                                                     #
#    This script is one of the pyqt5Custom examples   #


import sys

from PyQt5.QtCore import Qt
from PyQt5.QtWidgets import QWidget, QApplication, QVBoxLayout
from PyQt5.QtGui import QColor, QFontDatabase, QBrush, QPalette, QLinearGradient

from pyqt5Custom import TitleBar



class MainWindow(QWidget):
    def __init__(self):
        super().__init__()

        QFontDatabase.addApplicationFont("data/SFPro.ttf")

        self.setGeometry(100, 100, 410, 240)

        self.layout = QVBoxLayout()
        self.layout.setAlignment(Qt.AlignTop)
        self.setLayout(self.layout)
        self.layout.setContentsMargins(0, 0, 0, 0)

        self.titlebar = TitleBar(self, title="Custom TitleBar!")
        self.layout.addWidget(self.titlebar, alignment=Qt.AlignTop)
        self.titlebar.setStyleDict({
                "background-color" : (255, 255, 255),
                "font-size" : 18,
                "font-subpixel-aa" : True,
                "font-family" : "SF Pro Display",
            })

        self.titlebar.closeButton.setStyleDict({
                "border-radius" : 100,
                "background-color" : (255, 255, 255, 120),
                "font-size" : 18,
                "font-family" : "SF Pro Display",
                "render-fast" : True
            })
        self.titlebar.maxButton.copyStyleDict(self.titlebar.closeButton)
        self.titlebar.minButton.copyStyleDict(self.titlebar.closeButton)


        self.anim = self.titlebar.newAnimation()
        self.anim.speed = 0.7

        @self.anim.tick
        def callback():
            r = QColor(255, 100, 100)
            g = QColor(100, 255, 100)
            b = QColor(100, 100, 255)

            if self.anim.current() < 0.25:
                c = self.anim.lerp(r, g)
            elif self.anim.current() < 0.75:
                c = self.anim.lerp(g, b)
            else:
                c = self.anim.lerp(r, b)

            self.titlebar.setStyleDict({
                    "background-color" : (c.red(), c.green(), c.blue()),
                })

        self.anim.start(loop = True)



if __name__ == "__main__":
    app = QApplication(sys.argv)

    mw = MainWindow()
    mw.show()

    sys.exit(app.exec_())
