
from PyQt5 import QtWidgets, uic

class BuildWindow:
    def __init__(self):
       self.window = uic.loadUi("mainwindow.ui")

    def showWindow(self):
        self.window.show()
