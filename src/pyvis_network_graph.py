# -- coding: latin1 --
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
    # weightNode = map_network_data['Id']

    edge_data = zip(sources, targets, weights)

    for e in edge_data:
        src = e[0]
        dst = e[1]
        w = e[2]
        # k = e[3]

        map_network.add_node(src, src, title=str(src))
        map_network.add_node(dst, dst, title=str(dst))
        map_network.add_edge(src, dst, value=str(w))

    # voisins = map_network.get_adj_list()
    #
    # for info in map_network.nodes:
    #     print(info)
        # info['title'] += " Valeurs:<br>" + "<br>".join(voisins[info["value"]])

    map_network.show_buttons(filter_=['nodes', 'edges', 'physics'])
    map_network.save_graph("ERCMapGraph.html")
    map_network.show("ERCMapGraph.html")


if __name__ == "__main__":
    create_graph("CSVTraiteMAP/CalculEG_Edges_2019-08-30-10-58-12")
