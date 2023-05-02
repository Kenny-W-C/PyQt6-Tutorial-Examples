from PyQt6.QtWidgets import QApplication, QWidget, QLabel
import sys


class Window(QWidget):
    def __init__(self):
        super().__init__()
        self.resize(300, 250)
        self.setWindowTitle('CodersLegacy')

        # the 2nd parameter refers to the parent widget in which we want to
        # place the label
        label = QLabel('GUI Applications with PyQt6', self)
        # move the label from x=0, y=0 to x=80, y=100
        label.move(80, 100)
        

app = QApplication(sys.argv)
window = Window()
window.show()
sys.exit(app.exec())
