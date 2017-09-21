import sys
import pandas as pd
from PyQt5.QtWidgets import QApplication, QWidget, QPushButton, QFileDialog, QTableWidget, QTableWidgetItem, QVBoxLayout
from PyQt5.QtCore import pyqtSlot


class App(QWidget):
    # global variable for df
    globvar = 0

    def __init__(self):
        super().__init__()
        self.title = 'PyQt5 simple window - pythonspot.com'
        self.left = 10
        self.top = 10
        self.width = 660
        self.height = 500
        self.initUI()

    def initUI(self):
        self.setWindowTitle(self.title)
        self.setGeometry(self.left, self.top, self.width, self.height)

        button = QPushButton('Open a file', self)
        button.setToolTip('Load a data file')
        button.move(560, 475)
        button.clicked.connect(self.on_click)

        self.show()

    #Function used to open the File Dialog so that the user can select a file
    def openFileNameDialog(self):
        options = QFileDialog.Options()
        options = QFileDialog.DontUseNativeDialog
        fileName, _ = QFileDialog.getOpenFileName(self, "QFileDialog.getOpenFileName()", "",
                                                  "Comma Separated Values (*.csv)", options=options)
        if fileName:
            print(fileName)
            return(fileName)

    #Creates the editable table using PyQt and Pandas Dataframe
    def createTable(self, df):
        #row and column count
        rows, columns = df.shape

        #horizontal and vertical labels
        row_label = list(df.index)
        columns_label = list(df.columns.values)

        #create the table
        self.tableWidget = QTableWidget()
        self.tableWidget.setRowCount(rows)
        self.tableWidget.setColumnCount(columns)

        #add information to the table
        for i in range(rows):
            self.tableWidget.setVerticalHeaderItem(i, QTableWidgetItem(row_label[i]))
            for j in range(columns):
                self.tableWidget.setItem(i, j, QTableWidgetItem(str(df.get_value(row_label[i],columns_label[j]))))

                if i < 1:
                    self.tableWidget.setHorizontalHeaderItem(j, QTableWidgetItem(columns_label[j]))

        #new Boxlayout for displaying the table and the table to it
        self.layout = QVBoxLayout()
        self.layout.addWidget(self.tableWidget)
        self.setLayout(self.layout)

    @pyqtSlot()
    def on_click(self):
        filename = self.openFileNameDialog()
        df = pd.read_csv(filename)

        self.createTable(df)

        print(df)
        print('Clicked')

        global globvar  # Needed to modify global copy of globvar
        globvar = df

    def get_global(self):
        return globvar

    #def getmean(self):
        #Second column
        k=df.iloc[:,1]
        print(k.mean())
        print(k.median())
        #Returns item that appears the most
        #May return more than 1 value
        print(k.mode())
        #Perform standard deviation
        print(k.std())
        #Perform variance of sample calculation
        print(k.var())
        #Item in 4th row 1st item
        #print(df.iloc[3,0])
        # row to row,column to column
        #print(df.iloc[0:1, 0: 2])

if __name__ == '__main__':
    app = QApplication(sys.argv)
    ex = App()
    sys.exit(app.exec_())

class statistics(App):
    # global variable for df
#    globvar2 = 0

    t= App()
#    t.get_global()

    globvar2=t.get_global()

    def singleColumn(self):
        global globvar2
        #col=self
        col=1
        # Second column
        k = globvar2.iloc[:, col]
        #k= self + 2
        print(k)
        #return k

    def getmean(self):
        #k=self
        df=globvar
        k = df.iloc[:, 1]
        print(k.mean())

    def getmedian(self):
        k=self
        print(k.median())

    def getmode(self):
        k=self
        print(k.mode())

    def getstd(self):
        k=self
        print(k.std())

    def getvariance(self):
        k=self
        print(k.var())


if __name__ == '__main__':
    foo = statistics()
    foo.singleColumn()




