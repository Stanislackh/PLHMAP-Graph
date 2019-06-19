# -- coding: windows-1252 --
# Created by Slackh
# Github : https://github.com/Stanislackh

"""Fichier test de GephiStreamer"""

import networkx as nx
import networkx.drawing
import matplotlib.pyplot as plt

"""Exemple ok"""
# G = nx.petersen_graph()
# plt.subplot(121)
#
# nx.draw(G, with_labels=True, font_weight='bold')
# plt.subplot(122)
#
# nx.draw_shell(G, nlist=[range(5, 10), range(5)], with_labels=True, font_weight='bold')
# plt.savefig("blap.png")
# plt.show()

# G = nx.Graph()
#
# listNodes = [1, 2, 3, 4, 5]
# listEdges = [(1, 2), (2, 3), (1, 5), (1, 4), (4, 5), (2, 4)]
#
# G.add_nodes_from(listNodes)
# G.add_edges_from(listEdges)
#
# print(G.number_of_nodes())
# print(G.number_of_edges())
#
# nx.draw(G, with_labels=True, font_weight='bold')
# plt.show()

from gephistreamer import graph
from gephistreamer import streamer

stream = streamer.Streamer(streamer.GephiWS(hostname="localhost", port=8080, workspace="workspace1"))

# Create a node with a custom_property
node_a = graph.Node("A",custom_property=1)

# Create a node and then add the custom_property
node_b = graph.Node("B")
node_b.property['custom_property']=2

# Add the node to the stream
# you can also do it one by one or via a list
# l = [node_a,node_b]
# stream.add_node(*l)
stream.add_node(node_a,node_b)

# Create edge
# You can also use the id of the node : graph.Edge("A","B",custom_property="hello")
edge_ab = graph.Edge(node_a,node_b,custom_property="hello")
stream.add_edge(edge_ab)