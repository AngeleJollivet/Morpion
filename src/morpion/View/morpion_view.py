from PyQt5.QtWidgets import (
    QWidget, QLabel, QVBoxLayout
)
from PyQt5.QtCore import Qt

class MorpionView(QWidget):
    def __init__(self):
        super().__init__()
        self.setWindowTitle("Morpion")
        self.resize(400, 300)
        self.setStyleSheet("background-color: lightgray;")
#permet de créer la fenêtre avec un tritre et une taille
        self.question_label = QLabel("Ready to test your tic tac toe skills ?", self)
        self.question_label.setAlignment(Qt.AlignCenter)
        self.question_label.setStyleSheet("font-size: 16px; font-weight: bold;")
        
        main_layout = QVBoxLayout()
        main_layout.addWidget(self.question_label)

