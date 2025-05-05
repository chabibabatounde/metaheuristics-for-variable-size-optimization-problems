import random

import matplotlib.pyplot as plt

from System.Algorithms.Algorithm import Algorithm
from System.Representation.Solution import Solution
import networkx as nx


class Genetic(Algorithm):

    def __init__(self, partial, score_wanted, iteration, size):
        super().__init__(partial, score_wanted, iteration, size)

    def optimize(self, df=None, params=None, initial_params=None, env=None, fn=None, variables=[]):
        if params is None:
            params = {'nb_cross': 3, 'nb_new': 2, 'p_mutation': 0.5}
        population = []
        iteration = 0
        # initialize population
        for _ in range(self.size):
            s = self.partial.get_some(self.partial)
            population.append({
                'solution': s,
                'score': s.eval(df, variables, fn, initial_params, env)
            })
        # ---WHILE---
        performances = []
        while iteration < self.iteration:
            iteration += 1
            print('Iteration ', iteration)
            # Choose_candidates
            children = []
            for _ in range(params['nb_cross']):
                c1, c2 = self.__candidates(len(population))
                # Crossover
                child1, child2 = self.crossover(population[c1], population[c2])
                if child1 is not None:
                    children.append({'solution': child1, 'score': child1.eval(df, variables, fn, initial_params, env)})
                if child2 is not None:
                    children.append({'solution': child2, 'score': child2.eval(df, variables, fn, initial_params, env)})
            population = population + children
            for _ in range(params['nb_new']):
                s = self.partial.get_some(self.partial)
                population.append({
                    'solution': s,
                    'score': s.eval(df, variables, fn, initial_params, env)
                })
            # Update population
            population = sorted(population, key=lambda x: x["score"], reverse=False)[:self.size]
            print('\tMin:', population[0]['score'])
            print('\tMax:', population[-1]['score'])
            performances.append({'it': iteration, 'min': population[0]['score'], 'max': population[-1]['score']})
            # ---END WHILE---
        return population[0], performances

    def __candidates(self, size):
        c1 = random.randint(0, size - 1)
        c2 = random.randint(0, size - 1)
        while c1 == c2:
            c2 = random.randint(0, size - 1)
        return c1, c2

    def crossover(self, p1, p2):
        graph1 = p1['solution'].get_graph()
        graph2 = p2['solution'].get_graph()
        point_1, point_2 = self.__choice_crossing_point(graph1, graph2)
        point_1 = list(graph1.nodes())[point_1]
        point_2 = list(graph2.nodes())[point_2]
        child1 = self.__crossing(p1, point_1, p2, point_2)
        child2 = self.__crossing(p2, point_2, p1, point_1)
        return child1, child2

    def __crossing(self, p1, point_1, p2, point_2):
        graph1 = p1['solution'].get_graph()
        graph2 = p2['solution'].get_graph()
        replacement = self.__get_replacement_tree(graph2, point_2)
        graph = self.__replace_node(graph1, point_1, replacement)
        if not self.__is_lethal(graph):
            solution = Solution()
            solution.init_from_graph(graph)
            return solution
        else:
            return None

    def __get_replacement_tree(self, G, start_node):
        graph = G.copy()
        subtree = nx.DiGraph()
        visited = []

        def dfs(node, visited):
            node_data = graph.nodes()[node]
            subtree.add_node('*' + node, data=node_data['data'], type=node_data['type'], partial=node_data['partial'])
            ngb_list = list(graph.neighbors(node))
            c1 = not (node == list(graph.nodes())[-1])
            c2 = (len(ngb_list) == 1 and graph.nodes()[ngb_list[0]]['type'] == 'param')
            if c1 or c2:
                visited.append(node)
                for neighbor in graph.successors(node):
                    if neighbor not in visited:
                        neighbor_node = graph.nodes()[neighbor]
                        current_node = graph.nodes()[node]
                        subtree.add_node('*' + node, data=current_node['data'], type=current_node['type'],
                                         partial=current_node['partial'])
                        subtree.add_node('*' + neighbor, data=neighbor_node['data'], type=neighbor_node['type'],
                                         partial=neighbor_node['partial'])
                        subtree.add_edge('*' + node, '*' + neighbor)
                        dfs(neighbor, visited)

        dfs(start_node, visited)
        return subtree

    def __plot(self, G, name='Df', show=False):
        def hierarchy_pos(G, root, width=1.0, vert_gap=0.2, vert_loc=0, xcenter=0.5):
            pos = {}
            pos[root] = (xcenter, vert_loc)
            neighbors = list(G.neighbors(root))
            if len(neighbors) != 0:
                sub_width = width / len(neighbors)
                for neighbor in neighbors:
                    pos.update(
                        hierarchy_pos(G, neighbor, sub_width, vert_gap, vert_loc - vert_gap, xcenter))
                    xcenter += sub_width
            return pos

        pos = hierarchy_pos(G, list(G.nodes)[0])
        plt.figure(figsize=(16, 10))
        nx.draw(G, pos, with_labels=True, node_color='lightblue', node_size=500, font_size=10)
        plt.savefig('Plots/1_' + name + '.png', dpi=300)
        if show:
            plt.show()
        plt.clf()

    def __replace_node(self, G, node_to_replace, replacement):
        new_G = G.copy()
        replacement_copy = replacement.copy()
        if node_to_replace not in new_G:
            raise ValueError(f"Le nœud {node_to_replace} n'existe pas dans le graphe")
        predecessors = list(new_G.predecessors(node_to_replace))
        is_terminal = list(new_G.successors(node_to_replace)) == []
        if is_terminal:
            node_name = list(replacement_copy.nodes)[0]
            i = 0
            while node_name in list(new_G.nodes) and node_name != node_to_replace:
                node_name = list(replacement_copy.nodes)[0] + '_' + str(i)
                i += 1
            new_G.remove_node(node_to_replace)
            node = replacement_copy.nodes[list(replacement_copy.nodes)[0]]
            new_G.add_node(node_name, data=node['data'], type=node['type'], partial=node['partial'])
            for predecessor in predecessors:
                new_G.add_edge(predecessor, node_name)
        else:
            if not isinstance(replacement_copy, nx.DiGraph):
                raise TypeError("Pour un nœud non-terminal, le remplacement doit être un DiGraph")
            root_nodes = [n for n in replacement_copy.nodes() if replacement_copy.in_degree(n) == 0]
            if len(root_nodes) != 1:
                raise ValueError("Le sous-graphe de remplacement doit avoir exactement une racine")
            root_node = root_nodes[0]
            subtree_nodes = set(nx.descendants(new_G, node_to_replace))
            subtree_nodes.add(node_to_replace)
            remaining_nodes = set(new_G.nodes()) - subtree_nodes
            node_mapping = {}
            for repl_node in replacement_copy.nodes():
                node_name = repl_node
                if node_name in remaining_nodes:
                    i = 0
                    while node_name in remaining_nodes:  # or node_name in not_map:
                        node_name = repl_node + '_' + str(i)
                        i += 1
                    node_mapping[repl_node] = node_name
                    remaining_nodes.add(node_name)

            replacement_copy = nx.relabel_nodes(replacement_copy, node_mapping)
            if root_node in node_mapping:
                root_node = node_mapping[root_node]
            new_G.remove_nodes_from(subtree_nodes)
            new_G = nx.compose(new_G, replacement_copy)
            for predecessor in predecessors:
                if predecessor in new_G:
                    new_G.add_edge(predecessor, root_node)
                else:
                    raise ValueError("Noeud inexistant dans Genetic")
        return new_G

    def __re_choice_node(self, graph, pos):
        n = list(graph.nodes)[pos]
        node = graph.nodes[n]
        c1 = (node['type'] not in ['perception'])
        c2 = ('perception_need' not in n)
        c3 = ('kill' not in n)
        r = True
        if c1 and c2 and c3:
            r = False
        return r

    def __choice_crossing_point(self, graph1, graph2):
        nodes = list(graph1.nodes(data=True))
        point1 = random.randint(1, len(nodes) - 1)
        while self.__re_choice_node(graph1, point1):
            point1 = random.randint(1, len(nodes) - 1)
        nodes_ = list(graph2.nodes(data=True))
        point2 = random.randint(1, len(nodes_) - 1)
        cnt = 0
        while nodes_[point2][1]['type'] != nodes[point1][1]['type'] or self.__re_choice_node(graph2, point2):
            point2 = random.randint(1, len(nodes_) - 1)
            cnt += 1
        return point1, point2

    def __is_lethal(self, new_G):
        pb = False
        for n in new_G.nodes:
            if new_G.nodes[n]['type'] == 'action':
                sucessors = new_G.successors(n)
                if len(list(sucessors)) != len(new_G.nodes[n]['data'].get_attributes().keys()):
                    pb = True
                if not pb:
                    for s in sucessors:
                        if new_G.nodes[s]['type'] != 'param':
                            pb = True
                            break
                if pb:
                    break
        return pb
