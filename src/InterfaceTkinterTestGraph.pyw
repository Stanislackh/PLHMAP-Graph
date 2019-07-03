# -- coding: utf-8 --
"""Interface Tkinter pour essayer d'intégrer Gephi"""

# Created by Slackh
# Github : https://github.com/Stanislackh

import InterfaceGraphe
import AlgoTestFormulesSandBox  # Importe les feuilles de tests
from matplotlib.rcsetup import validate_nseq_float

"""PyQt5"""
import result
import sys
import csv
from PyQt5 import QtGui
from PyQt5.QtWidgets import QMainWindow, QApplication, QAction, qApp, QFileDialog, QCheckBox, QGridLayout, QLabel, \
    QPushButton, QHBoxLayout, QScrollArea, QDialog, QMessageBox, QTabWidget, QWidget, QVBoxLayout
from PyQt5 import QtCore
from PyQt5.QtGui import QPixmap


class Principale(QMainWindow):
    def __init__(self):
        super().__init__()
        self.name = ""
        self.titre = ""
        self.id = ""

        # Importation brute des attestations
        self.checkBoxAll = []
        self.listCheckBox = []
        self.listLabel = []
        self.listo = []
        self.setUI()

    def setUI(self):
        # Bouton d'affichage aide de l'application
        aideAction = QAction('Aide', self)
        aideAction.setShortcut('Ctrl+Q')
        aideAction.setStatusTip("Affiche une fenêtre d'aide à l'utilisation")
        aideAction.triggered.connect(qApp.exit)

        # Bouton pour l'importation du fichier CSV
        importerCSV = QAction('Importer CSV', self)
        importerCSV.setStatusTip("Ouvre une fenêtre pour l'importation des fichiers")
        importerCSV.triggered.connect(self.openFileNameDialog)

        # Barre d'outils
        self.barreOutils = self.addToolBar('Tool Bar')
        self.barreOutils.addAction(importerCSV)
        self.barreOutils.addAction(aideAction)

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
            print("check")
            i.setChecked(True)

    # Uncheck All
    def decocheTout(self):
        for i in self.checkBoxAll:
            print("uncheck")
            i.setChecked(False)

    # Affiche le graphe associé à la coocurence
    def afficheConcomittanceGraph(self):
        self.my_dialog = QDialog(self)
        # my_dialog.setPixmap(QPixmap('screenshotCooccurrenceCorrigée.png'))
        self.my_dialog.setGeometry(300, 300, 1024, 768)
        self.my_dialog.setWindowTitle('PLH / MAP')
        self.my_dialog.exec_()  # blocks all other windows until this window is closed.

    # Affiche le graphe associé aux graphe valué
    def afficheValuateGraph(self):
        self.my_dialog = QDialog(self)
        # my_dialog.setPixmap(QPixmap('screenshotCooccurrenceCorrigée.png'))
        self.my_dialog.setGeometry(300, 300, 1024, 768)
        self.my_dialog.setWindowTitle('PLH / MAP')
        self.my_dialog.exec_()  # blocks all other windows until this window is closed.

    # Fonction ouverture de fichier
    def openFileNameDialog(self):
        options = QFileDialog.Options()
        options != QFileDialog.DontUseNativeDialog
        fileName, _ = QFileDialog.getOpenFileNames(self, "Importer fichier CSV", "",
                                                   "All Files (*);;CSV Files (*.csv)", options=options)

        if fileName:
            page = 0
            for i in fileName:  # i == Path du fichier
                with open(i, 'r', newline="") as csvfile:
                    reader = csv.reader(csvfile, delimiter=";")

                    cle = 0
                    for l in reader:  # Nomme toutes les checkbox
                        if cle == 0:
                            self.titre = l[1]
                            self.id = l[0]
                            cle += 1
                        else:
                            name = "checkbox_" + str(cle)
                            self.listCheckBox.append(name)
                            self.listLabel.append(l)
                            cle += 1

                    print(self.listCheckBox)
                    print(self.listLabel)

                    # indice, marge = 0
                    for k, v in enumerate(self.listCheckBox):
                        print(k)
                        print(v)
                        self.listo.append(QCheckBox(str(k)))
                        print(self.listo[k])

                        # self.nam1 = QCheckBox(self.listLabel[k], self)
                        # print(self.nam1)
                        # self.nam1 = QCheckBox(self.listLabel[indice], self)
                        # self.checkBoxAll.append(self.nam1)
                        # self.nam1.setChecked(True)
                        # self.nam1.move(20, 20 + marge)
                        # self.nam1.resize(320, 40)
                        #
                        # indice += 1
                        # marge += 20
            Principale.afficherBoutons(self)
            # Principale.placeCB(self)
        return self

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
            Principale.placeCB(self, i, marge)
            marge += 20

    # Affiche la fenêtre d'aide
    def afficheAide(self):
        self.aideDialog = QDialog(self)

    """Liste des fonctions utilisés"""

    # CheckAll fonction
    def cocheTout(self):
        for i in self.checkBoxAll:
            print("check")
            i.setChecked(True)

    # Uncheck All
    def decocheTout(self):
        for i in self.checkBoxAll:
            print("uncheck")
            i.setChecked(False)

    # Affiche le graphe associé à la coocurence
    def afficheConcomittanceGraph(self):
        self.my_dialog = QDialog(self)
        # my_dialog.setPixmap(QPixmap('screenshotCooccurrenceCorrigée.png'))
        self.my_dialog.setGeometry(300, 300, 1024, 768)
        self.my_dialog.setWindowTitle('PLH / MAP')
        self.my_dialog.exec_()  # blocks all other windows until this window is closed.

    # Affiche le graphe associé aux graphe valué
    def afficheValuateGraph(self):
        self.my_dialog = QDialog(self)
        # my_dialog.setPixmap(QPixmap('screenshotCooccurrenceCorrigée.png'))
        self.my_dialog.setGeometry(300, 300, 1024, 768)
        self.my_dialog.setWindowTitle('PLH / MAP')
        self.my_dialog.exec_()  # blocks all other windows until this window is closed.

    # Affiche les boutons
    def afficherBoutons(self):
        # Bouton pour check toutes les propositions
        checkAll = QPushButton("Check All", self.centralwidget)
        checkAll.setToolTip('Permet de cocher tout')
        checkAll.clicked.connect(self.cocheTout)
        checkAll.move(150, 360)
        checkAll.show()

        # Bouton pour uncheck les propositions
        uncheckAll = QPushButton("Uncheck All", self.centralwidget)
        uncheckAll.setToolTip('Permet de tout désélectionner')
        uncheckAll.clicked.connect(self.decocheTout)
        uncheckAll.move(50, 360)
        uncheckAll.show()

        # Bouton traitement coocurence
        coocurence = QPushButton("Coocurrence", self.centralwidget)
        coocurence.setToolTip("Affiche le graphe avec l'algorithme de coocurence")
        coocurence.clicked.connect(self.afficheConcomittanceGraph)
        coocurence.move(250, 360)
        coocurence.show()

        # Bouton traintement graphe value
        valuateGraph = QPushButton("Graphe Valué", self.centralwidget)
        valuateGraph.setToolTip("Affiche le graphe avec l'algorithme de Graphe valué")
        valuateGraph.clicked.connect(self.afficheValuateGraph)
        valuateGraph.move(350, 360)
        valuateGraph.show()



if __name__ == "__main__":
    monApp = QApplication(sys.argv)
    fenetre = Principale()
    sys.exit(monApp.exec_())
