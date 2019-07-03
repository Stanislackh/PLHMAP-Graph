# -- coding: windows-1252 --
# Created by Slackh
# Github : https://github.com/Stanislackh

"""Prise en main de NetworkX tests en tout genre"""

import csv
import AlgoTestFormulesSandBox
from random import randrange
import networkx as nx
from networkx.algorithms.community import greedy_modularity_communities
import matplotlib.pyplot as plt

"""fonction qui permet de récupérer les arcs et les noeuds lire CSV on verra pour l'intégrer a l'algo"""


def lireNoeudCSV(nomFichier):
    global Noeud
    global nomNoeud
    global idNoeud
    global poids1Noeud
    global poids2Noeud

    with open(nomFichier, 'r', newline="") as csvfile:
        reader = csv.reader(csvfile, delimiter=";")

        Noeud = []
        nomNoeud = []
        idNoeud = []
        poids1Noeud = []
        poids2Noeud = []

        titre = 0

        for i in reader:
            if titre == 0:
                titre += 1
            else:
                Noeud.append(i[0])
                idNoeud.append(i[1])
                nomNoeud.append(i[2])
                poids1Noeud.append(i[3])
                poids2Noeud.append(i[4])


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


def random_color():  # Génère une couleur aléatoire en 8 bit

    color = []
    for i in range(3):
        r = randrange(256)
        color.append(r)

    return color


def dessinerGraphe():
    G = nx.Graph()  # Création du graphe

    cpt = 0
    for arc in tupleSourceTarget:
        G.add_edge(arc[0], arc[1])
        cpt += 1

    p = list(greedy_modularity_communities(G))
    sorted(p)
    colorCommunity = []
    for i in p:
        r = random_color()
        colorCommunity.append((i, r))  # Communauté et sa couleur associée

    print(colorCommunity)
    nx.draw_networkx(G, node_size=20, with_labels=True)
    plt.show()
    plt.savefig("Exemple1.png")


if __name__ == "__main__":
    lireNoeudCSV("Nodes.csv")
    print("")
    lireArcCSV("Edges.csv")
    dessinerGraphe()
