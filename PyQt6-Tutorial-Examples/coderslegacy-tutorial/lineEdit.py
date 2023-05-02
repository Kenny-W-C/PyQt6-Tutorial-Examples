from PyQt6.QtWidgets import (
    QApplication, QWidget, QLineEdit
)
import sys


class Window(QWidget):
    def __init__(self):
        super().__init__()
        self.resize(300, 250)
        self.setWindowTitle('CodersLegacy')

        self.input = QLineEdit(self)
        self.input.move(80, 100)


app = QApplication(sys.argv)
window = Window()
window.show()
sys.exit(app.exec())
