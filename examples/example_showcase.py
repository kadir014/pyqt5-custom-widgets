#        PyQt5 Custom Widgets - Showcase Demo         #
#                    Kadir Aksoy                      #
#   https://github.com/kadir014/pyqt5-custom-widgets  #
#                                                     #
#    This script is one of the pyqt5Custom examples   #


import sys

from PyQt5.QtCore import Qt
from PyQt5.QtWidgets import QWidget, QApplication, QHBoxLayout, QVBoxLayout, QLabel, QFrame
from PyQt5.QtGui import QColor, QFontDatabase

from pyqt5Custom import ToggleSwitch, StyledButton, ImageBox, ColorPicker, ColorPreview, DragDropFile, EmbedWindow, TitleBar, CodeTextEdit, Spinner, SegmentedButtonGroup



class MainWindow(QWidget):
    def __init__(self):
        super().__init__()

        w, h = 950, 630
        self.setMinimumSize(w//6, h//6)
        self.setGeometry(100, 100, w, h)

        QFontDatabase.addApplicationFont("data/Montserrat-Regular.ttf")
        QFontDatabase.addApplicationFont("data/SourceCodePro-Regular.ttf")
        QFontDatabase.addApplicationFont("data/SFPro.ttf")

        self.setStyleSheet("QLabel {font-family: Montserrat-Regular;}")

        self.setAutoFillBackground(True)
        p = self.palette()
        p.setColor(self.backgroundRole(), QColor(254, 254, 254))
        self.setPalette(p)


        self.mainlayout = QVBoxLayout()
        self.mainlayout.setSpacing(0)
        self.mainlayout.setContentsMargins(0, 0, 0, 0)
        self.setLayout(self.mainlayout)

        self.titlebar = TitleBar(self, title="PyQt5 Custom Widgets Showcase")
        self.titlebar.setStyleDict({
            "color" : (0, 0, 0, 0),
            "font-family" : "Montserrat-Regular",
            "font-size" : 14
        })
        self.mainlayout.addWidget(self.titlebar)

        self.layout = QHBoxLayout()
        self.layout.setContentsMargins(0, 0, 0, 0)
        self.mainlayout.addLayout(self.layout)

        # Side menu
        self.menu_wdt = QWidget()
        self.menu_wdt.setFixedWidth(90)
        self.menu = QVBoxLayout()
        self.menu.setAlignment(Qt.AlignTop)
        self.menu.setSpacing(5)
        self.menu_wdt.setLayout(self.menu)
        self.layout.addWidget(self.menu_wdt)

        self.menu_wdt.setAutoFillBackground(True)
        p = self.menu_wdt.palette()
        p.setColor(self.menu_wdt.backgroundRole(), QColor(245, 66, 126))
        self.menu_wdt.setPalette(p)

        self.menubtn1 = StyledButton(icon="data/switchicon.png")
        self.menubtn2 = StyledButton(icon="data/buttonicon.png")
        self.menubtn3 = StyledButton(icon="data/imageicon.png")
        self.menubtn4 = StyledButton(icon="data/colorpckicon.png")
        self.menubtn5 = StyledButton(icon="data/dragdropicon.png")
        self.menubtn6 = StyledButton(icon="data/windowicon.png")
        self.menubtn7 = StyledButton(icon="data/codeicon.png")
        self.menubtn8 = StyledButton(icon="data/spinnericon.png")

        w, i = 60, 30

        self.menubtn1.setFixedSize(w, w)
        self.menubtn1.setIconSize(40, 40)
        self.menubtn1.setStyleDict({
            "background-color" : (245, 66, 126),
            "border-color" : (0, 0, 0, 0),
            "border-radius" : 14
        })
        self.menubtn1.setStyleDict({
            "background-color" : (245, 127, 167),
        }, "hover")
        self.menubtn1.setStyleDict({
            "background-color" : (255, 156, 189),
        }, "press")

        self.menubtn2.setFixedSize(w, w)
        self.menubtn2.setIconSize(i, i)
        self.menubtn2.copyStyleDict(self.menubtn1)

        self.menubtn3.setFixedSize(w, w)
        self.menubtn3.setIconSize(i, i)
        self.menubtn3.copyStyleDict(self.menubtn1)

        self.menubtn4.setFixedSize(w, w)
        self.menubtn4.setIconSize(i, i)
        self.menubtn4.copyStyleDict(self.menubtn1)

        self.menubtn5.setFixedSize(w, w)
        self.menubtn5.setIconSize(i, i)
        self.menubtn5.copyStyleDict(self.menubtn1)

        self.menubtn6.setFixedSize(w, w)
        self.menubtn6.setIconSize(i, i)
        self.menubtn6.copyStyleDict(self.menubtn1)

        self.menubtn7.setFixedSize(w, w)
        self.menubtn7.setIconSize(i, i)
        self.menubtn7.copyStyleDict(self.menubtn1)

        self.menubtn8.setFixedSize(w, w)
        self.menubtn8.setIconSize(i, i)
        self.menubtn8.copyStyleDict(self.menubtn1)

        self.menu.addSpacing(10)
        self.menu.addWidget(self.menubtn1, alignment=Qt.AlignTop|Qt.AlignCenter)
        self.menu.addWidget(self.menubtn2, alignment=Qt.AlignTop|Qt.AlignCenter)
        self.menu.addWidget(self.menubtn3, alignment=Qt.AlignTop|Qt.AlignCenter)
        self.menu.addWidget(self.menubtn4, alignment=Qt.AlignTop|Qt.AlignCenter)
        self.menu.addWidget(self.menubtn5, alignment=Qt.AlignTop|Qt.AlignCenter)
        self.menu.addWidget(self.menubtn6, alignment=Qt.AlignTop|Qt.AlignCenter)
        self.menu.addWidget(self.menubtn7, alignment=Qt.AlignTop|Qt.AlignCenter)
        self.menu.addWidget(self.menubtn8, alignment=Qt.AlignTop|Qt.AlignCenter)

        @self.menubtn1.clicked.connect
        def slot():
            self.togglesw_showcase_wdt.show()
            self.stbtn_showcase_wdt.hide()
            self.imgbox_showcase_wdt.hide()
            self.colorpk_showcase_wdt.hide()
            self.dropfile_showcase_wdt.hide()
            self.emwin_showcase_wdt.hide()
            self.codeedit_showcase_wdt.hide()
            self.spinner_showcase_wdt.hide()

        @self.menubtn2.clicked.connect
        def slot():
            self.togglesw_showcase_wdt.hide()
            self.stbtn_showcase_wdt.show()
            self.imgbox_showcase_wdt.hide()
            self.colorpk_showcase_wdt.hide()
            self.dropfile_showcase_wdt.hide()
            self.emwin_showcase_wdt.hide()
            self.codeedit_showcase_wdt.hide()
            self.spinner_showcase_wdt.hide()

        @self.menubtn3.clicked.connect
        def slot():
            self.togglesw_showcase_wdt.hide()
            self.stbtn_showcase_wdt.hide()
            self.imgbox_showcase_wdt.show()
            self.colorpk_showcase_wdt.hide()
            self.dropfile_showcase_wdt.hide()
            self.emwin_showcase_wdt.hide()
            self.codeedit_showcase_wdt.hide()
            self.spinner_showcase_wdt.hide()

        @self.menubtn4.clicked.connect
        def slot():
            self.togglesw_showcase_wdt.hide()
            self.stbtn_showcase_wdt.hide()
            self.imgbox_showcase_wdt.hide()
            self.colorpk_showcase_wdt.show()
            self.dropfile_showcase_wdt.hide()
            self.emwin_showcase_wdt.hide()
            self.codeedit_showcase_wdt.hide()
            self.spinner_showcase_wdt.hide()

        @self.menubtn5.clicked.connect
        def slot():
            self.togglesw_showcase_wdt.hide()
            self.stbtn_showcase_wdt.hide()
            self.imgbox_showcase_wdt.hide()
            self.colorpk_showcase_wdt.hide()
            self.dropfile_showcase_wdt.show()
            self.emwin_showcase_wdt.hide()
            self.codeedit_showcase_wdt.hide()
            self.spinner_showcase_wdt.hide()

        @self.menubtn6.clicked.connect
        def slot():
            self.togglesw_showcase_wdt.hide()
            self.stbtn_showcase_wdt.hide()
            self.imgbox_showcase_wdt.hide()
            self.colorpk_showcase_wdt.hide()
            self.dropfile_showcase_wdt.hide()
            self.emwin_showcase_wdt.show()
            self.codeedit_showcase_wdt.hide()
            self.spinner_showcase_wdt.hide()

        @self.menubtn7.clicked.connect
        def slot():
            self.togglesw_showcase_wdt.hide()
            self.stbtn_showcase_wdt.hide()
            self.imgbox_showcase_wdt.hide()
            self.colorpk_showcase_wdt.hide()
            self.dropfile_showcase_wdt.hide()
            self.emwin_showcase_wdt.hide()
            self.codeedit_showcase_wdt.show()
            self.spinner_showcase_wdt.hide()

        @self.menubtn8.clicked.connect
        def slot():
            self.togglesw_showcase_wdt.hide()
            self.stbtn_showcase_wdt.hide()
            self.imgbox_showcase_wdt.hide()
            self.colorpk_showcase_wdt.hide()
            self.dropfile_showcase_wdt.hide()
            self.emwin_showcase_wdt.hide()
            self.codeedit_showcase_wdt.hide()
            self.spinner_showcase_wdt.show()


        ##################################################
        #                                                #
        #              ToggleSwitch Widget               #
        #                                                #
        ##################################################

        self.togglesw_showcase_wdt = QWidget()
        self.togglesw_showcase_wdt.setStyleSheet("font-family: Montserrat-Regular; font-size: 15px;")
        self.togglesw_showcase_lyt = QVBoxLayout()
        self.togglesw_showcase_lyt.setSpacing(5)
        self.togglesw_showcase_lyt.setAlignment(Qt.AlignTop|Qt.AlignHCenter)
        self.togglesw_showcase_wdt.setLayout(self.togglesw_showcase_lyt)
        self.togglesw_showcase_lyt.addWidget(QLabel("<span style='font-size:30px;'>Toggle Switch</span>"),
                                            alignment=Qt.AlignHCenter)
        self.togglesw_showcase_lyt.addWidget(QLabel("<span style='font-size:15px; color:#777777;'>These are styled & animated toggle switches.</span>"),
                                            alignment=Qt.AlignHCenter)

        self.togglesw_showcase_lyt.addSpacing(140)

        self.togglesw_content_lyt = QHBoxLayout()
        self.togglesw_showcase_lyt.addLayout(self.togglesw_content_lyt)

        self.togglesw_style1_lyt = QVBoxLayout()
        self.togglesw_style1_lyt.setAlignment(Qt.AlignTop|Qt.AlignHCenter)
        self.togglesw_style1_lyt.setSpacing(15)
        self.togglesw_content_lyt.addLayout(self.togglesw_style1_lyt)
        self.togglesw_style2_lyt = QVBoxLayout()
        self.togglesw_style2_lyt.setAlignment(Qt.AlignTop|Qt.AlignHCenter)
        self.togglesw_style2_lyt.setSpacing(15)
        self.togglesw_content_lyt.addLayout(self.togglesw_style2_lyt)
        self.togglesw_style3_lyt = QVBoxLayout()
        self.togglesw_style3_lyt.setAlignment(Qt.AlignTop|Qt.AlignHCenter)
        self.togglesw_style3_lyt.setSpacing(15)
        self.togglesw_content_lyt.addLayout(self.togglesw_style3_lyt)


        # Windows 10 Styled Toggle Switch
        self.togglesw_style1_lyt.addWidget(QLabel("<span style='font-size:20px;'>Windows 10</span>"),
                                           alignment=Qt.AlignHCenter)
        self.togglesw_style1_lyt.addSpacing(35)

        self.togglesw_style1_off = ToggleSwitch(text="Off",          style="win10")
        self.togglesw_style1_on  = ToggleSwitch(text="On",           style="win10", on=True)
        self.togglesw_style1_en  = ToggleSwitch(text="Disabled off", style="win10")
        self.togglesw_style1_di  = ToggleSwitch(text="Disabled on",  style="win10", on=True)
        self.togglesw_style1_en.setEnabled(False)
        self.togglesw_style1_di.setEnabled(False)

        self.togglesw_style1_lyt.addWidget(self.togglesw_style1_off)
        self.togglesw_style1_lyt.addWidget(self.togglesw_style1_on)
        self.togglesw_style1_lyt.addWidget(self.togglesw_style1_en)
        self.togglesw_style1_lyt.addWidget(self.togglesw_style1_di)


        # iOS Styled Toggle Switch
        self.togglesw_style2_lyt.addWidget(QLabel("<span style='font-size:20px;'>iOS</span>"),
                                           alignment=Qt.AlignHCenter)
        self.togglesw_style2_lyt.addSpacing(35)

        self.togglesw_style2_off = ToggleSwitch(text="Off",          style="ios")
        self.togglesw_style2_on  = ToggleSwitch(text="On",           style="ios", on=True)
        self.togglesw_style2_en  = ToggleSwitch(text="Disabled off", style="ios")
        self.togglesw_style2_di  = ToggleSwitch(text="Disabled on",  style="ios", on=True)
        self.togglesw_style2_en.setEnabled(False)
        self.togglesw_style2_di.setEnabled(False)

        self.togglesw_style2_lyt.addWidget(self.togglesw_style2_off)
        self.togglesw_style2_lyt.addWidget(self.togglesw_style2_on)
        self.togglesw_style2_lyt.addWidget(self.togglesw_style2_en)
        self.togglesw_style2_lyt.addWidget(self.togglesw_style2_di)


        # Android Styled Toggle Switch
        self.togglesw_style3_lyt.addWidget(QLabel("<span style='font-size:20px;'>Android</span>"),
                                           alignment=Qt.AlignHCenter)
        self.togglesw_style3_lyt.addSpacing(35)

        self.togglesw_style3_off = ToggleSwitch(text="Off",          style="android")
        self.togglesw_style3_on  = ToggleSwitch(text="On",           style="android", on=True)
        self.togglesw_style3_en  = ToggleSwitch(text="Disabled off", style="android")
        self.togglesw_style3_di  = ToggleSwitch(text="Disabled on",  style="android", on=True)
        self.togglesw_style3_en.setEnabled(False)
        self.togglesw_style3_di.setEnabled(False)

        self.togglesw_style3_lyt.addWidget(self.togglesw_style3_off)
        self.togglesw_style3_lyt.addWidget(self.togglesw_style3_on)
        self.togglesw_style3_lyt.addWidget(self.togglesw_style3_en)
        self.togglesw_style3_lyt.addWidget(self.togglesw_style3_di)


        ##################################################
        #                                                #
        #              StyledButton Widget               #
        #                                                #
        ##################################################

        self.stbtn_showcase_wdt = QWidget()
        self.stbtn_showcase_wdt.setStyleSheet("font-family: Montserrat-Regular; font-size:15px;")
        self.stbtn_showcase_lyt = QVBoxLayout()
        self.stbtn_showcase_lyt.setSpacing(5)
        self.stbtn_showcase_lyt.setAlignment(Qt.AlignTop|Qt.AlignHCenter)
        self.stbtn_showcase_wdt.setLayout(self.stbtn_showcase_lyt)

        self.stbtn_showcase_lyt.addWidget(QLabel("<span style='font-size:30px;'>Styled Buttons</span>"),
                                          alignment=Qt.AlignHCenter)
        self.stbtn_showcase_lyt.addWidget(QLabel("<span style='font-size:15px; color:#777777;'>These are styled & animated buttons.</span>"),
                                          alignment=Qt.AlignHCenter)

        self.stbtn_showcase_lyt.addSpacing(80)

        self.stbtn_content_lyt = QHBoxLayout()
        self.stbtn_content_lyt.setSpacing(60)
        self.stbtn_showcase_lyt.addLayout(self.stbtn_content_lyt)

        self.stbtn_style1_lyt = QVBoxLayout()
        self.stbtn_style1_lyt.setAlignment(Qt.AlignTop|Qt.AlignHCenter)
        self.stbtn_style1_lyt.setSpacing(15)
        self.stbtn_content_lyt.addLayout(self.stbtn_style1_lyt)

        self.stbtn_style2_lyt = QVBoxLayout()
        self.stbtn_style2_lyt.setAlignment(Qt.AlignTop|Qt.AlignHCenter)
        self.stbtn_style2_lyt.setSpacing(15)
        self.stbtn_content_lyt.addLayout(self.stbtn_style2_lyt)

        self.stbtn_style3_lyt = QVBoxLayout()
        self.stbtn_style3_lyt.setAlignment(Qt.AlignTop|Qt.AlignHCenter)
        self.stbtn_style3_lyt.setSpacing(15)
        self.stbtn_content_lyt.addLayout(self.stbtn_style3_lyt)


        self.stbtn_style1_lyt.addWidget(QLabel("<span style='font-size:20px;'>Default style</span>"),
                                        alignment=Qt.AlignHCenter)
        self.stbtn_style1_lyt.addSpacing(35)

        self.stbtn_style1      = StyledButton(text="Button")
        self.stbtn_style1_icon = StyledButton(text="Icon", icon="data/homeicon.png")
        self.stbtn_style1_spn = StyledButton(text="Spinner", icon=Spinner(2, QColor(0, 0, 0)))
        self.stbtn_style1_shad = StyledButton(text="Drop shadow")
        self.stbtn_style1_shad.setStyleDict({
                "drop-shadow-radius" : 7,
                "drop-shadow-offset" : (0, 2)
            })

        self.stbtn_style1_lyt.addWidget(self.stbtn_style1)
        self.stbtn_style1_lyt.addWidget(self.stbtn_style1_icon)
        self.stbtn_style1_lyt.addWidget(self.stbtn_style1_spn)
        self.stbtn_style1_lyt.addWidget(self.stbtn_style1_shad)


        self.stbtn_style2_lyt.addWidget(QLabel("<span style='font-size:20px;'>Shadow interactions</span>"),
                                        alignment=Qt.AlignHCenter)
        self.stbtn_style2_lyt.addSpacing(35)

        self.stbtn_style2_1 = StyledButton(text="Shadow on hover")
        self.stbtn_style2_2 = StyledButton(text="Shadow on press")
        self.stbtn_style2_3 = StyledButton(text="Shadow on idle")
        self.stbtn_style2_4 = StyledButton(text="Changing offset")

        self.stbtn_style2_1.setStyleDict({
            "drop-shadow-radius" : 10,
            "drop-shadow-offset" : (0, 3)
        }, "hover")

        self.stbtn_style2_2.setStyleDict({
            "drop-shadow-radius" : 10,
            "drop-shadow-offset" : (0, 3)
        }, "press")

        self.stbtn_style2_3.setStyleDict({
            "drop-shadow-radius" : 10,
            "drop-shadow-offset" : (0, 3)
        }, "default")

        self.stbtn_style2_4.setStyleDict({
            "drop-shadow-radius" : 10,
            "drop-shadow-offset" : (0, 3)
        })
        self.stbtn_style2_4.setStyleDict({
            "drop-shadow-offset" : (3, 0)
        }, "hover")
        self.stbtn_style2_4.setStyleDict({
            "drop-shadow-offset" : (-1.5, -1.5)
        }, "press")

        self.stbtn_style2_lyt.addWidget(self.stbtn_style2_1)
        self.stbtn_style2_lyt.addWidget(self.stbtn_style2_2)
        self.stbtn_style2_lyt.addWidget(self.stbtn_style2_3)
        self.stbtn_style2_lyt.addWidget(self.stbtn_style2_4)


        self.stbtn_style3_lyt.addWidget(QLabel("<span style='font-size:20px;'>Variations</span>"),
                                        alignment=Qt.AlignHCenter)
        self.stbtn_style3_lyt.addSpacing(35)

        self.stbtn_style3_1 = StyledButton(text="iOS styled")
        self.stbtn_style3_2 = StyledButton(text="Pill shaped")
        self.stbtn_style3_3 = StyledButton(text="✕")
        self.stbtn_style3_4 = StyledButton(text="Only text")

        self.stbtn_style3_1.setStyleDict({
            "border-radius" : 4,
            "border-color" : (0, 122, 255),
            "color" : (0, 122, 255)
        })
        self.stbtn_style3_1.setStyleDict({
            "background-color" : (255, 255, 255),
            "border-color" : (0, 172, 255),
            "color" : (0, 172, 255)
        }, "hover")
        self.stbtn_style3_1.setStyleDict({
            "background-color" : (0, 122, 255),
            "border-color" : (0, 122, 255),
            "color" : (255, 255, 255)
        }, "press")

        self.stbtn_style3_2.setStyleDict({
            "border-radius" : 100
        })

        self.stbtn_style3_3.setFixedSize(52, 52)
        self.stbtn_style3_3.setStyleDict({
            "border-radius" : 100,
            "border-color" : (0, 0, 0, 0),
            "background-color" : (241, 241, 241),
            "font-size" : 24
        })
        self.stbtn_style3_3.setStyleDict({
            "background-color": (200, 0, 0),
            "color" : (255, 255, 255)
        }, "hover")
        self.stbtn_style3_3.setStyleDict({
            "background-color": (255, 0, 0),
            "color" : (255, 255, 255)
        }, "press")

        self.stbtn_style3_4.setStyleDict({
            "border-color" : (0, 0, 0, 0),
            "background-color" : (0, 0, 0, 0)
        })

        self.stbtn_style3_lyt.addWidget(self.stbtn_style3_1)
        self.stbtn_style3_lyt.addWidget(self.stbtn_style3_2)
        self.stbtn_style3_lyt.addWidget(self.stbtn_style3_3)
        self.stbtn_style3_lyt.addWidget(self.stbtn_style3_4)


        ##################################################
        #                                                #
        #                ImageBox Widget                 #
        #                                                #
        ##################################################

        self.imgbox_showcase_wdt = QWidget()
        self.imgbox_showcase_lyt = QVBoxLayout()
        self.imgbox_showcase_lyt.setSpacing(5)
        self.imgbox_showcase_lyt.setAlignment(Qt.AlignTop|Qt.AlignHCenter)
        self.imgbox_showcase_wdt.setLayout(self.imgbox_showcase_lyt)

        self.imgbox_showcase_lyt.addWidget(QLabel("<span style='font-size:30px;'>Image Box</span>"),
                                           alignment=Qt.AlignHCenter)
        self.imgbox_showcase_lyt.addWidget(QLabel("<span style='font-size:15px; color:#777777;'>Image boxes are simply widgets to hold visual content, such as PNG, JPG and GIF files.</span>"),
                                           alignment=Qt.AlignHCenter)

        self.imgbox_showcase_lyt.addSpacing(45)

        self.imgbox_hstatic_lyt = QHBoxLayout()
        self.imgbox_hstatic_lyt.setAlignment(Qt.AlignHCenter)
        self.imgbox_showcase_lyt.addLayout(self.imgbox_hstatic_lyt)

        self.imgbox_static1_lyt = QVBoxLayout()
        self.imgbox_static1_lyt.setAlignment(Qt.AlignHCenter)
        self.imgbox_hstatic_lyt.addLayout(self.imgbox_static1_lyt)

        self.imgbox_hstatic_lyt.addSpacing(100)

        self.imgbox_static1 = ImageBox("data/image.jpg", keepAspectRatio=True)
        self.imgbox_static1.setFixedSize(110, 110)
        self.imgbox_static1_lbl = QLabel("<span style='font-size:14px; color:#888888'>Aspect ratio protected</span>")
        self.imgbox_static1_lyt.addWidget(self.imgbox_static1)
        self.imgbox_static1_lyt.addWidget(self.imgbox_static1_lbl, alignment=Qt.AlignHCenter)

        self.imgbox_static2_lyt = QVBoxLayout()
        self.imgbox_static2_lyt.setAlignment(Qt.AlignHCenter)
        self.imgbox_hstatic_lyt.addLayout(self.imgbox_static2_lyt)

        self.imgbox_static2 = ImageBox("data/image.jpg", keepAspectRatio=False)
        self.imgbox_static2.setFixedSize(110, 110)
        self.imgbox_static2_lbl = QLabel("<span style='font-size:14px; color:#888888'>Aspect ratio ignored</span>")
        self.imgbox_static2_lyt.addWidget(self.imgbox_static2)
        self.imgbox_static2_lyt.addWidget(self.imgbox_static2_lbl, alignment=Qt.AlignHCenter)

        self.imgbox_showcase_lyt.addSpacing(80)

        self.imgbox_showcase_lyt.addWidget(QLabel("<span style='font-size:15px; color:#777777;'>You can also use animated GIFs.</span>"),
                                           alignment=Qt.AlignHCenter)

        self.imgbox_animated = ImageBox("data/luffy.gif")
        self.imgbox_animated.setFixedSize(250, 210)
        self.imgbox_showcase_lyt.addWidget(self.imgbox_animated, alignment=Qt.AlignHCenter)


        ##################################################
        #                                                #
        #               ColorPicker Widget               #
        #                                                #
        ##################################################

        self.colorpk_showcase_wdt = QWidget()
        self.colorpk_showcase_lyt = QVBoxLayout()
        self.colorpk_showcase_lyt.setSpacing(5)
        self.colorpk_showcase_lyt.setAlignment(Qt.AlignTop|Qt.AlignHCenter)
        self.colorpk_showcase_wdt.setLayout(self.colorpk_showcase_lyt)

        self.colorpk_showcase_lyt.addWidget(QLabel("<span style='font-size:30px;'>Color Picker</span>"),
                                           alignment=Qt.AlignHCenter)
        self.colorpk_showcase_lyt.addWidget(QLabel("<span style='font-size:15px; color:#777777;'>Color Picker widget simply lets you to choose a color from the wheel.</span>"),
                                           alignment=Qt.AlignHCenter)

        self.colorpk_showcase_lyt.addSpacing(85)

        self.colorpk_hori_lyt = QHBoxLayout()
        self.colorpk_showcase_lyt.addLayout(self.colorpk_hori_lyt)

        self.colorpk_picker = ColorPicker()
        self.colorpk_hori_lyt.addWidget(self.colorpk_picker)

        self.colorpk_cpre = ColorPreview()
        self.colorpk_hori_lyt.addWidget(self.colorpk_cpre)

        self.colorpk_picker.colorChanged.connect(self.colorpk_cpre.setColor)


        ##################################################
        #                                                #
        #              DragDropFile Widget               #
        #                                                #
        ##################################################

        self.dropfile_showcase_wdt = QWidget()
        self.dropfile_showcase_lyt = QVBoxLayout()
        self.dropfile_showcase_lyt.setSpacing(5)
        self.dropfile_showcase_lyt.setAlignment(Qt.AlignTop|Qt.AlignHCenter)
        self.dropfile_showcase_wdt.setLayout(self.dropfile_showcase_lyt)

        self.dropfile_showcase_lyt.addWidget(QLabel("<span style='font-size:30px;'>File Drag & Drop</span>"),
                                           alignment=Qt.AlignHCenter)
        self.dropfile_showcase_lyt.addWidget(QLabel("<span style='font-size:15px; color:#777777;'>Drag files and drop on this widget.</span>"),
                                           alignment=Qt.AlignHCenter)

        self.dropfile_showcase_lyt.addSpacing(140)

        self.dropfile = DragDropFile()
        self.dropfile.setFixedSize(300, 210)
        self.dropfile_showcase_lyt.addWidget(self.dropfile)


        ##################################################
        #                                                #
        #              EmbedWindow Widget                #
        #                                                #
        ##################################################

        self.emwin_showcase_wdt = QWidget()
        self.emwin_showcase_lyt = QVBoxLayout()
        self.emwin_showcase_lyt.setSpacing(5)
        self.emwin_showcase_lyt.setAlignment(Qt.AlignTop|Qt.AlignHCenter)
        self.emwin_showcase_wdt.setLayout(self.emwin_showcase_lyt)

        self.emwin_showcase_lyt.addWidget(QLabel("<span style='font-size:30px;'>Embed Window</span>"),
                                           alignment=Qt.AlignHCenter)
        self.emwin_showcase_lyt.addWidget(QLabel("<span style='font-size:15px; color:#777777;'>A pop-up dialog, but actually embed.</span>"),
                                           alignment=Qt.AlignHCenter)

        self.emwin_showcase_lyt.addSpacing(70)

        self.emwin_spawner = StyledButton("Click here to spawn embed windows")
        self.emwin_spawner.setFixedHeight(33)
        self.emwin_showcase_lyt.addWidget(self.emwin_spawner)

        self.emwin_windows = list()

        # Parent is main window
        @self.emwin_spawner.clicked.connect
        def slot():
            ewl = QLabel("<span style='color:#333333; font-size: 15px;'>My parent is the top-level widget so I can move anywhere 😎</span>")
            ewl.setWordWrap(True)
            ew = EmbedWindow(self)
            ew.content.addWidget(ewl)
            ew.closed.connect(lambda: self.emwin_windows.remove(ew))
            self.emwin_windows.append(ew)
            ew.show()
            ew.raise_()

        self.emwin_showcase_lyt.addSpacing(30)

        self.emwin_showcase_lyt.addWidget(QLabel("<span style='font-size:14px; color: #999999;'>There is a QFrame with invisible borders</span>"))

        self.emwin_frame = QFrame()
        self.emwin_frame.setFixedSize(400, 300)
        self.emwin_showcase_lyt.addWidget(self.emwin_frame)

        #Parent is QFrame
        self.emwin_frame_window = EmbedWindow(self.emwin_frame)
        lb = QLabel("My parent is this QFrame so I'm embed here and can't get out!")
        lb.setStyleSheet("color:#333333; font-size: 15px;")
        lb.setWordWrap(True)
        self.emwin_frame_window.content.addWidget(lb)


        ##################################################
        #                                                #
        #              CodeTextEdit Widget               #
        #                                                #
        ##################################################

        self.codeedit_showcase_wdt = QWidget()
        self.codeedit_showcase_lyt = QVBoxLayout()
        self.codeedit_showcase_lyt.setSpacing(5)
        self.codeedit_showcase_lyt.setAlignment(Qt.AlignTop|Qt.AlignHCenter)
        self.codeedit_showcase_wdt.setLayout(self.codeedit_showcase_lyt)

        self.codeedit_showcase_lyt.addWidget(QLabel("<span style='font-size:30px;'>Code Editor</span>"),
                                           alignment=Qt.AlignHCenter)
        self.codeedit_showcase_lyt.addWidget(QLabel("<span style='font-size:15px; color:#777777;'>CodeTextEdit widget is simply a syntax-highlighted editor</span>"),
                                           alignment=Qt.AlignHCenter)
        self.codeedit_showcase_lyt.addWidget(QLabel("<span style='font-size:15px; color:#777777;'>Currently it only supports few languages</span>"),
                                           alignment=Qt.AlignHCenter)

        self.codeedit_showcase_lyt.addSpacing(34)

        self.codeedit_filedrop = DragDropFile()
        self.codeedit_filedrop.setTitle("Drop source file")
        self.codeedit_filedrop.setFixedSize(410, 64)
        self.codeedit_filedrop.borderRadius = 6
        self.codeedit_filedrop.borderWidth = 3
        self.codeedit_showcase_lyt.addWidget(self.codeedit_filedrop, alignment=Qt.AlignHCenter)

        self.codeedit_showcase_lyt.addSpacing(9)

        @self.codeedit_filedrop.fileDropped.connect
        def slot(file):
            self.codeedit.loadFile(file.path)

        self.codeedit = CodeTextEdit()
        self.codeedit.setFixedSize(510, 300)
        self.codeedit.setStyleSheet("QPlainTextEdit {font-size:17px; font-family: Source Code Pro;}")
        self.codeedit.loadFile("example.cpp")
        self.codeedit.setTheme("one-dark")
        self.codeedit_showcase_lyt.addWidget(self.codeedit, alignment=Qt.AlignHCenter|Qt.AlignTop)

        self.codeedit_showcase_lyt.addSpacing(9)

        self.codeedit_theme_btngrp = SegmentedButtonGroup(radio=True)
        self.codeedit_theme_btngrp.setFixedHeight(32)

        self.codeedit_theme_btngrp.addButton("Default",   tag=0)
        self.codeedit_theme_btngrp.addButton("One Light", tag=1)
        self.codeedit_theme_btngrp.addButton("One Dark",  tag=2)
        self.codeedit_theme_btngrp.addButton("Monokai",   tag=3)
        self.codeedit_theme_btngrp.addButton("Oceanic",   tag=4)
        self.codeedit_theme_btngrp.addButton("Zenburn",   tag=5)

        self.codeedit_theme_btngrp.getByTag(2).setChecked(True)

        @self.codeedit_theme_btngrp.clicked.connect
        def slot(tag):
            btn = self.codeedit_theme_btngrp.getByTag(tag)
            self.codeedit.setTheme(btn.text().lower().replace(" ", "-"))

        self.codeedit_showcase_lyt.addWidget(self.codeedit_theme_btngrp)


        ##################################################
        #                                                #
        #                Spinner Widget                  #
        #                                                #
        ##################################################

        self.spinner_showcase_wdt = QWidget()
        self.spinner_showcase_lyt = QVBoxLayout()
        self.spinner_showcase_lyt.setSpacing(5)
        self.spinner_showcase_lyt.setAlignment(Qt.AlignTop|Qt.AlignHCenter)
        self.spinner_showcase_wdt.setLayout(self.spinner_showcase_lyt)

        self.spinner_showcase_lyt.addWidget(QLabel("<span style='font-size:30px;'>Spinner</span>"),
                                           alignment=Qt.AlignHCenter)
        self.spinner_showcase_lyt.addWidget(QLabel("<span style='font-size:15px; color:#777777;'>It's spinning! You can use this widget as icon argument.</span>"),
                                           alignment=Qt.AlignHCenter)

        self.spinner_showcase_lyt.addSpacing(70)

        self.spinner_row1 = QHBoxLayout()
        self.spinner_row2 = QHBoxLayout()
        self.spinner_row3 = QHBoxLayout()
        self.spinner_row4 = QHBoxLayout()
        self.spinner_showcase_lyt.addLayout(self.spinner_row1)
        self.spinner_showcase_lyt.addSpacing(15)
        self.spinner_showcase_lyt.addLayout(self.spinner_row2)
        self.spinner_showcase_lyt.addSpacing(15)
        self.spinner_showcase_lyt.addLayout(self.spinner_row3)
        self.spinner_showcase_lyt.addSpacing(15)
        self.spinner_showcase_lyt.addLayout(self.spinner_row4)


        self.spinner_style1_1 = Spinner(1.5, QColor(0, 0, 0))
        self.spinner_style1_1.setFixedSize(18, 18)

        self.spinner_style1_2 = Spinner(1.5, QColor(0, 0, 0))
        self.spinner_style1_2.setFixedSize(36, 36)

        self.spinner_style1_3 = Spinner(1.5, QColor(0, 0, 0))
        self.spinner_style1_3.setFixedSize(78, 78)

        self.spinner_row1.addWidget(QLabel("<span style='font-size:17px; color:#444444;'>Fixed Width</span>"))
        self.spinner_row1.addWidget(self.spinner_style1_1)
        self.spinner_row1.addSpacing(20)
        self.spinner_row1.addWidget(self.spinner_style1_2)
        self.spinner_row1.addSpacing(20)
        self.spinner_row1.addWidget(self.spinner_style1_3)


        self.spinner_style2_1 = Spinner(1.5, QColor(0, 0, 0))
        self.spinner_style2_1.setFixedSize(18, 18)

        self.spinner_style2_2 = Spinner(6.0, QColor(0, 0, 0))
        self.spinner_style2_2.setFixedSize(36, 36)

        self.spinner_style2_3 = Spinner(18, QColor(0, 0, 0))
        self.spinner_style2_3.setFixedSize(78, 78)

        self.spinner_row2.addWidget(QLabel("<span style='font-size:17px; color:#444444;'>Increasing width</span>"))
        self.spinner_row2.addWidget(self.spinner_style2_1)
        self.spinner_row2.addSpacing(20)
        self.spinner_row2.addWidget(self.spinner_style2_2)
        self.spinner_row2.addSpacing(20)
        self.spinner_row2.addWidget(self.spinner_style2_3)


        self.spinner_style3_1 = Spinner(2, QColor(0, 0, 0))
        self.spinner_style3_1.animType = 0
        self.spinner_style3_1.setFixedSize(18, 18)

        self.spinner_style3_2 = Spinner(2, QColor(0, 0, 0))
        self.spinner_style3_2.animType = 0
        self.spinner_style3_2.setFixedSize(36, 36)

        self.spinner_style3_3 = Spinner(2, QColor(0, 0, 0))
        self.spinner_style3_3.animType = 0
        self.spinner_style3_3.setFixedSize(78, 78)

        self.spinner_row3.addWidget(QLabel("<span style='font-size:17px; color:#444444;'>Boring animation type</span>"))
        self.spinner_row3.addWidget(self.spinner_style3_1)
        self.spinner_row3.addSpacing(20)
        self.spinner_row3.addWidget(self.spinner_style3_2)
        self.spinner_row3.addSpacing(20)
        self.spinner_row3.addWidget(self.spinner_style3_3)


        self.spinner_style4_1 = Spinner(4, QColor(255, 0, 0))
        self.spinner_style4_1.animType = 0
        self.spinner_style4_1.speed = 1.2
        self.spinner_style4_1.setFixedSize(24, 24)

        self.spinner_style4_2 = Spinner(2, QColor(0, 255, 20))
        self.spinner_style4_2.setFixedSize(36, 36)

        self.spinner_style4_3 = Spinner(5, QColor(0, 55, 255))
        self.spinner_style4_3.speed = 12
        self.spinner_style4_3.setFixedSize(55, 55)

        self.spinner_row4.addWidget(QLabel("<span style='font-size:15px; color:#444444;'>Variations</span>"))
        self.spinner_row4.addWidget(self.spinner_style4_1)
        self.spinner_row4.addSpacing(25)
        self.spinner_row4.addWidget(self.spinner_style4_2)
        self.spinner_row4.addSpacing(45)
        self.spinner_row4.addWidget(self.spinner_style4_3)


        # finalize layout
        self.layout.addWidget(self.togglesw_showcase_wdt)
        self.layout.addWidget(self.stbtn_showcase_wdt)
        self.layout.addWidget(self.imgbox_showcase_wdt)
        self.layout.addWidget(self.colorpk_showcase_wdt)
        self.layout.addWidget(self.dropfile_showcase_wdt)
        self.layout.addWidget(self.emwin_showcase_wdt)
        self.layout.addWidget(self.codeedit_showcase_wdt)
        self.layout.addWidget(self.spinner_showcase_wdt)

        self.togglesw_showcase_wdt.show()
        self.stbtn_showcase_wdt.hide()
        self.imgbox_showcase_wdt.hide()
        self.colorpk_showcase_wdt.hide()
        self.dropfile_showcase_wdt.hide()
        self.emwin_showcase_wdt.hide()
        self.codeedit_showcase_wdt.hide()
        self.spinner_showcase_wdt.hide()



if __name__ == "__main__":
    app = QApplication(sys.argv)

    mw = MainWindow()
    mw.show()

    sys.exit(app.exec_())
