# main.py -> file utama untuk menjalankan aplikasi
import sys
from PyQt6.QtWidgets import (
    QApplication,
    QMainWindow,
    QTabWidget,
)

from layouts.grid_layout import GridCalculator # -> memanggil file grid layout
from layouts.kombinasi_layout import KombinasiLayout # -> memanggil file kombinasi layout
from layouts.menu import MenuBar

from utils.function_button import MathExecs

class MainWindow(QMainWindow):
    def __init__(self):
        super().__init__()

        self.setWindowTitle("Aplikasi Kalkulator")

        controller = MathExecs()

        # Membuat tab widget
        tabs = QTabWidget()
        tabs.setTabPosition(QTabWidget.TabPosition.North) # -> di taruh di tengah
        tabs.setMovable(True)

        # Tab Grid - untuk menampilkan layout bentuk gridnya
        grid_widget = GridCalculator(controller)
        tabs.addTab(grid_widget, "Grid Layout")

        # Tab Kombinasi - untuk menampilkan layout kombinasinya yang meliputi qh qv
        kombinasi_widget = KombinasiLayout(controller)
        tabs.addTab(kombinasi_widget, "Kombinasi Layout")

        # Menu
        menu = MenuBar()
        self.setMenuBar(menu.menuBar())
        menu.perform_operation = controller.push_operator
        self.setCentralWidget(tabs)

app = QApplication(sys.argv)
window = MainWindow()
window.show()
app.exec()