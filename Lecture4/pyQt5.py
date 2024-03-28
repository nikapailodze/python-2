from PyQt5 import QtWidgets
from PyQt5.QtWidgets import QApplication, QMainWindow, QLabel
import sys

def main():
    app = QApplication(sys.argv)
    win=QMainWindow()
    win.setGeometry(200,200,1000,1000)

    label = QLabel(win)
    label.setText("my first label ")
    label.move(150,150)

    win.show()
    sys.exit(app.exec_())

main()