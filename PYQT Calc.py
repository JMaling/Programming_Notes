import sys
from PyQt5.QtCore import Qt
from PyQt5.QtWidgets import *
from PyQt5.QtGui import *

class Window(QWidget):
    def __init__(self):
        super().__init__()
        # Layout
        self.grid = QGridLayout()
        self.setLayout(self.grid)
        self.setGeometry(800, 150, 300, 300)

        # Widgets
        self.title = QLabel("Hypotenuse Calculator")
        self.grid.addWidget(self.title, 1, 1, 1, 1)
        self.title.setObjectName("title")
        self.labelA = QLabel("Length of Side A:")
        self.grid.addWidget(self.labelA, 2, 1, 1, 1)
        self.labelB = QLabel("Length of Side B:")
        self.grid.addWidget(self.labelB, 3, 1, 1, 1)
        self.sideA = QLineEdit()
        self.grid.addWidget(self.sideA, 2, 2, 1, 1)
        self.sideB = QLineEdit()
        self.grid.addWidget(self.sideB, 3, 2, 1, 1)
        self.calc = QPushButton("Calculate Force of Gravity (N)")
        self.grid.addWidget(self.calc, 4, 1, 1, 1)
        self.answer = QLabel("0")
        self.grid.addWidget(self.answer, 4, 2, 1, 1)

        # Signals/Slots
        self.calc.clicked.connect(self.find_hyp)
        self.show()
        self.style_sheet()

        # Set Style
    def style_sheet(self):
        style_sheet = "PYQT Calc.css"
        with open(style_sheet) as f:
            self.setStyleSheet(f.read())

        # Draw
    def find_hyp(self):
        a = float(self.sideA.text())
        b = float(self.sideB.text())
        c = round(((a ** 2) + (b ** 2)) ** (1 / 2), 3)
        self.answer.setText(str(c))

if __name__ == "__main__":
    app = QApplication(sys.argv)
    gui = Window()
    sys.exit(app.exec())

