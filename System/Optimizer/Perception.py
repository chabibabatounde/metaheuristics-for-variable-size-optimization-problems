import math


class Perception:
    __condition = None
    name = ''
    radius = 0

    def get_conditions(self):
        return self.__condition

    def __init__(self, name, condition, radius=1, perception_type='bool', priority=1):
        self.priority = priority
        self.radius = radius
        self.perception_type = perception_type
        self.name = name
        self.__condition = condition.replace('€.timer', 'agent.model.timer')  # timer
        self.__condition = self.__condition.replace('π.@', 'ng')  # Other agent
        self.__condition = self.__condition.replace('$', 'agent')  # Self agent

    def get_neighbors(self, agent):
        return agent.model.grid.get_neighbors(pos=agent.pos, moore=True, include_center=False, radius=self.radius)

    def strengh(self, agent, items):
        if items is None:
            return self.priority
        else:
            return self.priority

    def __trigger(self, agent):
        res = False
        items = []
        neighbor_distances = []
        if self.perception_type == 'bool':  # Boolean condition. True/False as response
            res = eval(self.__condition)
            items = None
        else:  # it will get items that satisfy the condition
            for ng in self.get_neighbors(agent):
                if eval(self.__condition):
                    distance = self.__get_distance(agent, ng)
                    neighbor_distances.append((ng, distance))
            neighbor_distances.sort(key=lambda x: x[1])
            items = [neighbor for neighbor, _ in neighbor_distances]
            res = len(items) > 0
        return res, items

    def __get_distance(self, agent1, agent2):
        x1, y1 = agent1.pos
        x2, y2 = agent2.pos
        is_torus = hasattr(agent1.model.grid, 'torus') and agent1.model.grid.torus
        if not is_torus:
            return math.sqrt((x2 - x1) ** 2 + (y2 - y1) ** 2)
        else:
            grid_width = agent1.model.grid.width
            grid_height = agent1.model.grid.height
            dx = min(abs(x2 - x1), grid_width - abs(x2 - x1))
            dy = min(abs(y2 - y1), grid_height - abs(y2 - y1))
            return math.sqrt(dx ** 2 + dy ** 2)

    def percept(self, agent):
        return self.__trigger(agent)
