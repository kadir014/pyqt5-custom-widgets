#        PyQt5 Custom Widgets - Showcase Demo         #
#                    Kadir Aksoy                      #
#   https://github.com/kadir014/pyqt5-custom-widgets  #


import sys

from PyQt5.QtCore import Qt
from PyQt5.QtWidgets import QWidget, QApplication, QHBoxLayout, QVBoxLayout, QLabel
from PyQt5.QtGui import QColor, QFontDatabase

from customwidgets import ToggleSwitch, StyledButton, ImageBox, ColorPicker, ColorPreview



class MainWindow(QWidget):
    def __init__(self):
        super().__init__()

        w, h = 950, 630
        self.setMinimumSize(w, h)
        self.setGeometry(100, 100, w, h)
        self.setWindowTitle("PyQt5 Custom Widgets Showcase")

        QFontDatabase.addApplicationFont("data/Montserrat-Regular.ttf")
        self.setStyleSheet("QLabel {font-family: Montserrat-Regular;}")

        self.setAutoFillBackground(True)
        p = self.palette()
        p.setColor(self.backgroundRole(), QColor(252, 252, 252))
        self.setPalette(p)


        self.layout = QHBoxLayout()
        self.layout.setContentsMargins(0, 0, 0, 0)
        self.setLayout(self.layout)

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

        self.menubtn1.resize(70, 70)
        self.menubtn1.borderColor = QColor(245, 66, 126)
        self.menubtn1.backgroundColor = QColor(245, 66, 126)
        self.menubtn1.circleColor = self.menubtn1.borderColor.lighter(146)
        self.menubtn1.borderRadius = 14
        self.menubtn1.hoverLighter = True
        self.menubtn1.hoverFactor = 3.8

        self.menubtn2.resize(70, 70)
        self.menubtn2.borderColor = QColor(245, 66, 126)
        self.menubtn2.backgroundColor = QColor(245, 66, 126)
        self.menubtn2.circleColor = self.menubtn2.borderColor.lighter(146)
        self.menubtn2.borderRadius = 14
        self.menubtn2.hoverLighter = True
        self.menubtn2.hoverFactor = 3.8

        self.menubtn3.resize(70, 70)
        self.menubtn3.borderColor = QColor(245, 66, 126)
        self.menubtn3.backgroundColor = QColor(245, 66, 126)
        self.menubtn3.circleColor = self.menubtn3.borderColor.lighter(146)
        self.menubtn3.borderRadius = 14
        self.menubtn3.hoverLighter = True
        self.menubtn3.hoverFactor = 3.8

        self.menubtn4.resize(70, 70)
        self.menubtn4.borderColor = QColor(245, 66, 126)
        self.menubtn4.backgroundColor = QColor(245, 66, 126)
        self.menubtn4.circleColor = self.menubtn4.borderColor.lighter(146)
        self.menubtn4.borderRadius = 14
        self.menubtn4.hoverLighter = True
        self.menubtn4.hoverFactor = 3.8

        self.menu.addSpacing(10)
        self.menu.addWidget(self.menubtn1, alignment=Qt.AlignTop|Qt.AlignCenter)
        self.menu.addWidget(self.menubtn2, alignment=Qt.AlignTop|Qt.AlignCenter)
        self.menu.addWidget(self.menubtn3, alignment=Qt.AlignTop|Qt.AlignCenter)
        self.menu.addWidget(self.menubtn4, alignment=Qt.AlignTop|Qt.AlignCenter)

        @self.menubtn1.clicked.connect
        def slot():
            self.togglesw_showcase_wdt.show()
            self.stbtn_showcase_wdt.hide()
            self.imgbox_showcase_wdt.hide()
            self.colorpk_showcase_wdt.hide()

        @self.menubtn2.clicked.connect
        def slot():
            self.togglesw_showcase_wdt.hide()
            self.stbtn_showcase_wdt.show()
            self.imgbox_showcase_wdt.hide()
            self.colorpk_showcase_wdt.hide()

        @self.menubtn3.clicked.connect
        def slot():
            self.togglesw_showcase_wdt.hide()
            self.stbtn_showcase_wdt.hide()
            self.imgbox_showcase_wdt.show()
            self.colorpk_showcase_wdt.hide()

        @self.menubtn4.clicked.connect
        def slot():
            self.togglesw_showcase_wdt.hide()
            self.stbtn_showcase_wdt.hide()
            self.imgbox_showcase_wdt.hide()
            self.colorpk_showcase_wdt.show()


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

        # Flat styled button
        self.stbtn_style1_lyt.addWidget(QLabel("<span style='font-size:20px;'>Flat</span>"),
                                        alignment=Qt.AlignHCenter)
        self.stbtn_style1_lyt.addSpacing(35)

        self.stbtn_style1      = StyledButton(text="Flat styled", style="flat")
        self.stbtn_style1_icon = StyledButton(text="Icon",        style="flat", icon="data/homeicon.png")
        self.stbtn_style1_shad = StyledButton(text="Drop shadow", style="flat")
        self.stbtn_style1_di   = StyledButton(text="Disabled",    style="flat")
        self.stbtn_style1_shad.setDropShadow(True)
        self.stbtn_style1_di.setEnabled(False)

        self.stbtn_style1_lyt.addWidget(self.stbtn_style1)
        self.stbtn_style1_lyt.addWidget(self.stbtn_style1_icon)
        self.stbtn_style1_lyt.addWidget(self.stbtn_style1_shad)
        self.stbtn_style1_lyt.addWidget(self.stbtn_style1_di)

        # Hyper styled button
        self.stbtn_style2_lyt.addWidget(QLabel("<span style='font-size:20px;'>Hyper</span>"),
                                        alignment=Qt.AlignHCenter)
        self.stbtn_style2_lyt.addSpacing(35)

        self.stbtn_style2      = StyledButton(text="Hyper styled", style="hyper")
        self.stbtn_style2_icon = StyledButton(text="Icon",         style="hyper", icon="data/homeicon.png")
        self.stbtn_style2_shad = StyledButton(text="Fixed bottom", style="hyper", fixedBottom=True)
        self.stbtn_style2_di   = StyledButton(text="Disabled",     style="hyper", fixedBottom=True)
        self.stbtn_style2_di.setEnabled(False)

        self.stbtn_style2_lyt.addWidget(self.stbtn_style2)
        self.stbtn_style2_lyt.addWidget(self.stbtn_style2_icon)
        self.stbtn_style2_lyt.addWidget(self.stbtn_style2_shad)
        self.stbtn_style2_lyt.addWidget(self.stbtn_style2_di)


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
        self.imgbox_static1.scale(0.35)
        self.imgbox_static1_lbl = QLabel("<span style='font-size:14px; color:#888888'>Aspect ratio protected</span>")
        self.imgbox_static1_lyt.addWidget(self.imgbox_static1)
        self.imgbox_static1_lyt.addWidget(self.imgbox_static1_lbl, alignment=Qt.AlignHCenter)

        self.imgbox_static2_lyt = QVBoxLayout()
        self.imgbox_static2_lyt.setAlignment(Qt.AlignHCenter)
        self.imgbox_hstatic_lyt.addLayout(self.imgbox_static2_lyt)

        self.imgbox_static2 = ImageBox("data/image.jpg", keepAspectRatio=False)
        self.imgbox_static2.scale(0.35)
        self.imgbox_static2_lbl = QLabel("<span style='font-size:14px; color:#888888'>Aspect ratio ignored</span>")
        self.imgbox_static2_lyt.addWidget(self.imgbox_static2)
        self.imgbox_static2_lyt.addWidget(self.imgbox_static2_lbl, alignment=Qt.AlignHCenter)

        self.imgbox_showcase_lyt.addWidget(QLabel("<span style='font-size:15px; color:#777777;'>You can also use animated GIFs.</span>"),
                                           alignment=Qt.AlignHCenter)

        self.imgbox_animated = ImageBox("data/luffy.gif")
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


        # finalize layout
        self.layout.addWidget(self.togglesw_showcase_wdt)
        self.layout.addWidget(self.stbtn_showcase_wdt)
        self.layout.addWidget(self.imgbox_showcase_wdt)
        self.layout.addWidget(self.colorpk_showcase_wdt)

        self.togglesw_showcase_wdt.show()
        self.stbtn_showcase_wdt.hide()
        self.imgbox_showcase_wdt.hide()
        self.colorpk_showcase_wdt.hide()



if __name__ == "__main__":
    app = QApplication(sys.argv)

    mw = MainWindow()
    mw.show()

    sys.exit(app.exec_())
