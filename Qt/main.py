from PyQt5.QtWidgets import QMainWindow
from PyQt5.QtCore import QSize


class MainWindow(QMainWindow):
    def __init__(self):
        super().__init__()

        self.setMinimumSize(QSize(640, 480))    
        self.setWindowTitle("Financial Control") 