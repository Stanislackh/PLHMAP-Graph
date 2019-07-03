# -- coding: windows-1252 --
# Created by Slackh
# Github : https://github.com/Stanislackh


from graphviz import Digraph
import os
import TestCreationGraphNetworkX
import csv

os.environ["PATH"] += os.pathsep + 'C:/Program Files (x86)/Graphviz2.38/bin/'

from graphviz import Graph

g = Graph('G', filename='process.gv', engine='sfdp')


def lireArcCSV(nomFichier):
    global tupleSourceTarget
    global typeArc
    global idArc
    global poidsArc

    with open(nomFichier, 'r', newline="") as csvfile:
        reader = csv.reader(csvfile, delimiter=";")

        tupleSourceTarget = []
        typeArc = []
        idArc = []
        poidsArc = []

        titre = 0

        for i in reader:
            if titre == 0:
                titre += 1
            else:
                tupleSourceTarget.append((i[0], i[1]))
                typeArc.append(i[2])
                idArc.append(i[3])
                poidsArc.append(i[5])


    cpt = 0
    for arc in tupleSourceTarget:
        g.edge(arc[0], arc[1])
        cpt += 1


    g.view()

lireArcCSV("Edges.csv")