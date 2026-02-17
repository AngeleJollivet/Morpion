from PyQt5.QtWidgets import QWidget
class MorpionView(QWidget):
    def __init__(self):
        super().__init__()
        self.setWindowTitle("Morpion")
        self.resize(400, 300)