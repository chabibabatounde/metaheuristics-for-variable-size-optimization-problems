import networkx as nx


class Solution:
    __graph = None

    def __init__(self):
        self.__graph = nx.Graph()

    def get_node(self, node_id):
        print("")
