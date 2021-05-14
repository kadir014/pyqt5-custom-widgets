#                 PyQt5 Custom Widgets                #
#                GPL 3.0 - Kadir Aksoy                #
#   https://github.com/kadir014/pyqt5-custom-widgets  #


from PyQt5.QtCore    import Qt, QPointF
from PyQt5.QtWidgets import QWidget, QHBoxLayout, QLabel, QAbstractButton, QGraphicsDropShadowEffect, QGraphicsOpacityEffect
from PyQt5.QtGui     import QColor, QPainter, QPen, QBrush, QFont

from .animation import Animation, AnimationHandler
from .imagebox import ImageBox



class StyledButton(QAbstractButton):
    def __init__(self, text="", icon=None):
        super().__init__()

        self.setMinimumSize(100, 45)

        self.layout = QHBoxLayout()
        self.layout.setContentsMargins(0, 0, 0, 0)
        self.setLayout(self.layout)

        self.conwdt = QWidget()
        self.conlyt = QHBoxLayout()
        self.conlyt.setContentsMargins(0, 0, 0, 0)
        self.conwdt.setLayout(self.conlyt)
        self.layout.addWidget(self.conwdt, alignment=Qt.AlignCenter)

        self._text = text
        self.textLbl = QLabel(text)
        self.conlyt.addWidget(self.textLbl, alignment=Qt.AlignCenter)

        self._icon = None
        if icon is not None:
            self.setIcon(icon)

        # REMOVE
        self.opacity = QGraphicsOpacityEffect()
        self.opacity.setOpacity(1.0)
        #self.setGraphicsEffect(self.opacity)

        self.shadow = QGraphicsDropShadowEffect()
        self.shadow.setBlurRadius(0.8)
        self.shadow.setColor(QColor(0, 0, 0, 100))
        self.shadow.setOffset(0, 2)
        self.setGraphicsEffect(self.shadow)

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

        self.anim_hover = AnimationHandler(self, 0, 1, Animation.easeOutCirc)
        self.anim_press = AnimationHandler(self, 0, 1, Animation.easeOutCubic)

        self._press_reset = False
        self.mouse_x, self.mouse_y = 0, 0
        self._mouse_pressed = False
        self._hover = False
        self._was_checked = False

    def __repr__(self):
        return f"<pyqt5Custom.StyledButton()>"

    def setText(self, text):
        self._text = text
        self.textLbl.setText(self._text)

    def text(self):
        return self._text

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

    def copyStyleDict(self, widget):
        for state in widget.styleDict:
            self.setStyleDict(widget.styleDict[state], state)

    def setIcon(self, icon):
        if self._icon is not None:
            self._icon.deleteLater()

        if isinstance(icon, str):
            self._icon = ImageBox(icon)
            self._icon.setFixedSize(18, 18)
            if self._text:
                self.textLbl.show()
                self.conlyt.insertWidget(0, self._icon, alignment=Qt.AlignVCenter|Qt.AlignRight)
                self.conlyt.removeItem(self.conlyt.itemAt(1))
                self.conlyt.addWidget(self.textLbl, alignment=Qt.AlignVCenter|Qt.AlignLeft)
            else:
                self.textLbl.hide()
                self.conlyt.insertWidget(0, self._icon, alignment=Qt.AlignCenter)

        else:
            self._icon = icon
            self._icon.setFixedSize(18, 18)
            if self._text:
                self.textLbl.show()
                self.conlyt.insertWidget(0, self._icon, alignment=Qt.AlignVCenter|Qt.AlignRight)
                self.conlyt.removeItem(self.conlyt.itemAt(1))
                self.conlyt.addWidget(self.textLbl, alignment=Qt.AlignVCenter|Qt.AlignLeft)

            else:
                self.textLbl.hide()
                self.conlyt.insertWidget(0, self._icon, alignment=Qt.AlignCenter)

    def setIconSize(self, width, height):
        self._icon.setFixedSize(width, height)

    def update(self):
        self.anim_hover.update()
        self.anim_press.update()

        super().update()

    def enterEvent(self, event):
        self.anim_hover.start()
        self._hover = True

        if not self.isChecked():
            self._was_checked = False

    def leaveEvent(self, event):
        self.anim_hover.start(reverse=True)
        self._hover = False

        if not self.isChecked():
            self._was_checked = False

    def mousePressEvent(self, event):
        self.mouse_x, self.mouse_y = event.x(), event.y()
        self._mouse_pressed = True
        self.anim_press.start()

        if self.isChecked(): self._was_checked = True

        super().mousePressEvent(event)

    def mouseReleaseEvent(self, event):
        self._mouse_pressed = False
        self.anim_press.start(reverse=True)

        super().mouseReleaseEvent(event)

    def paintEvent(self, event):
        pt = QPainter()
        pt.begin(self)
        pt.setRenderHint(QPainter.Antialiasing, on=self.styleDict["default"]["render-aa"])

        dsr1 = self.styleDict["default"]["drop-shadow-radius"]
        dsr2 = self.styleDict["hover"]["drop-shadow-radius"]
        dsr3 = self.styleDict["press"]["drop-shadow-radius"]
        dso1 = self.styleDict["default"]["drop-shadow-offset"]
        dso2 = self.styleDict["hover"]["drop-shadow-offset"]
        dso3 = self.styleDict["press"]["drop-shadow-offset"]
        dsc1 = self.styleDict["default"]["drop-shadow-alpha"]
        dsc2 = self.styleDict["hover"]["drop-shadow-alpha"]
        dsc3 = self.styleDict["press"]["drop-shadow-alpha"]

        if self.anim_press.current() > 0.001:
            dsr = dsr3
            dso = dso3
            dsc = dsc3
        elif self._hover:
            dsr = dsr2
            dso = dso2
            dsc = dsc2
        else:
            dsr = dsr1
            dso = dso1
            dsc = dsc1

        if dsr == 0:
            self.shadow.setEnabled(False)
        else:
            self.shadow.setEnabled(True)
            self.shadow.setBlurRadius(dsr)
            self.shadow.setOffset(*dso)
            self.shadow.setColor(QColor(0, 0, 0, dsc))

        if self.isChecked():
            fc1 = QColor(*self.styleDict["press"]["color"])
            fc2 = QColor(*self.styleDict["check-hover"]["color"])
            fc = self.anim_hover.lerp(fc1, fc2)
        else:
            fc1 = QColor(*self.styleDict["default"]["color"])
            fc2 = QColor(*self.styleDict["hover"]["color"])
            fc3 = QColor(*self.styleDict["press"]["color"])
            if   self.anim_press.current() > 0.001 and self._hover: fc = self.anim_press.lerp(fc2, fc3)
            elif self.anim_press.current() > 0.001:                 fc = self.anim_press.lerp(fc1, fc3)
            else:                                                   fc = self.anim_hover.lerp(fc1, fc2)

        plt = self.textLbl.palette()
        plt.setColor(self.textLbl.foregroundRole(), fc)
        self.textLbl.setPalette(plt)

        fs1 = self.styleDict["default"]["font-size"]
        fs2 = self.styleDict["hover"]["font-size"]
        fs3 = self.styleDict["press"]["font-size"]
        if   self.anim_press.current() > 0.001 and self._hover: fs = self.anim_press.lerp(fs2, fs3)
        elif self.anim_press.current() > 0.001:                 fs = self.anim_press.lerp(fs1, fs3)
        else:                                                   fs = self.anim_hover.lerp(fs1, fs2)

        fnt = self.textLbl.font()
        fnt.setPixelSize(fs)
        if not self.styleDict["default"]["font-subpixel-aa"]: fnt.setStyleStrategy(QFont.NoSubpixelAntialias)
        if self.styleDict["default"]["font-family"]: fnt.setFamily(self.styleDict["default"]["font-family"])
        self.textLbl.setFont(fnt)

        pc1 = QColor(*self.styleDict["default"]["border-color"])
        pc2 = QColor(*self.styleDict["hover"]["border-color"])
        pc3 = QColor(*self.styleDict["press"]["border-color"])
        if   self.anim_press.current() > 0.001 and self._hover: pc = self.anim_press.lerp(pc2, pc3)
        elif self.anim_press.current() > 0.001:                 pc = self.anim_press.lerp(pc1, pc3)
        else:                                                   pc = self.anim_hover.lerp(pc1, pc2)

        pw1 = self.styleDict["default"]["border-width"]
        pw2 = self.styleDict["hover"]["border-width"]
        pw3 = self.styleDict["press"]["border-width"]
        if   self.anim_press.current() > 0.001 and self._hover: pw = self.anim_press.lerp(pw2, pw3)
        elif self.anim_press.current() > 0.001:                 pw = self.anim_press.lerp(pw1, pw3)
        else:                                                   pw = self.anim_hover.lerp(pw1, pw2)

        pen = QPen(pc, pw)

        if self.isChecked():
            b1 = QColor(*self.styleDict["press"]["background-color"])
            b2 = QColor(*self.styleDict["check-hover"]["background-color"])
            b = self.anim_hover.lerp(b1, b2)
        else:
            b1 = QColor(*self.styleDict["default"]["background-color"])
            b2 = QColor(*self.styleDict["hover"]["background-color"])
            b3 = QColor(*self.styleDict["press"]["background-color"])
            b4 = QColor(*self.styleDict["check-hover"]["background-color"])
            if self._was_checked:                                   b = self.anim_press.lerp(b2, b4)
            elif self.anim_press.current() > 0.001 and self._hover: b = self.anim_press.lerp(b2, b3)
            elif self.anim_press.current() > 0.001:                 b = self.anim_press.lerp(b1, b3)
            else:                                                   b = self.anim_hover.lerp(b1, b2)

        brush = QBrush(b)

        pt.setPen(pen)
        pt.setBrush(brush)

        r1 = self.styleDict["default"]["border-radius"]
        r2 = self.styleDict["hover"]["border-radius"]
        r3 = self.styleDict["press"]["border-radius"]
        if   self.anim_press.current() > 0.001 and self._hover: r = self.anim_press.lerp(r2, r3)
        elif self.anim_press.current() > 0.001:                 r = self.anim_press.lerp(r1, r3)
        else:                                                   r = self.anim_hover.lerp(r1, r2)

        if r > self.height()/2: r = self.height()/2


        crn = self.styleDict["default"]["radius-corners"]

        if all(crn) and self.styleDict["default"]["render-fast"]:
            pt.drawRoundedRect(1, 1, self.width()-2, self.height()-2, r, r)

        else:
            pt.setPen(QPen(QColor(0, 0, 0, 0)))
            pt.setBrush(QBrush(pc))

            pt.drawRect(0, r, self.width(), self.height()-r*2)
            pt.drawRect(r, 0, self.width()-r*2, self.height())

            if crn[0]: pt.drawEllipse(QPointF(r, r), r, r)
            else: pt.drawRect(0, 0, r, r)
            if crn[3]: pt.drawEllipse(QPointF(self.width()-r, self.height()-r), r, r)
            else: pt.drawRect(self.width()-r, self.height()-r, r, r)
            if crn[2]: pt.drawEllipse(QPointF(r, self.height()-r), r, r)
            else: pt.drawRect(0, self.height()-r, r, r)
            if crn[1]: pt.drawEllipse(QPointF(self.width()-r, r), r, r)
            else: pt.drawRect(self.width()-r, 0, r, r)

            pt.setBrush(QBrush(b))

            pt.drawRect(pw, r+pw, self.width()-pw*2, self.height()-r*2-pw*2)
            pt.drawRect(r+pw, pw, self.width()-r*2-pw*2, self.height()-pw*2)
            if crn[0]: pt.drawEllipse(QPointF(r, r), r-pw, r-pw)
            else: pt.drawRect(pw, pw, r+1, r+1)
            if crn[3]: pt.drawEllipse(QPointF(self.width()-r, self.height()-r), r-pw, r-pw)
            else: pt.drawRect(self.width()-r-pw, self.height()-r-pw, r, r)
            if crn[2]: pt.drawEllipse(QPointF(r, self.height()-r), r-pw, r-pw)
            else: pt.drawRect(pw, self.height()-r-pw, r, r)
            if crn[1]: pt.drawEllipse(QPointF(self.width()-r, r), r-pw, r-pw)
            else: pt.drawRect(self.width()-r-pw, pw, r, r)

        pt.end()

        if not self.anim_hover.done(): self.update()
        if not self.anim_press.done(): self.update()
