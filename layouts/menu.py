from PyQt6.QtWidgets import QMainWindow, QMenuBar
from PyQt6.QtGui import QAction 

class MenuBar(QMainWindow):
    def __init__(self):
        super().__init__()

        menubar = QMenuBar(self)
        self.setMenuBar(menubar)

        operasi_menu = menubar.addMenu("Operasi")

        tambah_action = QAction("Tambah (+)", self)
        kurang_action = QAction("Kurang (-)", self)
        kali_action = QAction("Kali (*)", self)
        bagi_action = QAction("Bagi (/)", self)

        operasi_menu.addAction(tambah_action)
        operasi_menu.addAction(kurang_action)
        operasi_menu.addAction(kali_action)
        operasi_menu.addAction(bagi_action)

        tambah_action.triggered.connect(lambda: self.perform_operation("+"))
        kurang_action.triggered.connect(lambda: self.perform_operation("-"))
        kali_action.triggered.connect(lambda: self.perform_operation("*"))
        bagi_action.triggered.connect(lambda: self.perform_operation("/"))

    def perform_operation(self, operator):
        print(f"Operasi {operator} dipilih")