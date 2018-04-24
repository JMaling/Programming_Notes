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
        button1 = QPushButton("Press for a Suprise", self)
        grid.addWidget(button1, 1, 2, 1, 1)
        lcd = QLCDNumber(self)
        grid.addWidget(lcd, 2, 1, 1, 2)
        slider = QSlider(Qt.Horizontal, self)
        grid.addWidget(slider, 3, 1, 1, 2)
        slider.setValue(99)
        # Set the signals and the slots
        button1.clicked.connect(lambda: label1.setText("CLICK"))
        # slider.valueChanged.connect(lambda: lcd.setWindowIconText(slider.value()))
        # Draw the Application
        self.show()

if __name__ == "__main__":
    app = QApplication(sys.argv)
    gui = Window() # create an instance of the Window class
    sys.exit(app.exec_())