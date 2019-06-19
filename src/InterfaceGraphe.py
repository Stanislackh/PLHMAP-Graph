"""PyQt5"""

import sys
from PyQt5 import QtGui, QtWidgets
from PyQt5.QtWidgets import QMainWindow, QApplication, QAction, qApp, QFileDialog, QCheckBox, QGridLayout, QLabel, \
    QPushButton, QHBoxLayout, QScrollArea, QWidget
from PyQt5 import QtCore
from PyQt5.QtGui import QPixmap


class Secondaire(QtWidgets.QWidget):

    def __init__(self):
        super().__init__()
        self.afficherGraphe()

    def afficherGraphe(self):
        self.label = QLabel(self)
        self.label.setPixmap(QPixmap('screenshotCooccurrenceCorrigée.png'))
        self.label.setGeometry(0, 0, 1024, 768)
        self.setGeometry(300, 300, 1024, 768)
        self.setWindowTitle('PLH / MAP')
        self.show()

if __name__ == "__main__":
    monApp = QApplication(sys.argv)
    fenetre = Secondaire()
    sys.exit(monApp.exec_())