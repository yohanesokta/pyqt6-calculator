# grid_layout.py -> untuk membuat layout grid kalkulator
import sys

from PyQt6.QtGui import QFont
from PyQt6.QtWidgets import QWidget, QApplication, QMainWindow, QTextEdit, QVBoxLayout, QHBoxLayout, QGridLayout, \
    QLayoutItem

from utils.function_button import MathExecs, ButtonOperation

font_size = 16
fixed_size = 60

class GridCalculator(QWidget):
    def __init__(self):
        super().__init__()

        input_text = QTextEdit()
        controllers = MathExecs(input_text)
        input_text.setFontPointSize(font_size)

        grid = QGridLayout()
        grid.addWidget(input_text, 0, 0, 1, 3)

        grid.addWidget(ButtonOperation(9, controllers.push_number, fixed_size, font_size), 1, 0)
        grid.addWidget(ButtonOperation("AC", controllers.clearState, fixed_size, font_size), 1, 1)
        grid.addWidget(ButtonOperation("*", controllers.push_operator, fixed_size, font_size), 1, 2)

        grid.addWidget(ButtonOperation(5, controllers.push_number, fixed_size, font_size), 2, 0)
        grid.addWidget(ButtonOperation(6, controllers.push_number, fixed_size, font_size), 2, 1)
        grid.addWidget(ButtonOperation("/", controllers.push_operator, fixed_size, font_size), 2, 2)

        grid.addWidget(ButtonOperation(1, controllers.push_number, fixed_size, font_size), 3, 0)
        grid.addWidget(ButtonOperation(3, controllers.push_number, fixed_size, font_size), 3, 1)
        grid.addWidget(ButtonOperation("-", controllers.push_operator, fixed_size, font_size), 3, 2)

        grid.addWidget(ButtonOperation(0, controllers.push_number, fixed_size, font_size), 4, 0)
        grid.addWidget(ButtonOperation("=", controllers.push_operator, fixed_size, font_size), 4, 1)
        grid.addWidget(ButtonOperation("+", controllers.push_operator, fixed_size, font_size), 4, 2)

        grid.setVerticalSpacing(5)
        grid.setHorizontalSpacing(5)

        self.setLayout(grid)