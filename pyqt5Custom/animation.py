#                 PyQt5 Custom Widgets                #
#                GPL 3.0 - Kadir Aksoy                #
#   https://github.com/kadir014/pyqt5-custom-widgets  #


import time
from math import ceil, sin, pi, sqrt, pow

from PyQt5.QtGui import QColor



class Animation:
    easeOutSine  = lambda x: sin((x * pi) / 2)
    easeOutCubic = lambda x: 1 - ((1 - x)**3)
    easeOutQuart = lambda x: 1 - pow(1 - x, 4)
    easeOutCirc  = lambda x: 1 - ((1 - x)**3)#sqrt(1 - pow(x - 1, 2))



class AnimationHandler:
    def __init__(self, widget, startv, endv, type):
        self.widget = widget
        self.type = type

        self.startv = startv
        self.endv = endv

        self.value = 0

        self.speed = 3.45

        self.sensitivity = 0.001

        self.reverse = False
        self.loop = False
        self.started = None

        self._tickfunc = None

    def __repr__(self):
        return f"<pyqt5Custom.AnimationHandler({self.startv}->{self.endv})>"

    def tick(self, func):
        self._tickfunc = func
        return func

    def start(self, reverse=False, loop=False):
        self.reverse = reverse
        self.loop = loop
        self.started = True
        self.orgstart_time = time.time()
        self.value = 0
        self.widget.update()

    def reset(self):
        self.value = 0
        self.started = None

    def done(self):
        return self.started is None

    def update(self):
        if not self.done():
            ep = time.time() - self.orgstart_time

            self.value = self.type(ep * self.speed)

            if self.reverse:
                if self.current() <= self.startv + self.sensitivity: self.started = None
            else:
                if self.current() >= self.endv - self.sensitivity: self.started = None

            if self.done():
                if self.loop:
                    self.start(reverse=not self.reverse, loop=True)
                return

            #print(self.value)
            if self._tickfunc: self._tickfunc()

    def current(self):
        if self.reverse:
            return self.endv - (self.value * (self.endv-self.startv))
        else:
            return self.value * (self.endv-self.startv)

    def lerp(self, a, b):
        f = self.current() / self.endv

        if isinstance(a, QColor):
            r1, r2 = a.red(),   b.red()
            g1, g2 = a.green(), b.green()
            b1, b2 = a.blue(),  b.blue()
            a1, a2 = a.alpha(), b.alpha()

            r  = (r2 - r1) * f + r1
            g  = (g2 - g1) * f + g1
            _b = (b2 - b1) * f + b1
            _a = (a2 - a1) * f + a1

            return QColor(r, g, _b, _a)

        else:
            return (b - a) * f + a
