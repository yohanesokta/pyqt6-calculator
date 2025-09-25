from PyQt6.QtGui import QFont
from PyQt6.QtWidgets import  QPushButton, QTextEdit
import re

#  ** How to use **
#  Ini biar ada tutorial bang jangan di sangka AI hehe ..
#  Controller nanti di buat dari class MathExecs
#  Bisa gunakan ButtonOperation Langsung dengan controllernya saling terhubung
#  Nanti kalau mau lihat hasil text print saja controller dari MathExecs
#  BROOWW MathExecs aku butuh textEdit di parameter nya agar bisa change value


class ButtonOperation(QPushButton):
    def __init__(self,text,callback,fixSize=0,fontSize=0):
        super().__init__()
        self.setText(str(text))
        if (fixSize > 0):
            self.setFixedSize(fixSize,fixSize)
        if (fontSize > 0):
            font = QFont()
            font.setPointSize(fontSize)
            self.setFont(font)
        self.clicked.connect(lambda : callback(str(text)))

#  ** How to use **
#  fungsi controler dari class MathExecs gunakan untuk push number dan eksekusi operator
#  psuh number dan push opertor di sini langsung mengeksekusi sesuai operasi matematika

class MathExecs:
    def __init__(self):
        self.listNumber:str = ""
        self.operator = None
        self.text_edits: list[QTextEdit] = [] # ini buat nampung text edit
        
    def add_text_edit(self, widget: QTextEdit):
        self.text_edits.append(widget)

    def change_text_edit(self):
        for widget in self.text_edits:
            widget.setText(self.listNumber)
    def push_number(self, other):
        self.listNumber += other
        self.change_text_edit()
    def push_operator(self,operator):
        lastInput = self.listNumber[-1] if len(self.listNumber) > 0 else ""
        self.calculate(lastInput)
        
        if operator == "=":
            self.change_text_edit()
            return

        if lastInput in "+/*" and operator == "-":
            self.listNumber += operator
        elif lastInput not in "-+/*":
            self.listNumber += operator
            self.operator = operator
        self.change_text_edit()
        
    def calculate(self,lastInput):
        if (self.operator != None and lastInput not in "-+/*"):
            operasi = re.sub(r'\b0+(\d+)', r'\1',self.listNumber)
            self.listNumber = str(eval(operasi))
            self.operator = None
    def clearState(self,_):
        self.listNumber = ""
        self.operator = None
        self.change_text_edit()

    def __str__(self):
       return self.listNumber
