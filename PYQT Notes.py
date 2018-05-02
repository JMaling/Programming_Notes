import sys
from PyQt5.QtCore import Qt
from PyQt5.QtWidgets import *

class Window(QWidget): # window class is a child of the widget class
    def __init__(self):
        super().__init__()
        # Set a layout
        grid = QGridLayout()
        self.setLayout(grid)
        self.setGeometry(10, 10, 300, 300) # topleftx, toprighty, width, height

        # Make the widgets
        label1 = QLabel("Label #1", self) # text to display, and the widget it is assigned to
        grid.addWidget(label1, 1, 1, 1, 1) # row, column, rowspan, columnspan

        button1 = QPushButton("Press for a Surprise", self)
        grid.addWidget(button1, 1, 2, 1, 1)

        combobox = QComboBox(self)
        grid.addWidget(combobox, 4, 1, 1, 1)
        combobox.addItems(["Beck", "Can", "Go", "Kick Sticks"])

        checkbox = QCheckBox(self) # boolean
        grid.addWidget(checkbox, 4, 2, 1, 1)

        textline = QLineEdit(self) # getting a string
        grid.addWidget(textline, 5, 1, 1, 1)

        multiline = QTextEdit(self)
        grid.addWidget(multiline, 5, 2, 1, 1)

        calendar = QCalendarWidget(self)
        grid.addWidget(calendar, 6, 1, 1, 1)

        lcd = QLCDNumber(self)
        grid.addWidget(lcd, 2, 1, 1, 2)

        slider = QSlider(Qt.Horizontal, self)
        grid.addWidget(slider, 3, 1, 1, 2)
        slider.setValue(99)
        lcd.display(99)

        # Set the signals and the slots
        button1.clicked.connect(lambda: label1.setText("CLICK"))
        slider.valueChanged.connect(lcd.display)
        checkbox.stateChanged.connect(lambda: print("Box Checked"))
        multiline.textChanged.connect(lambda: print(multiline))
    def box_checked(self):
        print("Box Checked")
        # Draw the Application
        self.show()

if __name__ == "__main__":
    app = QApplication(sys.argv)
    gui = Window() # create an instance of the Window class
    sys.exit(app.exec_())