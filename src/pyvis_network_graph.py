# -- coding: utf-8 --
# Created by Slackh
# Github : https://github.com/Stanislackh

from pyvis.network import Network
import pandas as pd
import NouvelleMethode

def create_graph(resultCSV):
    map_network = Network(height="750px", width="100%", bgcolor="#222222", font_color="white")

    # set the physics layout of the network
    map_network.barnes_hut()
    map_network_data = pd.read_csv(resultCSV + ".csv")

    sources = map_network_data['Source']
    targets = map_network_data['Target']
    weights = map_network_data['Force_lien']

    edge_data = zip(sources, targets, weights)


    for e in edge_data:
        src = e[0]
        dst = e[1]
        w = e[2]

        map_network.add_node(src, src, title=str(src))
        map_network.add_node(dst, dst, title=str(dst))
        map_network.add_edge(src, dst, value=w)

    map_network.show_buttons(filter_=['physics'])
    map_network.show("ERCMapGraph.html")


# create_graph(resultCSV)
