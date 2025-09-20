# main.py -> file utama untuk menjalankan aplikasi
import sys
from PyQt6.QtWidgets import (
    QApplication,
    QMainWindow,
    QTabWidget,
)

from layouts.grid_layout import GridCalculator # -> memanggil file grid layout
from layouts.kombinasi_layout import KombinasiLayout # -> memanggil file kombinasi layout

class MainWindow(QMainWindow):
    def __init__(self):
        super().__init__()

        self.setWindowTitle("Aplikasi Kalkulator")

        # Membuat tab widget
        tabs = QTabWidget()
        tabs.setTabPosition(QTabWidget.TabPosition.North) # -> di taruh di tengah
        tabs.setMovable(True)

        # Tab Grid - untuk menampilkan layout bentuk gridnya
        grid_widget = GridCalculator()
        tabs.addTab(grid_widget, "Grid Layout")

        # Tab Kombinasi - untuk menampilkan layout kombinasinya yang meliputi qh qv
        kombinasi_widget = KombinasiLayout()
        tabs.addTab(kombinasi_widget, "Kombinasi Layout")

        self.setCentralWidget(tabs)

app = QApplication(sys.argv)
window = MainWindow()
window.show()
app.exec()