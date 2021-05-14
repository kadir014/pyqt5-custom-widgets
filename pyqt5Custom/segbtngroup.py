#                 PyQt5 Custom Widgets                #
#                GPL 3.0 - Kadir Aksoy                #
#   https://github.com/kadir014/pyqt5-custom-widgets  #


from PyQt5.QtCore    import Qt, pyqtSignal
from PyQt5.QtWidgets import QWidget, QHBoxLayout

from .styledbutton import StyledButton



class SegmentedButtonGroup(QWidget):

    clicked = pyqtSignal(int)

    def __init__(self, radio=False):
        super().__init__()

        self.styleDict = {
            "default" : {
                "background-image" : None,
                "background-color" : (255, 255, 255),

                "border-color"  : (0, 0, 0),
                "border-width"  : 1,
                "border-radius" : 11,
                "radius-corners" : (True, True, True, True),

                "font-family" : None,
                "font-size"   : 12,
                "font-weight" : "regular",
                "color"       : (0, 0, 0),

                "drop-shadow-radius" : 0,
                "drop-shadow-offset" : (0, 0),
                "drop-shadow-alpha"  : 120,

                "click-effect-radius" : 500,
                "click-effect-color"  : (0, 0, 0, 90),

                "render-fast"      : False,
                "render-aa"        : True,
                "font-subpixel-aa" : False
            },

            "hover" : {
                "background-image" : None,
                "background-color" : (245, 245, 245),

                "border-color"  : (0, 0, 0),
                "border-width"  : 1,
                "border-radius" : 11,

                "font-size"   : 12,
                "font-weight" : "regular",
                "color"       : (0, 0, 0),

                "drop-shadow-radius" : 0,
                "drop-shadow-offset" : (0, 0),
                "drop-shadow-alpha"  : 120
            },

            "press" : {
                "background-image" : None,
                "background-color" : (228, 228, 228),

                "border-color"  : (0, 0, 0),
                "border-width"  : 1,
                "border-radius" : 11,

                "font-size"   : 12,
                "font-weight" : "regular",
                "color"       : (0, 0, 0),

                "drop-shadow-radius" : 0,
                "drop-shadow-offset" : (0, 0),
                "drop-shadow-alpha"  : 120
            },

            "check-hover" : {
                "background-image" : None,
                "background-color" : (245, 245, 245),

                "border-color"  : (0, 0, 0),
                "border-width"  : 1,
                "border-radius" : 11,

                "font-size"   : 12,
                "font-weight" : "regular",
                "color"       : (0, 0, 0),

                "drop-shadow-radius" : 0,
                "drop-shadow-offset" : (0, 0),
                "drop-shadow-alpha"  : 120
            },
        }

        self.radio = radio

        self._buttons = list()

        self.layout = QHBoxLayout()
        self.setLayout(self.layout)
        self.layout.setContentsMargins(2, 0, 2, 0)
        self.layout.setSpacing(0)

    def __repr__(self):
        return f"<pyqt5Custom.SegmentdButtonGroup({len(self._buttons)} buttons)>"

    def setStyleDict(self, styledict, state=None):
        if state is None:
            for k in styledict:
                self.styleDict["default"][k] = styledict[k]
                self.styleDict["hover"][k] = styledict[k]
                self.styleDict["press"][k] = styledict[k]
                self.styleDict["check-hover"][k] = styledict[k]
        else:
            for k in styledict:
                self.styleDict[state][k] = styledict[k]

    def addButton(self, text="", icon=None, tag=None):
        btn = StyledButton(text=text, icon=None)
        btn.setStyleDict(self.styleDict["default"])
        btn.setStyleDict(self.styleDict["hover"], "hover")
        btn.setStyleDict(self.styleDict["press"], "press")
        btn.setStyleDict(self.styleDict["check-hover"], "check-hover")
        if self.radio:
            btn.setCheckable(True)

        if tag is None: tag = id(btn)
        self._buttons.append((tag, btn))
        self.layout.addWidget(btn)

        if len(self._buttons) == 1:
            btn.setStyleDict({"radius-corners":(True, False, True, False)})

        else:
            if len(self._buttons) >= 3:
                btnPrev = self._buttons[-2][1]
                btnPrev.setStyleDict({"radius-corners":(False, False, False, False)})
            btn.setStyleDict({"radius-corners":(False, True, False, True)})

        for btnn in self._buttons:
            btnn[1].setFixedSize(self.width()/len(self._buttons), self.height())

        @btn.clicked.connect
        def slot():
            self._clicked(tag)
            self.clicked.emit(tag)

        l = len(self._buttons)
        self.layout.setContentsMargins(l*2, 0, l*2, 0)
        return btn

    def getByTag(self, tag):
        for btn in self._buttons:
            if btn[0] == tag: return btn[1]

    def _clicked(self, tag):
        for btn in self._buttons:
            if btn[0] != tag:
                if btn[1].isChecked():
                    btn[1].anim_press.start(reverse=True)
                    btn[1]._was_checked = False
                    btn[1].setChecked(False)
