from PyQt6.QtWidgets import (
    QApplication, QWidget, QLineEdit, QPushButton, QVBoxLayout
)
from PyQt6.QtCore import Qt
import sys


class Window(QWidget):
    def __init__(self):
        super().__init__()
        self.resize(300, 250)
        self.setWindowTitle('CodersLegacy')

        layout = QVBoxLayout()
        self.setLayout(layout)

        self.input = QLineEdit(self)
        self.input.setFixedWidth(150)
        layout.addWidget(self.input, alignment = Qt.AlignmentFlag.AlignHCenter)

        self.password = QLineEdit(self)
        self.password.setFixedWidth(150)
        self.password.setEchoMode(QLineEdit.EchoMode.Password)
        layout.addWidget(self.password,
                         alignment = Qt.AlignmentFlag.AlignHCenter)

        button = QPushButton('Get Password')
        button.clicked.connect(self.get2)
        layout.addWidget(button)

        button = QPushButton('Clear Password')
        button.clicked.connect(self.password.clear)
        layout.addWidget(button)

        button = QPushButton('Get Text')
        button.clicked.connect(self.get)
        layout.addWidget(button)

        button = QPushButton('Clear Text')
        button.clicked.connect(self.input.clear)
        layout.addWidget(button)

    def get(self):
        text = self.input.text()
        print('text = ', text)

    def get2(self):
        text = self.password.text()
        print('password = ', text)


app = QApplication(sys.argv)
window = Window()
window.show()
sys.exit(app.exec())
