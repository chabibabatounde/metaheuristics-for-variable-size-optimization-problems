import random
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
            # Choose_candidates
            for _ in range(params['nb_cross']):
                c1, c2 = self.__candidates(len(population))
                # Crossover
                child1, child2 = self.crossover(population[c1], population[c2])
                if child1 is not None:
                    population.append({'solution': child1, 'score': child1.eval(df)})
                if child1 is not None:
                    population.append({'solution': child2, 'score': child2.eval(df)})
            for _ in range(params['nb_new']):
                s = self.partial.get_some(self.partial)
                population.append({
                    'solution': s,
                    'score': s.eval(df)
                })
            # Update population
            population = sorted(population, key=lambda x: x["score"], reverse=False)[:self.size]
            # ---END WHILE---
        return random.uniform(0, 100)

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
        while nodes_[point2][1]['type'] != nodes[point1][1]['type']:
            point2 = random.randint(1, len(nodes_) - 1)
        return point1, point2

    def __get_left_subtree(self, G, start_node, end_node):
        graph = G.copy()
        subtree = nx.Graph()
        visited = []

        def dfs(node, visited):
            if node != end_node:
                visited.append(node)
                for neighbor in graph.neighbors(node):
                    if graph.nodes()[neighbor]['node_id'] < graph.nodes()[end_node]['node_id']:
                        if neighbor not in visited:
                            neighbor_node = graph.nodes()[neighbor]
                            current_node = graph.nodes()[node]
                            subtree.add_node('L#' + node, data=current_node['data'], type=current_node['type'],
                                             partial=current_node['partial'], node_id=current_node['node_id'],
                                             level=current_node['level'])
                            subtree.add_node('L#' + neighbor, data=neighbor_node['data'], type=neighbor_node['type'],
                                             partial=neighbor_node['partial'], node_id=neighbor_node['node_id'],
                                             level=neighbor_node['level'])
                            subtree.add_edge('L#' + node, 'L#' + neighbor)
                            dfs(neighbor, visited)

        dfs(start_node, visited)
        return subtree

    def __get_center_subtree(self, G, start_node):
        graph = G.copy()
        subtree = nx.Graph()
        visited = []

        def dfs(node, visited):
            node_data = graph.nodes()[node]
            subtree.add_node('C#' + node, data=node_data['data'], type=node_data['type'], partial=node_data['partial'],
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
                            subtree.add_node('C#' + node, data=current_node['data'], type=current_node['type'],
                                             partial=current_node['partial'], node_id=current_node['node_id'],
                                             level=current_node['level'])
                            subtree.add_node('C#' + neighbor, data=neighbor_node['data'], type=neighbor_node['type'],
                                             partial=neighbor_node['partial'], node_id=neighbor_node['node_id'],
                                             level=neighbor_node['level'])
                            subtree.add_edge('C#' + node, 'C#' + neighbor)
                            dfs(neighbor, visited)

        dfs(start_node, visited)
        return subtree

    def __get_right_subtree(self, G, cut_point):
        graph = G.copy()
        node = None
        pos = 0
        for n in graph.nodes():
            if cut_point == n:
                node = graph.nodes[n]
                break
            pos += 1
        next_point = None
        if node == list(graph.nodes)[-1]:
            next_point = None
        else:
            for n in list(graph.nodes)[pos + 1:]:
                if graph.nodes[n]['level'] <= graph.nodes[cut_point]['level']:
                    next_point = n
                    break
        if next_point is not None:
            nodes_list = list(graph.nodes)
            for n in nodes_list:
                if n == next_point:
                    break
                graph.remove_node(n)
            return graph
        else:
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

    def __crossing(self, p1, point_1, p2, point_2):
        graph1 = p1['solution'].get_graph()
        graph2 = p2['solution'].get_graph()
        left_subtree = self.__get_left_subtree(graph1, 'ROOT', point_1)
        center_subtree = self.__get_center_subtree(graph2, point_2)
        right_subtree = self.__get_right_subtree(graph1, point_1)
        graph = self.__patch_parts(left_subtree, center_subtree, right_subtree)
        if self.__is_not_lethal(graph):
            g = Solution.init_from_graph(graph)
            return g
        else:
            return None

    def __get_parent(self, graph, level):
        left_list = list(graph.nodes)
        left_list.reverse()
        for n in left_list:
            if graph.nodes[n]['level'] < level:
                return n

    def __patch_parts(self, left, center, right):
        center_node_index = list(center.nodes)[0]
        left_list = list(left.nodes)
        left_list.reverse()
        level = 3
        patch_node = 0
        if len(center[center_node_index]) != 0:
            level = center.nodes()[center_node_index]['level']
        for n in left_list:
            if left.nodes()[n]['level'] < level:
                patch_node = n
                break
        left.add_edge(patch_node, center_node_index)
        left.add_nodes_from(center.nodes(data=True))
        left.add_edges_from(center.edges(data=True))
        if right is not None:
            for n in right.nodes:
                parent = self.__get_parent(left, right.nodes[n]['level'])
                l_node = left.nodes[parent]
                r_node = right.nodes[n]
                left.add_node(parent, data=l_node['data'], type=l_node['type'], partial=l_node['partial'],
                              node_id=l_node['node_id'], level=l_node['level'])
                left.add_node(n, data=r_node['data'], type=r_node['type'], partial=r_node['partial'],
                              node_id=r_node['node_id'], level=r_node['level'])
                left.add_edge(parent, n)
        return self.__udate_child(left)

    def __udate_child(self, g):
        graph = g.copy()
        depths = nx.single_source_shortest_path_length(graph, 'L#ROOT')
        id = 0
        for n in graph.nodes:
            graph.nodes[n]['level'] = depths[n]
            graph.nodes[n]['node_id'] = id
            id += 1
        return graph
