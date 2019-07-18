"""Exemple OK
from pyvis.network import Network
import pandas as pd

got_net = Network(height="750px", width="100%", bgcolor="#222222", font_color="white")

# set the physics layout of the network
got_net.barnes_hut()
got_data = pd.read_csv("https://www.macalester.edu/~abeverid/data/stormofswords.csv")

sources = got_data['Source']
targets = got_data['Target']
weights = got_data['Weight']

edge_data = zip(sources, targets, weights)

for e in edge_data:
    src = e[0]
    dst = e[1]
    w = e[2]

    got_net.add_node(src, src, title=src)
    got_net.add_node(dst, dst, title=dst)
    got_net.add_edge(src, dst, value=w)

neighbor_map = got_net.get_adj_list()

# add neighbor data to node hover data
for node in got_net.nodes:
    node["title"] += " Neighbors:<br>" + "<br>".join(neighbor_map[node["id"]])
    node["value"] = len(neighbor_map[node["id"]])

got_net.show("gameofthrones.html")

"""

"""Test données MAP"""
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

    # neighbor_map = map_network.get_adj_list()

    # add neighbor data to node hover data
    # for node in got_net.nodes:
    #     print(node)
    # node["title"] += " Neighbors:<br>" + "<br>".join(neighbor_map[node[""]])
    # node["value"] = len(neighbor_map[node["id"]])

    map_network.show_buttons(filter_=['physics'])
    map_network.show("ERCMapGraph.html")


# create_graph(resultCSV)
