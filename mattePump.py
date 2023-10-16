"All source code within this document is covered by"
"a CC BY-NC-SA 4.0 licence. Read more in /README.md"

import typing
from PyQt6 import QtCore
from PyQt6.QtWidgets import QWidget
from reportlab.pdfgen import canvas
from reportlab.lib.pagesizes import A4

from pdfGeneration import addInfoText, addQuestions

import sys
from PyQt6.QtCore import QSize, Qt
from PyQt6.QtWidgets import *

class mattePumpWindow(QMainWindow):
    def __init__(self):

        super().__init__()

        self.setWindowTitle("MattePump 1.0")

        self.title_input = QLineEdit()
        self.title_input.setText("MattePump")

        self.additionCheckbox = QCheckBox("Addition")
        self.subtractionCheckbox = QCheckBox("Subtraction")

        self.rangeFrom = QSpinBox()
        self.rangeFrom.setMinimum(2)
        self.rangeFrom.setValue(2)
        self.rangeTo = QSpinBox()
        self.rangeTo.setValue(10)

        self.button = QPushButton("Generate Sheet")
        self.button.clicked.connect(generateQuestionSheet)

        layout = QVBoxLayout()

        layout2 = QHBoxLayout()
        layout2.addWidget(self.rangeFrom)
        layout2.addWidget(QLabel(" to"))
        layout2.addWidget(self.rangeTo)

        
        layout.addWidget(self.title_input)
        layout.addWidget(self.additionCheckbox)
        layout.addWidget(self.subtractionCheckbox)
        layout.addLayout(layout2)
        layout.addWidget(self.button)

        container = QWidget()
        container.setLayout(layout)

        self.setCentralWidget(container)

    def changeTitle(self, s):
        self.title = s

    def getOperands(self):
        operands: [chr] = []
        if self.additionCheckbox.isChecked():
            operands += '+'
        if self.subtractionCheckbox.isChecked():
            operands += '-'
        return operands
    
    def getRange(self):
        return (self.rangeFrom.value(), self.rangeTo.value())
    
    def getTitle(self):
        return (self.title_input.text())

def generateQuestionSheet():
    worksheet = canvas.Canvas(window.getTitle() + ".pdf", pagesize=A4)
    addInfoText(worksheet, window.getTitle())
    addQuestions(worksheet, window.getOperands(), window.getRange())
    worksheet.save()

app = QApplication(sys.argv)

window = mattePumpWindow()
window.show()

app.exec()