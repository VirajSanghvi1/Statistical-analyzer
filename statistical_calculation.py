from PyQt5.QtWidgets import *
from PyQt5.QtWidgets import (QWidget, QLabel, QComboBox, QApplication)
import sys



class App(QWidget):
    def __init__(self):
        super().__init__()
        self.title = "Statistical Calculation"
        self.left = 10
        self.top = 10
        self.width = 640
        self.height = 480
        self.initUI()

    def initUI(self):
        self.setWindowTitle(self.title)
        self.setGeometry(self.left, self.top, self.width, self.height)

        combo = QComboBox(self)
        combo.addItem("Mean")
        combo.addItem("Median")
        combo.addItem("Mode")
        combo.addItem("Standard Deviation")
        combo.addItem("Variance")
        combo.addItem("Coefficient Of Variance")
        combo.addItem("Percentiles")
        combo.addItem("Probability Distribution")
        combo.addItem("Binomial Distribution")
        combo.addItem("Least Square Line")
        combo.addItem("Chi Square")
        combo.addItem("Correlation Coefficient")
        combo.addItem("Sign Test")
        combo.addItem("Rank Sum Test")
        combo.addItem("Spearman Rank Correlation Coefficient")

        self.setGeometry(10, 10, 640, 480)
        self.setWindowTitle('Statistical Calculation')
        self.show()








if __name__ == '__main__':
    app = QApplication(sys.argv)
    ex = App()
    sys.exit(app.exec_())