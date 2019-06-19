# -- coding: utf-8 --
"""Interface Tkinter pour essayer d'intégrer Gephi"""

# Created by Slackh
# Github : https://github.com/Stanislackh

import InterfaceGraphe
import AlgoTestFormulesSandBox  # Importe les feuilles de tests

"""PyQt5"""

import sys
from PyQt5 import QtGui
from PyQt5.QtWidgets import QMainWindow, QApplication, QAction, qApp, QFileDialog, QCheckBox, QGridLayout, QLabel, \
    QPushButton, QHBoxLayout, QScrollArea, QDialog, QMessageBox
from PyQt5 import QtCore
from PyQt5.QtGui import QPixmap


class Principale(QMainWindow):
    def __init__(self):
        super().__init__()

        # nommage des checkBox
        cle = 0
        for i in AlgoTestFormulesSandBox.attestations:
            name = "checkbox_" + str(cle)
            self.name = ""

        # Importation brute des attestations
        self.checkBoxAll = []
        self.listCheckBox = []
        self.listLabel = []
        self.listo = []
        cle = 0

        for i in AlgoTestFormulesSandBox.attestations:  # Nomme toutes les checkbox
            name = "checkbox_" + str(cle)
            self.listCheckBox.append(name)
            self.listLabel.append(i)
            cle += 1

        for i, v in enumerate(self.listCheckBox):
            self.listo.append(QCheckBox(str(i)))

        self.setUI()

    def setUI(self):
        # Bouton de fermeture de l'application
        exitAction = QAction('&Exit', self)
        exitAction.setShortcut('Ctrl+Q')
        exitAction.setStatusTip("Quitter l'application")
        exitAction.triggered.connect(qApp.exit)

        # Bouton pour l'importation du fichier CSV
        importerCSV = QAction('Importer CSV', self)
        importerCSV.setStatusTip("Ouvre une fenêtre pour l'importation du fichier")
        importerCSV.triggered.connect(self.openFileNameDialog)

        # Barre d'outils
        self.barreOutils = self.addToolBar('Quitter')
        self.barreOutils.addAction(importerCSV)
        self.barreOutils.addAction(exitAction)

        # Barre déroulante
        self.scrollArea = QScrollArea()

        # Liste de checkbox
        def placeCB(self, indice=0, marge=0):
            self.nam1 = QCheckBox(self.listLabel[indice], self)
            self.checkBoxAll.append(self.nam1)
            self.nam1.setChecked(True)
            self.nam1.move(20, 20 + marge)
            self.nam1.resize(320, 40)

        # Place toutes les attestations
        marge = 0
        for i in range(len(self.listLabel)):
            placeCB(self, i, marge)
            marge += 20

        # Bouton pour check toutes les propositions
        checkAll = QPushButton("Check All", self)
        checkAll.setToolTip('Permet de cocher tout')
        checkAll.clicked.connect(self.cocheTout)
        checkAll.move(150, 360)
        checkAll.show()

        # Bouton pour uncheck les propositions
        uncheckAll = QPushButton("Uncheck All", self)
        uncheckAll.setToolTip('Permet de tout désélectionner')
        uncheckAll.clicked.connect(self.decocheTout)
        uncheckAll.move(50, 360)
        uncheckAll.show()

        # Bouton suivant et traitement
        traiter = QPushButton("Graphe", self)
        traiter.setToolTip('Affiche le graphe associé')
        traiter.clicked.connect(self.afficheGraphe)
        traiter.move(250, 360)
        traiter.show()

        # Paramètres de la Fenêtre
        self.label = QLabel(self)
        self.label.setPixmap(QPixmap('map.png'))
        self.label.setGeometry(400, 50, 175, 175)
        self.setGeometry(300, 300, 500, 410)
        self.setWindowTitle('PLH / MAP')
        self.statusBar().showMessage('')
        self.show()

    """Liste des fonctions utilisés"""

    # CheckAll fonction
    def cocheTout(self):
        for i in self.checkBoxAll:
            i.setChecked(True)

    # Uncheck All
    def decocheTout(self):
        for i in self.checkBoxAll:
            i.setChecked(False)

    # Affiche le graphe associé
    def afficheGraphe(self):
        self.my_dialog = QDialog(self)
        # my_dialog.setPixmap(QPixmap('screenshotCooccurrenceCorrigée.png'))
        self.my_dialog.setGeometry(300, 300, 1024, 768)
        self.my_dialog.setWindowTitle('PLH / MAP')

        self.my_dialog.exec_()  # blocks all other windows until this window is closed.

    # Fonction ouverture de fichier
    def openFileNameDialog(self):
        options = QFileDialog.Options()
        options != QFileDialog.DontUseNativeDialog
        fileName, _ = QFileDialog.getOpenFileName(self, "Importer fichier CSV", "",
                                                  "All Files (*);;CSV Files (*.csv)", options=options)
        if fileName:
            print(fileName)


if __name__ == "__main__":
    monApp = QApplication(sys.argv)
    fenetre = Principale()
    sys.exit(monApp.exec_())
