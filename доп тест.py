from PySide6.QtWidgets import QApplication, QMainWindow, QFileDialog, QMessageBox
from info import Ui_MainWindow

import sys


class Root(QMainWindow):
    def __init__(self):
        super(Root, self).__init__()
        self.ui = Ui_MainWindow()
        self.ui.setupUi(self)



if __name__ == "__main__":
    app = QApplication(sys.argv)

    window = Root()
    window.show()

    sys.exit(app.exec())