# kombinasi_layout.py -> untuk mengatur layout kombinasi qh dan qv
import sys

from PyQt6.QtGui import QFont
from PyQt6.QtWidgets import QWidget, QApplication, QMainWindow, QTextEdit, QVBoxLayout, QHBoxLayout

from utils.function_button import MathExecs, ButtonOperation

font_size = 16
fixed_size = 60

class KombinasiLayout(QWidget):
    def __init__(self):
        super().__init__()

        input_text = QTextEdit()
        controllers = MathExecs(input_text)
        input_text.setFontPointSize(font_size)

        # Layout utama vertikal
        main_layout = QVBoxLayout()
        main_layout.addWidget(input_text)

        # Baris 1 (horizontal)
        row1 = QHBoxLayout()
        row1.addWidget(ButtonOperation(9, controllers.push_number, fixed_size, font_size))
        row1.addWidget(ButtonOperation("AC", controllers.clearState, fixed_size, font_size))
        row1.addWidget(ButtonOperation("*", controllers.push_operator, fixed_size, font_size))

        # Baris 2 (horizontal)
        row2 = QHBoxLayout()
        row2.addWidget(ButtonOperation(5, controllers.push_number, fixed_size, font_size))
        row2.addWidget(ButtonOperation(6, controllers.push_number, fixed_size, font_size))
        row2.addWidget(ButtonOperation("/", controllers.push_operator, fixed_size, font_size))

        # Baris 3 (horizontal)
        row3 = QHBoxLayout()
        row3.addWidget(ButtonOperation(1, controllers.push_number, fixed_size, font_size))
        row3.addWidget(ButtonOperation(3, controllers.push_number, fixed_size, font_size))
        row3.addWidget(ButtonOperation("-", controllers.push_operator, fixed_size, font_size))

        # Baris 4 (horizontal)
        row4 = QHBoxLayout()
        row4.addWidget(ButtonOperation(0, controllers.push_number, fixed_size, font_size))
        row4.addWidget(ButtonOperation("=", controllers.push_operator, fixed_size, font_size))
        row4.addWidget(ButtonOperation("+", controllers.push_operator, fixed_size, font_size))

        # Tambahkan semua baris ke layout utama
        main_layout.addLayout(row1)
        main_layout.addLayout(row2)
        main_layout.addLayout(row3)
        main_layout.addLayout(row4)

        main_layout.setSpacing(5)

        self.setLayout(main_layout)