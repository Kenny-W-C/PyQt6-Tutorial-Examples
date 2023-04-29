from PyQt6.QtGui import *
from PyQt6.QtWidgets import *
from PyQt6.QtCore import *
from PyQt6 import QtCore
import sys


class MainWindow(QMainWindow):
    def __init__(self, *args, **kwargs):
        super(MainWindow, self).__init__(*args, **kwargs)

        self.setWindowTitle('My Awesome App')
        label = QLabel('THIS IS AWE#SOME!!!!')
        # !!!!!!IMPORTANT!!!!!!!!! AlignCenter in PyQt6 requires to import
        # PyQt6.QtCore and the proper call of 'Qt.AlignmentFlag.AlignCenter'
        # for alignment flags to be called!!!!!!IMPORTANT!!!!!!!!!
        label.setAlignment(Qt.AlignmentFlag.AlignCenter)
        self.setCentralWidget(label)


app = QApplication(sys.argv)
window = MainWindow()
window.show()
app.exec()
