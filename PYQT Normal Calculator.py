import sys
from PyQt5.QtCore import Qt
from PyQt5.QtWidgets import *
from PyQt5.QtGui import *

class Window(QWidget):
    def __init__(self):
        super().__init__()
        self.eqn = ""
        # Layout
        self.grid = QGridLayout()
        self.setLayout(self.grid)
        self.setGeometry(800, 150, 300, 300)
        # Widgets
        self.display = QLabel("0")
        self.grid.addWidget(self.display, 1, 1, 1, 2)

        self.button1 = QPushButton("9")
        self.grid.addWidget(self.button1, 2, 1, 1, 1)

        self.button2 = QPushButton("8")
        self.grid.addWidget(self.button2, 2, 2, 1, 1)

        self.button3 = QPushButton("7")
        self.grid.addWidget(self.button3, 2, 3, 1, 1)

        self.button4 = QPushButton("6")
        self.grid.addWidget(self.button4, 3, 1, 1, 1)

        self.button5 = QPushButton("5")
        self.grid.addWidget(self.button5, 3, 2, 1, 1)

        self.button6 = QPushButton("4")
        self.grid.addWidget(self.button6, 3, 3, 1, 1)

        self.button7 = QPushButton("3")
        self.grid.addWidget(self.button7, 4, 1, 1, 1)

        self.button8 = QPushButton("2")
        self.grid.addWidget(self.button8, 4, 2, 1, 1)

        self.button9 = QPushButton("1")
        self.grid.addWidget(self.button9, 4, 3, 1, 1)

        self.button10 = QPushButton("0")
        self.grid.addWidget(self.button10, 5, 1, 1, 1)

        self.button_add = QPushButton("+")
        self.grid.addWidget(self.button_add, 2, 4, 1, 1)

        self.button_equal = QPushButton("=")
        self.grid.addWidget(self.button_equal, 3, 4, 1, 1)

        self.button_clear = QPushButton("AC")
        self.grid.addWidget(self.button_clear, 5, 3, 1, 1)

        # Signals and Slots
        self.button1.clicked.connect(lambda: self.concat("9"))
        self.button2.clicked.connect(lambda: self.concat("8"))
        self.button3.clicked.connect(lambda: self.concat("7"))
        self.button4.clicked.connect(lambda: self.concat("6"))
        self.button5.clicked.connect(lambda: self.concat("5"))
        self.button6.clicked.connect(lambda: self.concat("4"))
        self.button7.clicked.connect(lambda: self.concat("3"))
        self.button8.clicked.connect(lambda: self.concat("2"))
        self.button9.clicked.connect(lambda: self.concat("1"))
        self.button10.clicked.connect(lambda: self.concat("0"))

        self.button_add.clicked.connect(lambda: self.concat("+"))
        self.button_equal.clicked.connect(self.equal)
        self.button_clear.clicked.connect(self.clear)

        # Style
        # Draw
        self.show()
    def concat(self, val):
        self.eqn += val
        self.display.setText(self.eqn)
    def equal(self):
        try:
            answer = eval(self.eqn)
            self.display.setText(str(answer))
        except:
            self.display.setText("ERROR")
            self.eqn = ""
    def clear(self):
        self.display.setText("")
        self.eqn = ""

if __name__ == "__main__":
    app = QApplication(sys.argv)
    gui = Window()
    sys.exit(app.exec())