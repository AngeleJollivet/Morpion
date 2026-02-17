from PyQt5.QtWidgets import QWidget
class MorpionView(QWidget):
    def __init__(self):
        super().__init__()
        self.setWindowTitle("Morpion")
        self.resize(400, 300)
        self.setStyleSheet("background-color: lightgray;")
#permet de créer la fenêtre avec un tritre et une taille
