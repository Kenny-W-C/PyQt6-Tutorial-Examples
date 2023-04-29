from PyQt6.QtWidgets import (
    QApplication, QWidget, QLineEdit, QVBoxLayout
)
from PyQt6.QtCore import Qt
import sys


class Window(QWidget):
    def __init__(self):
        super().__init__()
        self.resize(250, 250)
        self.setWindowTitle("CodersLegacy")

        layout = QVBoxLayout()
        self.setLayout(layout)

        self.input = QLineEdit()
        self.input.setFixedWidth(150)
        self.input.textChanged.connect(self.check)
        layout.addWidget(self.input, alignment = Qt.AlignmentFlag.AlignCenter)

    def check(self):
        for x in self.input.text():
            if x < 'a' or x > 'z':
                print("Invalid Character entered")
                return


app = QApplication(sys.argv)
window = Window()
window.show()
sys.exit(app.exec())
