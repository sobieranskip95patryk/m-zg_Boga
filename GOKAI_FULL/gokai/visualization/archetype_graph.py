
import networkx as nx
import matplotlib.pyplot as plt

def draw_archetypes(nodes=("HEAVEN","HELL")):
    G = nx.Graph()
    G.add_nodes_from(nodes)
    G.add_edge("HEAVEN","HELL")
    pos = nx.spring_layout(G, seed=7)
    fig = plt.figure()
    nx.draw(G, pos, with_labels=True)
    return fig
