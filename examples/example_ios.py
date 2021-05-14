#                 PyQt5 Custom Widgets                #
#                GPL 3.0 - Kadir Aksoy                #
#   https://github.com/kadir014/pyqt5-custom-widgets  #
#                                                     #
#    This script is one of the pyqt5Custom examples   #


import sys

from PyQt5.QtCore import Qt
from PyQt5.QtWidgets import QWidget, QApplication, QHBoxLayout, QVBoxLayout, QLabel, QFrame, QGridLayout
from PyQt5.QtGui import QColor, QFontDatabase

from pyqt5Custom import ToggleSwitch, StyledButton, ImageBox, ColorPicker, ColorPreview, DragDropFile, EmbedWindow, TitleBar, CodeTextEdit, SegmentedButtonGroup, Spinner, Toast



class MainWindow(QWidget):
    def __init__(self):
        super().__init__()
        QFontDatabase.addApplicationFont("data/SFPro.ttf")

        self.setMinimumSize(150, 37)
        self.setGeometry(100, 100, 890, 610)

        self.setAutoFillBackground(True)
        p = self.palette()
        p.setColor(self.backgroundRole(), QColor(255, 255, 255))
        self.setPalette(p)

        self.layout = QVBoxLayout()
        self.layout.setAlignment(Qt.AlignTop)
        self.setLayout(self.layout)
        self.layout.setContentsMargins(0, 0, 0, 0)

        self.titlebar = TitleBar(self, title="iOS Design")
        self.titlebar.setStyleDict({
                "background-color" : (255, 255, 255),
                "font-size" : 17,
                "border-radius": 6,
                "font-family" : "SF Pro Display"
            })

        self.layout.addWidget(self.titlebar, alignment=Qt.AlignTop)


        self.conlyt = QVBoxLayout()
        self.conlyt.setSpacing(0)
        self.conlyt.setContentsMargins(70, 15, 70, 0)
        self.layout.addLayout(self.conlyt)
        h = QLabel("<span style='font-size:58px; font-family:SF Pro Display; color:rgb(28,28,30);'>Heading</span>")
        ah = QLabel("<span style='font-size:26px; font-family:SF Pro Display; color:rgb(89,89,92);'>Alt heading</span>")
        h.setContentsMargins(100, 0, 0, 0)
        ah.setContentsMargins(103, 0, 0, 0)
        self.conlyt.addWidget(h)
        self.conlyt.addWidget(ah)

        self.conlyt.addSpacing(90)

        self.btnslyt = QHBoxLayout()
        self.conlyt.addLayout(self.btnslyt)
        self.btnlyt = QVBoxLayout()
        self.btnlyt.setSpacing(16)
        self.btnslyt.addLayout(self.btnlyt)

        self.btnlyt2 = QVBoxLayout()
        self.btnslyt.addLayout(self.btnlyt2)

        self.btn2 = StyledButton("Default")
        self.btn2.setFixedSize(170, 54)
        self.btn2.anim_press.speed = 7.3
        self.btn2.setStyleDict({
                "background-color" : (0, 122, 255),
                "border-color" : (0, 122, 255),
                "border-radius" : 7,
                "color" : (255, 255, 255),
                "font-family" : "SF Pro Display",
                "font-size" : 21,
            })
        self.btn2.setStyleDict({
                "background-color" : (36, 141, 255),
                "border-color" : (36, 141, 255)
            }, "hover")
        self.btn2.setStyleDict({
                "background-color" : (130, 190, 255),
                "border-color" : (130, 190, 255),
                "color" : (255, 255, 255),
            }, "press")

        self.btnlyt.addWidget(self.btn2, alignment=Qt.AlignTop|Qt.AlignHCenter)

        self.btn3 = StyledButton("Quiet")
        self.btn3.setFixedSize(170, 54)
        self.btn3.anim_press.speed = 5
        self.btn3.setStyleDict({
                "background-color" : (255, 255, 255),
                "border-color" : (255, 255, 255),
                "border-radius" : 7,
                "color" : (0, 122, 255),
                "font-family" : "SF Pro Display",
                "font-size" : 21
            })
        self.btn3.setStyleDict({
                "color" : (107, 178, 255),
            }, "hover")
        self.btn3.setStyleDict({
                "color" : (227, 227, 255),
            }, "press")

        self.btnlyt.addWidget(self.btn3, alignment=Qt.AlignTop|Qt.AlignHCenter)

        self.btn1 = StyledButton("Outline")
        self.btn1.setFixedSize(170, 54)
        self.btn1.anim_press.speed = 5
        self.btn1.setStyleDict({
                "background-color" : (255, 255, 255),
                "border-color" : (0, 122, 255),
                "border-radius" : 7,
                "color" : (0, 122, 255),
                "font-family" : "SF Pro Display",
                "font-size" : 21
            })
        self.btn1.setStyleDict({
                "color" : (107, 178, 255),
            }, "hover")
        self.btn1.setStyleDict({
                "background-color" : (0, 122, 255),
                "color" : (255, 255, 255),
            }, "press")

        self.btnlyt.addWidget(self.btn1, alignment=Qt.AlignTop|Qt.AlignHCenter)

        self.btn4 = StyledButton("Flat")
        self.btn4.setFixedSize(170, 54)
        self.btn1.anim_press.speed = 5
        self.btn4.setStyleDict({
                "background-color" : (247, 247, 247),
                "border-color" : (0, 0, 0, 0),
                "border-radius" : 7,
                "color" : (0, 122, 255),
                "font-family" : "SF Pro Display",
                "font-size" : 21
            })
        self.btn4.setStyleDict({
                "background-color" : (242, 242, 242),
            }, "hover")
        self.btn4.setStyleDict({
                "background-color" : (230, 230, 230),
            }, "press")

        self.btnlyt.addWidget(self.btn4, alignment=Qt.AlignTop|Qt.AlignHCenter)


        self.btnlyt2.setAlignment(Qt.AlignTop)
        self.btnlyt2.addWidget(QLabel("<span style='font-size:17px; font-family:SF Pro Display; color:rgb(99,99,102);'>Segmented Button Group (Horizontal)</span>"))
        self.btnlyt2.addSpacing(10)

        self.segbg = SegmentedButtonGroup(radio=True)
        self.segbg.setFixedSize(349, 36)
        self.segbg .setStyleDict({
                "background-color" : (255, 255, 255),
                "border-color" : (0, 122, 255),
                "border-radius" : 7,
                "color" : (0, 122, 255),
                "font-family" : "SF Pro Display",
                "font-size" : 15,
                "font-subpixel-aa" : True
            })
        self.segbg .setStyleDict({
                "color" : (107, 178, 255),
            }, "hover")
        self.segbg .setStyleDict({
                "background-color" : (0, 122, 255),
                "color" : (255, 255, 255),
            }, "press")
        self.segbg .setStyleDict({
                "background-color" : (61, 154, 255),
                "color" : (255, 255, 255),
            }, "check-hover")

        self.segbg.addButton("First")
        self.segbg.addButton("Second")
        self.segbg.addButton("Third")

        self.btnlyt2.addWidget(self.segbg)

        self.btnlyt2.addSpacing(35)
        self.btnlyt2.addWidget(QLabel("<span style='font-size:17px; font-family:SF Pro Display; color:rgb(99,99,102);'>Toggle Switches</span>"))
        self.btnlyt2.addSpacing(10)

        self.tglyt = QHBoxLayout()
        self.tglyt.setAlignment(Qt.AlignLeft)
        self.btnlyt2.addLayout(self.tglyt)

        self.tgsw1 = ToggleSwitch(style="ios")
        self.tgsw2 = ToggleSwitch(style="ios")
        self.tgsw2.setEnabled(False)

        self.tgsw1.setFixedWidth(120)
        self.tgsw2.setFixedWidth(120)

        @self.tgsw1.toggled.connect
        def slot():
            if self.tgsw1.isToggled():
                self.tgsw2.setEnabled(True)
            else:
                self.tgsw2.setEnabled(False)

        self.tglyt.addWidget(self.tgsw1)
        self.tglyt.addWidget(self.tgsw2)

        self.btnlyt2.addSpacing(35)
        self.btnlyt2.addWidget(QLabel("<span style='font-size:17px; font-family:SF Pro Display; color:rgb(99,99,102);'>Buttons with icons & spinners</span>"))
        self.btnlyt2.addSpacing(10)

        self.ibtnlyt = QHBoxLayout()
        self.btnlyt2.addLayout(self.ibtnlyt)

        self.ibtn = StyledButton("Image Icon", icon="data/homeiconw.png")
        self.ibtn.setFixedSize(140, 45)
        self.ibtn.anim_press.speed = 7.3
        self.ibtn.setStyleDict({
                "background-color" : (0, 122, 255),
                "border-color" : (0, 122, 255),
                "border-radius" : 7,
                "color" : (255, 255, 255),
                "font-family" : "SF Pro Display",
                "font-size" : 18,
            })
        self.ibtn.setStyleDict({
                "background-color" : (36, 141, 255),
                "border-color" : (36, 141, 255)
            }, "hover")
        self.ibtn.setStyleDict({
                "background-color" : (130, 190, 255),
                "border-color" : (130, 190, 255),
                "color" : (255, 255, 255),
            }, "press")

        s = Spinner(1.5, QColor(255, 255, 255))
        s.animType = 0
        s.speed = 2
        self.ibtn2 = StyledButton("Spinner Icon", icon=s)
        self.ibtn2.setFixedSize(140, 45)
        self.ibtn2.anim_press.speed = 7.3
        self.ibtn2.setStyleDict({
                "background-color" : (0, 122, 255),
                "border-color" : (0, 122, 255),
                "border-radius" : 7,
                "color" : (255, 255, 255),
                "font-family" : "SF Pro Display",
                "font-size" : 18,
            })
        self.ibtn2.setStyleDict({
                "background-color" : (36, 141, 255),
                "border-color" : (36, 141, 255)
            }, "hover")
        self.ibtn2.setStyleDict({
                "background-color" : (130, 190, 255),
                "border-color" : (130, 190, 255),
                "color" : (255, 255, 255),
            }, "press")

        self.ibtnlyt.addWidget(self.ibtn)
        self.ibtnlyt.addWidget(self.ibtn2)

        self.ibtnl = StyledButton("Loading", icon=Spinner(1.5, QColor(255, 255, 255)))
        self.ibtnl.setMinimumSize(118, 38)
        self.ibtnl.anim_press.speed = 7.3
        self.ibtnl.setStyleDict({
                "background-color" : (52, 199, 89),
                "border-color" : (2, 199, 89),
                "border-radius" :  39,
                "color" : (255, 255, 255),
                "font-family" : "SF Pro Display",
                "font-size" : 18,
            })
        self.ibtnl.setStyleDict({
                "background-color" : (47, 212, 119),
                "border-color" : (47, 212, 119)
            }, "hover")
        self.ibtnl.setStyleDict({
                "background-color" : (89, 227, 149),
                "border-color" : (89, 227, 149),
                "color" : (255, 255, 255),
            }, "press")

        self.btnlyt2.addSpacing(15)
        self.btnlyt2.addWidget(self.ibtnl, alignment=Qt.AlignHCenter)

        self.toast = Toast(self, text="Simple Toast with Spinner", icon=Spinner(1.3, QColor(255, 255, 255)))
        self.toast.setFixedWidth(287)
        self.toast.setStyleDict({
                "font-family" : "SF Pro Display",
                "font-size" : 17
            })

        self.ibtnl.clicked.connect(lambda: self.toast.rise(3))



if __name__ == "__main__":
    app = QApplication(sys.argv)

    mw = MainWindow()
    mw.show()

    sys.exit(app.exec_())
