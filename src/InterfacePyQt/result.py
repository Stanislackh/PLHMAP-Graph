# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'result.ui'
#
# Created by: PyQt5 UI code generator 5.11.3
#
# WARNING! All changes made in this file will be lost!

from PyQt5 import QtCore, QtGui, QtWidgets

class Ui_PLHMAP(object):
    def setupUi(self, PLHMAP):
        PLHMAP.setObjectName("PLHMAP")
        PLHMAP.resize(500, 410)

        self.centralwidget = QtWidgets.QWidget(PLHMAP)
        self.centralwidget.setObjectName("centralwidget")

        self.pushButton = QtWidgets.QPushButton(self.centralwidget)
        self.pushButton.setGeometry(QtCore.QRect(60, 320, 75, 23))
        self.pushButton.setObjectName("pushButton")

        self.pushButton_2 = QtWidgets.QPushButton(self.centralwidget)
        self.pushButton_2.setGeometry(QtCore.QRect(160, 320, 75, 23))
        self.pushButton_2.setObjectName("pushButton_2")

        self.pushButton_3 = QtWidgets.QPushButton(self.centralwidget)
        self.pushButton_3.setGeometry(QtCore.QRect(250, 320, 75, 23))
        self.pushButton_3.setObjectName("pushButton_3")

        self.pushButton_4 = QtWidgets.QPushButton(self.centralwidget)
        self.pushButton_4.setGeometry(QtCore.QRect(350, 320, 75, 23))
        self.pushButton_4.setObjectName("pushButton_4")

        self.tabWidget = QtWidgets.QTabWidget(self.centralwidget)
        self.tabWidget.setGeometry(QtCore.QRect(20, 20, 311, 291))
        self.tabWidget.setObjectName("tabWidget")

        self.tab = QtWidgets.QWidget()
        self.tab.setObjectName("tab")

        self.verticalScrollBar_2 = QtWidgets.QScrollBar(self.tab)
        self.verticalScrollBar_2.setGeometry(QtCore.QRect(10, 10, 16, 241))
        self.verticalScrollBar_2.setOrientation(QtCore.Qt.Vertical)
        self.verticalScrollBar_2.setObjectName("verticalScrollBar_2")

        self.tabWidget.addTab(self.tab, "")
        self.tab_2 = QtWidgets.QWidget()
        self.tab_2.setObjectName("tab_2")

        self.verticalScrollBar = QtWidgets.QScrollBar(self.tab_2)
        self.verticalScrollBar.setGeometry(QtCore.QRect(10, 10, 16, 241))
        self.verticalScrollBar.setOrientation(QtCore.Qt.Vertical)
        self.verticalScrollBar.setObjectName("verticalScrollBar")

        self.tabWidget.addTab(self.tab_2, "")
        PLHMAP.setCentralWidget(self.centralwidget)

        self.statusbar = QtWidgets.QStatusBar(PLHMAP)
        self.statusbar.setObjectName("statusbar")

        PLHMAP.setStatusBar(self.statusbar)
        self.menubar = QtWidgets.QMenuBar(PLHMAP)

        self.menubar.setGeometry(QtCore.QRect(0, 0, 500, 21))
        self.menubar.setObjectName("menubar")

        self.menuImport_CSV = QtWidgets.QMenu(self.menubar)
        self.menuImport_CSV.setObjectName("menuImport_CSV")

        self.menuAide = QtWidgets.QMenu(self.menubar)
        self.menuAide.setObjectName("menuAide")

        PLHMAP.setMenuBar(self.menubar)

        self.menubar.addAction(self.menuImport_CSV.menuAction())
        self.menubar.addAction(self.menuAide.menuAction())

        self.retranslateUi(PLHMAP)
        self.tabWidget.setCurrentIndex(0)
        QtCore.QMetaObject.connectSlotsByName(PLHMAP)

    def retranslateUi(self, PLHMAP):

        _translate = QtCore.QCoreApplication.translate
        PLHMAP.setWindowTitle(_translate("PLHMAP", "PLH / MAP"))
        self.pushButton.setText(_translate("PLHMAP", "Check All"))
        self.pushButton_2.setText(_translate("PLHMAP", "Uncheck All"))
        self.pushButton_3.setText(_translate("PLHMAP", "Coocurrence"))
        self.pushButton_4.setText(_translate("PLHMAP", "Graphe Value"))

        self.tabWidget.setTabText(self.tabWidget.indexOf(self.tab), _translate("PLHMAP", "Tab 1"))
        self.tabWidget.setTabText(self.tabWidget.indexOf(self.tab_2), _translate("PLHMAP", "Tab 2"))
        self.menuImport_CSV.setTitle(_translate("PLHMAP", "Import CSV"))
        self.menuAide.setTitle(_translate("PLHMAP", "Aide"))


if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    PLHMAP = QtWidgets.QMainWindow()
    ui = Ui_PLHMAP()
    ui.setupUi(PLHMAP)
    PLHMAP.show()
    sys.exit(app.exec_())

