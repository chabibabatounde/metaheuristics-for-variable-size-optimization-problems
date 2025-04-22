import random

from matplotlib import pyplot as plt

from System.Algorithms.Algorithm import Algorithm
from System.Representation.Solution import Solution
import networkx as nx


class Genetic(Algorithm):

    def __init__(self, partial, score_wanted, iteration, size):
        super().__init__(partial, score_wanted, iteration, size)

    def __candidates(self, len):
        c1 = random.randint(0, len - 1)
        c2 = random.randint(0, len - 1)
        while c1 == c2:
            c2 = random.randint(0, len - 1)
        return c1, c2

    def optimize(self, df, params=None):
        if params is None:
            params = {'nb_cross': 3, 'nb_new': 2, 'p_mutation': 0.5}
        population = []
        iteration = 0
        # initialize population
        for _ in range(self.size):
            s = self.partial.get_some(self.partial)
            population.append({
                'solution': s,
                'score': s.eval(df)
            })
        # ---WHILE---
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
                    children.append({'solution': child1, 'score': child1.eval(df)})
                if child2 is not None:
                    children.append({'solution': child2, 'score': child2.eval(df)})
            # population = population + children
            population = children
            for _ in range(params['nb_new']):
                s = self.partial.get_some(self.partial)
                population.append({
                    'solution': s,
                    'score': s.eval(df)
                })
            # Update population
            population = sorted(population, key=lambda x: x["score"], reverse=False)[:self.size]
            print('\tMin:', population[0]['score'])
            print('\tMax:', population[-1]['score'])
            # ---END WHILE---
        exit('Fin de processus @GENETIC')
        return random.uniform(0, 100)

    def __patch_parts(self, left, center, right):
        last_node = list(left.nodes)[-1]
        ng = list(left.neighbors(last_node))[0]
        left.add_nodes_from(center.nodes(data=True))
        left.add_edges_from(center.edges(data=True))
        left.add_edge(ng, list(center.nodes)[0])
        left.remove_node(last_node)
        left = self.__update_child(left)
        if right is not None:
            nx.draw(left, with_labels=True)
            plt.savefig('img/Left.png')
            plt.clf()

            nx.draw(right, with_labels=True)
            plt.savefig('img/Right.png')
            plt.clf()

            tops = []
            nodes = []
            for g in list(nx.connected_components(right)):
                nodes.append(right.subgraph(g))
                top_node = None
                top_level = 1000000
                for k in g:
                    if right.nodes[k]['level'] < top_level:
                        top_node = k
                        top_level = right.nodes[k]['level']
                tops.append({'level': top_level, 'node': top_node})
            seq = 0
            print(left.nodes, right.nodes)
            for point in tops:
                left_nodes = list(left.nodes)
                left_nodes.reverse()
                for n in left_nodes:
                    if left.nodes[n]['level'] < point['level']:
                        nodes_list = []
                        for _n_ in nodes[seq].nodes:
                            nodes_list.append({'level': nodes[seq].nodes[_n_]['level'], 'key': _n_})
                        nodes_list = sorted(nodes_list, key=lambda x: x["level"], reverse=False)

                        for k in nodes_list:
                            _node = right.nodes[k['key']]
                            left.add_node(k['key'], data=_node['data'], type=_node['type'], partial=_node['partial'],
                                          node_id=_node['node_id'], level=_node['level'])
                        for _ in nodes[seq].nodes:
                            left.add_edges_from(nodes[seq].edges(data=True))
                            left.add_edge(n, point['node'])
                            print('\t\t', n, '->', point['node'])
                            # print(left.nodes)
                            break
                seq += 1
        print('--------------------------')
        exit()
        return self.__update_child(left)

    def __is_not_lethal(self, graph):
        return True

    def __re_choice_node(self, node):
        r = True
        value = node[0]
        data = node[1]
        c1 = (data['type'] not in ['perception'])
        c2 = ('perception_need' not in value)
        c3 = ('kill' not in value)
        if c1 and c2 and c3:
            r = False
        return r

    def __choice_crossing_point(self, graph1, graph2):
        nodes = list(graph1.nodes(data=True))
        point1 = random.randint(1, len(nodes) - 1)
        while self.__re_choice_node(nodes[point1]):
            point1 = random.randint(1, len(nodes) - 1)
        nodes_ = list(graph2.nodes(data=True))
        point2 = random.randint(1, len(nodes_) - 1)
        while nodes_[point2][1]['type'] != nodes[point1][1]['type'] or self.__re_choice_node(nodes_[point2]):
            point2 = random.randint(1, len(nodes_) - 1)
        point1, point2 = 4, 9
        return point1, point2

    def __get_left_subtree(self, G, start_node, end_node):
        graph = G.copy()
        subtree = nx.Graph()
        subtree = self.__dfs(start_node, subtree, graph, end_node)
        return subtree

    def __get_center_subtree(self, G, start_node):
        graph = G.copy()
        subtree = nx.Graph()
        visited = []

        def dfs(node, visited):
            node_data = graph.nodes()[node]
            subtree.add_node('*' + node, data=node_data['data'], type=node_data['type'], partial=node_data['partial'],
                             node_id=node_data['node_id'], level=node_data['level'])
            # Si fin ou noeud de niveau inférieur
            if not (node == list(graph.nodes())[-1]) or (
                    len(list(graph.neighbors(node))) == 1 and graph.nodes()[list(graph.neighbors(node))[0]][
                'type'] == 'param'):
                visited.append(node)
                for neighbor in graph.neighbors(node):
                    if graph.nodes()[neighbor]['level'] > graph.nodes()[node]['level']:
                        if neighbor not in visited:
                            neighbor_node = graph.nodes()[neighbor]
                            current_node = graph.nodes()[node]
                            subtree.add_node('*' + node, data=current_node['data'], type=current_node['type'],
                                             partial=current_node['partial'], node_id=current_node['node_id'],
                                             level=current_node['level'])
                            subtree.add_node('*' + neighbor, data=neighbor_node['data'], type=neighbor_node['type'],
                                             partial=neighbor_node['partial'], node_id=neighbor_node['node_id'],
                                             level=neighbor_node['level'])
                            subtree.add_edge('*' + node, '*' + neighbor)
                            dfs(neighbor, visited)

        dfs(start_node, visited)
        return subtree

    def __get_right_subtree(self, G, cut_point):
        graph = G.copy()
        if cut_point != list(graph.nodes)[-1]:
            next_point = None
            index_start = list(graph.nodes).index(cut_point)
            for n in list(graph.nodes)[index_start + 1:]:
                if graph.nodes[n]['level'] <= graph.nodes[cut_point]['level']:
                    next_point = n
                    break
            nodes_list = list(graph.nodes)
            for n in nodes_list:
                if n == next_point:
                    break
                graph.remove_node(n)
            return graph
        return None

    def crossover(self, p1, p2):
        graph1 = p1['solution'].get_graph()
        graph2 = p2['solution'].get_graph()
        point_1, point_2 = self.__choice_crossing_point(graph1, graph2)
        point_1 = list(graph1.nodes())[point_1]
        point_2 = list(graph2.nodes())[point_2]
        child1 = self.__crossing(p1, point_1, p2, point_2)
        child2 = self.__crossing(p2, point_2, p1, point_1)
        return child1, child2

    def control_graph(self, graph1, graph2, point_1, point_2, left, center, right, graph):
        for g in graph.nodes:
            if graph.nodes[g]['type'] == 'action':
                if len(graph.nodes[g]['data'].get_attributes()) != len(list(graph.neighbors(g))) - 1:
                    nx.draw(graph1, with_labels=True)
                    plt.savefig('img/p1.png')
                    plt.clf()

                    # print(graph1.nodes, '\n\t', point_1)

                    nx.draw(graph2, with_labels=True)
                    plt.savefig('img/p2.png')
                    plt.clf()

                    # print(graph2.nodes, '\n\t', point_2)

                    nx.draw(left, with_labels=True)
                    plt.savefig('img/left.png')
                    plt.clf()

                    nx.draw(center, with_labels=True)
                    plt.savefig('img/center.png')
                    plt.clf()

                    nx.draw(right, with_labels=True)
                    plt.savefig('img/right.png')
                    plt.clf()

                    nx.draw(graph, with_labels=True)
                    plt.savefig('img/child.png')
                    plt.clf()

                    exit(self)

    def __crossing(self, p1, point_1, p2, point_2):
        graph1 = p1['solution'].get_graph()
        graph2 = p2['solution'].get_graph()
        left_subtree = self.__get_left_subtree(graph1, list(graph1.nodes)[0], point_1)
        left = left_subtree.copy()
        center_subtree = self.__get_center_subtree(graph2, point_2)
        right_subtree = self.__get_right_subtree(graph1, point_1)
        graph = self.__patch_parts(left_subtree, center_subtree, right_subtree)
        self.control_graph(graph1, graph2, point_1, point_2, left, center_subtree, right_subtree, graph)
        if not self.__is_lethal(graph):
            solution = Solution()
            solution.init_from_graph(graph)
            return solution
        else:
            return None

    def __is_lethal(self, graph):
        return False

    def __get_parent(self, graph, level):
        left_list = list(graph.nodes)
        left_list.reverse()
        for n in left_list:
            if graph.nodes[n]['level'] < level:
                return n

    def __update_child(self, g):
        graph = g.copy()
        depths = nx.single_source_shortest_path_length(graph, list(graph.nodes)[0])
        id = 0
        for n in graph.nodes:
            graph.nodes[n]['level'] = depths[n]
            graph.nodes[n]['node_id'] = id
            id += 1
        return graph

    def __dfs(self, node, subtree, graph, end_node):
        if '#' + node not in list(graph.nodes):
            current_node = graph.nodes()[node]
            subtree.add_node(
                '#' + node, data=current_node['data'], type=current_node['type'],
                partial=current_node['partial'], node_id=current_node['node_id'],
                level=current_node['level']
            )
        for neighbor in graph.neighbors(node):
            if graph.nodes()[neighbor]['node_id'] <= graph.nodes()[end_node]['node_id']:
                if graph.nodes()[neighbor]['level'] > graph.nodes()[node]['level']:
                    neighbor_node = graph.nodes()[neighbor]
                    subtree.add_node(
                        '#' + neighbor, data=neighbor_node['data'], type=neighbor_node['type'],
                        partial=neighbor_node['partial'], node_id=neighbor_node['node_id'],
                        level=neighbor_node['level']
                    )
                    subtree.add_edge('#' + node, '#' + neighbor)
                    subtree = self.__dfs(neighbor, subtree, graph, end_node)
        return subtree
