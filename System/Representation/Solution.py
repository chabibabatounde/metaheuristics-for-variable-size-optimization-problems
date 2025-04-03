import random

import networkx as nx
import matplotlib.pyplot as plt
from System.Evaluation.Simulator import Simulator


class Solution:
    __graph = None
    __score = 0
    __dict = 0

    def show(self):
        pos = nx.spring_layout(self.__graph)
        nx.draw(self.__graph, pos, with_labels=True, arrows=True)
        plt.show()

    def __init__(self, solution, partial):
        self.__dict = solution
        self.__score = 0
        partial = partial.get_match_table()
        graph = nx.Graph()
        graph.add_node('ROOT', data=solution, partial=partial)
        action_id = 0
        param_id = 0
        for perception in solution['perceptions']:
            p = perception['perception']
            graph.add_node(p.name, data=p, partial=p)
            graph.add_edge('ROOT', p.name)
            i = 0
            for action in perception['actions']:
                action_id += 1
                graph.add_node(action.name + str(action_id))
                graph.add_edge(action.name + str(action_id), p.name, data=action, partial=partial[p.name][i])
                for attr, valeur in vars(action).items():
                    param_id += 1
                    param_p = None
                    if attr not in ['name']:
                        for a in partial[p.name][i].variables_partial_knowledge:
                            if attr == a.name:
                                param_p = a.name
                                break
                        graph.add_node(attr + str(param_id), data=valeur)
                        graph.add_edge(attr + str(param_id), action.name + str(action_id), data=action, partial=param_p)
            i += 1
        self.__graph = graph

    def eval(self, df):
        simulator = Simulator(self, df)
        data = simulator.run(len(df))
        return random.uniform(0, 100)

    def get_graph(self):
        return self.__graph

    def get_dict(self):
        return self.__dict
