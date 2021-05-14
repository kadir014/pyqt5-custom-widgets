#                 PyQt5 Custom Widgets                #
#                GPL 3.0 - Kadir Aksoy                #
#   https://github.com/kadir014/pyqt5-custom-widgets  #


import time
import requests

from PyQt5.QtCore import QThread, pyqtSignal



class RequestHandler(QThread):

    requestResponsed = pyqtSignal(requests.Response)

    def __init__(self):
        super().__init__()

        self._request_pool = list()
        self._resume = True

    def __repr__():
        return f"<pyqt5Custom.RequestHandler()>"

    def pause(self):
        self._resume = False

    def resume(self):
        self._resume = True

    def newRequest(self, method, url, headers=None, data=None):
        self._request_pool.append((method, url, headers, data))

    def run(self):
        # time.sleeps prevents main window from glitching out, but IDK why
        while True:
            while not self._resume: time.sleep(0.15)

            if len(self._request_pool) > 0:
                for req in self._request_pool:
                    resp = requests.request(req[0], req[1], headers=req[2], data=req[3])
                    self.requestResponsed.emit(resp)

                self._request_pool.clear()

            time.sleep(0.15)
