import sys
import pandas as pd
from PyQt5.QtWidgets import QApplication, QWidget, QPushButton, QInputDialog, QLineEdit, QFileDialog
from PyQt5.QtGui import QIcon
from PyQt5.QtCore import pyqtSlot


class App(QWidget):

    def __init__(self):
        super().__init__()
        self.title = 'PyQt5 simple window - pythonspot.com'
        self.left = 10
        self.top = 10
        self.width = 640
        self.height = 480
        self.initUI()

    def initUI(self):
        self.setWindowTitle(self.title)
        self.setGeometry(self.left, self.top, self.width, self.height)

        button = QPushButton('Open a file', self)
        button.setToolTip('Load a data file')
        button.move(535, 450)
        button.clicked.connect(self.on_click)

        self.show()

    def openFileNameDialog(self):
        options = QFileDialog.Options()
        options = QFileDialog.DontUseNativeDialog
        fileName, _ = QFileDialog.getOpenFileName(self, "QFileDialog.getOpenFileName()", "",
                                                  "Comma Separated Values (*.csv)", options=options)
        if fileName:
            print(fileName)
            return(fileName)

    @pyqtSlot()
    def on_click(self):
        filename = self.openFileNameDialog()
        df = pd.read_csv(filename)
        print(df)
        print('Clicked')


if __name__ == '__main__':
    app = QApplication(sys.argv)
    ex = App()
    sys.exit(app.exec_())
