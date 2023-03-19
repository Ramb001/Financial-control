from PyQt5.QtWidgets import QApplication, QLabel
from Qt.main import MainWindow

if __name__ == "__main__":
    app = QApplication([])
    window = MainWindow()
    window.show()
    app.exec_()