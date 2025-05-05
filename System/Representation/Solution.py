import networkx as nx
import matplotlib.pyplot as plt
import pandas as pd
from System.Core.Simulator import Simulator


class Solution:
    __graph = None
    __score = 0
    __dict = 0

    def show(self):
        def hierarchy_pos(G, root, width=1.0, vert_gap=0.2, vert_loc=0, xcenter=0.5):
            pos = {}
            pos[root] = (xcenter, vert_loc)
            neighbors = list(G.neighbors(root))
            if len(neighbors) != 0:
                sub_width = width / len(neighbors)
                for neighbor in neighbors:
                    pos.update(hierarchy_pos(G, neighbor, sub_width, vert_gap, vert_loc - vert_gap, xcenter))
                    xcenter += sub_width
            return pos
        pos = hierarchy_pos(self.__graph, list(self.__graph.nodes)[0])
        plt.figure(figsize=(25, 10))
        nx.draw(self.__graph, pos, with_labels=True, node_color='lightblue', node_size=500, font_size=10)
        plt.show()

    def init_from_partial(self, solution, partial):
        self.__graph = None
        self.__dict = solution
        self.__score = 0
        partial = partial.get_match_table()
        graph = nx.DiGraph()
        node_id = 0
        graph.add_node('ROOT', data=solution, type='root', partial=partial)
        action_id = 0
        param_id = 0
        for perception in solution['perceptions']:
            p = perception['perception']
            graph.add_node(p.name, data=p, type='perception', partial=p)
            node_id += 1
            graph.add_edge('ROOT', p.name)
            i = 0
            for action in perception['actions']:
                action_id += 1
                graph.add_node(action.name + str(action_id), data=action, type='action', partial='Perception')
                node_id += 1
                graph.add_edge(p.name, action.name + str(action_id))
                for attr, valeur in vars(action).items():
                    param_id += 1
                    param_p = None
                    if attr not in ['name']:
                        for a in partial[p.name][i].variables_partial_knowledge:
                            if attr == a.name:
                                param_p = a.name
                                break
                        graph.add_node(attr + str(param_id), data=valeur, type='param', partial=valeur)
                        node_id += 1
                        graph.add_edge(action.name + str(action_id), attr + str(param_id))
            i += 1
        self.__graph = graph

    def eval(self, df, target_variables, function, initial_params, env):
        variables = target_variables.copy()
        target_data = 0
        simulator = Simulator(self, initial_params, env)
        data = simulator.run(len(df))
        agent_data = data['agent_data'].xs(key=target_data, level=1)
        model_data = data['model_data']
        available_steps = agent_data.index.get_level_values('Step').unique()
        predicted_values = pd.DataFrame()
        additional_variables = []
        if 'position' in variables:
            position_series = agent_data.loc[available_steps, 'position']
            predicted_values = position_series.reset_index()
            predicted_values.columns = ['step', 'position']
            predicted_values['x'] = predicted_values['position'].apply(lambda pos: pos[0])
            predicted_values['y'] = predicted_values['position'].apply(lambda pos: pos[1])
            predicted_values = predicted_values.drop('position', axis=1)
            variables.remove('position')
            additional_variables += ['x', 'y']
        for var in variables:
            predicted_values[var] = agent_data.loc[available_steps, var].reset_index()[var]
        variables += additional_variables
        self.__score = function(df, predicted_values, variables)
        return self.__score

    def get_graph(self):
        return self.__graph

    def get_dict(self):
        return self.__dict

    def init_from_graph(self, graph):
        self.__dict = {
            'name': 'generated',
            'perceptions': []
        }
        self.__score = 0
        perceptions = list(graph.successors(list(graph.nodes())[0]))
        for p in perceptions:
            perception = {'perception': graph.nodes[p]['data'], 'actions': []}
            actions = list(graph.successors(p))
            for a in actions:
                action = graph.nodes[a]['data']
                parameters = list(graph.successors(a))
                if len(action.get_attributes()) != len(list(graph.successors(a))):
                    print('Problem @', self, '\n\t', parameters)
                    nx.draw(graph, with_labels=True)
                    plt.show()
                    exit(self)
                params = []
                for parameter in parameters:
                    params.append(graph.nodes[parameter]['data'])
                action.init_params(params)
                perception['actions'].append(action)
            self.__dict['perceptions'].append(perception)
        self.__graph = graph
