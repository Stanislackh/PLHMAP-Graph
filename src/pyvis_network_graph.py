# -- coding: utf-8 --
# Created by Slackh
# Github : https://github.com/Stanislackh

from pyvis.network import Network
import pandas as pd
import NouvelleMethode
from datetime import datetime


def create_graph(resultCSV):
    map_network = Network(height="750px", width="100%", bgcolor="#222222", font_color="white")

    # Met en place la physique du graphe
    map_network.barnes_hut()
    map_network_data = pd.read_csv(resultCSV + ".csv")

    sources = map_network_data['Source']
    targets = map_network_data['Target']
    weights = map_network_data['Force_lien']
    forceSrc = map_network_data['ForceSrc']
    forceTgt = map_network_data['ForceTgt']

    edge_data = zip(sources, targets, weights, forceSrc, forceTgt)  # Lie les informations

    for e in edge_data:
        src = e[0]
        dst = e[1]
        w = e[2]
        v1 = e[3]
        v2 = e[4]

        map_network.add_node(src, src, title=str(src), value=v1)
        map_network.add_node(dst, dst, title=str(dst), value=v2)
        map_network.add_edge(src, dst, value=w)

    voisins = map_network.get_network_data()  # Récupère les informations sur le graphe

    listeVoisins = []  # Liste des noeuds voisins

    for info in voisins[1]:  # Récupère les arcs
        # print(info)
        listeVoisins.append(info)

    for info in voisins[0]:  # Récupère les infos pour chaque noeud

        info['title'] += " à une valeur de: " + str(info['value'])  # Permet l'affichage des infos sur le noeud
        info['title'] += " <br>"

        for cle in range(len(listeVoisins)):  # Regarde les infos pour chaque arc
            if info['label'] == listeVoisins[cle]['from']:  # Les infos pour chaque départ d'arc et les affiche
                info['title'] += "lié avec: " + listeVoisins[cle]['to'] + " : " + str(listeVoisins[cle]['value'])
                info['title'] += "<br>"

            if info['label'] == listeVoisins[cle]['to']:  # Les infos pour chaque arrivée d'arc et les affiche
                info['title'] += "lié avec: " + listeVoisins[cle]['from'] + " : " + str(listeVoisins[cle]['value'])
                info['title'] += "<br>"

    map_network.show_buttons(filter_=['nodes', 'edges', 'physics'])  # Affiche les boutons pour les options

    # Récupère l'heure et la date du jour
    date = datetime.now()
    datestr = date.strftime('_%Y-%m-%d-%H-%M-%S')

    map_network.save_graph("ERCMapGraph" + datestr + ".html")  # Sauvegarde le graphe
    map_network.show("ERCMapGraph" + datestr + ".html")  # Affiche le graphe


if __name__ == "__main__":
    create_graph("CSVTraiteMAP/CalculMAP_Edges_2019-09-02-13-11-53")
