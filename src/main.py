from PyQt5 import QtWidgets
from PyQt5.QtWidgets import QApplication, QMainWindow
from PyQt5 import QtGui
from PyQt5 import QtCore
import sys

def window():
    app = QApplication(sys.argv)
    win = QMainWindow()
    win.setGeometry(300, 300, 1200, 1000)
    win.setWindowTitle("Cost-Benefit Analysis Tool")


    label = QtWidgets.QLabel(win)
    label.setText('Window with text!')
    label.setFont(QtGui.QFont('Arial', 12))
    label.move(50, 50)
    #label.setAlignment(QtCore.Qt.AlignRight)
    

    b1 = QtWidgets.QPushButton(win)
    b1.setText("Click Me!")


    win.show()
    sys.exit(app.exec_()) # Makes a clean exit. 




window()
