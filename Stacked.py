# -------------------------------------------------------------------------------
# Name:             Stacked.py
# Purpose:          Stacked Widget example
#
# Author:           Jeffreaux
#
# Created:          06July24
#
# Required Packages:    PyQt5, PyQt5-Tools
# -------------------------------------------------------------------------------

from PyQt5.QtWidgets import QMainWindow, QApplication, QPushButton, QAction, QStackedWidget
from PyQt5 import uic
import sys


class UI(QMainWindow):
    def __init__(self):
        super(UI, self).__init__()

        # Load the UI file
        uic.loadUi("Stacked_GUI.ui", self)

        # define Widgets
        self.btnExit = self.findChild(QPushButton, "btnExit")
        self.btnBlue = self.findChild(QPushButton, "btnBlue")
        self.btnRed = self.findChild(QPushButton, "btnRed")
        self.btnYellow = self.findChild(QPushButton, "btnYellow")
        self.actExit = self.findChild(QAction, "actExit")

        self.stackedWidget = self.findChild(QStackedWidget, "stackedWidget")

        # Define the actions
        self.btnExit.clicked.connect(self.closeEvent)
        self.btnBlue.clicked.connect(self.showBlue)
        self.btnRed.clicked.connect(self.showRed)
        self.btnYellow.clicked.connect(self.showYellow)

        self.actExit.triggered.connect(self.closeEvent)

        # Calling the Home page of the stackedWidget to front / Current at startup
        self.stackedWidget.setCurrentWidget(self.Home)


        # Show the app
        self.show()

    def showBlue(self):
        # Calling the Blue page of the stackedWidget to front / Current
        self.stackedWidget.setCurrentWidget(self.Blue)
    
    def showRed(self):
        # Calling the Red page of the stackedWidget to front / Current
        self.stackedWidget.setCurrentWidget(self.Red)

    def showYellow(self):
        # Calling the Yellow page of the stackedWidget to front / Current
        self.stackedWidget.setCurrentWidget(self.Yellow)
    
    
    
    def closeEvent(self, *args, **kwargs):
        # print("Program closed Successfully!")
        self.close()


# Initialize the App
app = QApplication(sys.argv)
UIWindow = UI()
app.exec_()
