import sys
import time

from PySide6.QtWidgets import QApplication, QMainWindow, QFileDialog, QMessageBox, QWidget, QVBoxLayout, QProgressBar, QPushButton

from progressBar import Ui_MainWindow


class Progers(QMainWindow):
    def __init__(self):
        super(Progers, self).__init__()

        self.ui = Ui_MainWindow()
        self.ui.setupUi(self)

        for i in range(200):
            time.sleep(0.5)
            self.ui.progressBar.setBackgroundRole(0)



if __name__ == "__main__":
    app = QApplication(sys.argv)

    demo = Progers()
    demo.show()


    sys.exit(app.exec())
