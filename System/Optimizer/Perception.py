class Perception:
    __condition = None
    name = ''
    radius = 0

    def __init__(self, name, condition, perception_type='bool', radius=2):
        self.radius = radius
        self.perception_type = perception_type
        self.name = name
        self.__condition = condition.replace('€.timer', 'agent.model.timer')
        self.__condition = self.__condition.replace('π.@', 'ng')
        self.__condition = self.__condition.replace('@', 'agent')

    def get_neighbors(self, agent):
        return agent.model.grid.get_neighbors(agent.pos, moore=True, radius=self.radius)

    def strengh(self, agent, items):
        if items is None:
            return 10
        else:
            return len(items) + agent.energy

    def __trigger(self, agent):
        res = False
        items = []
        if self.perception_type == 'bool':  # Boolean condition. True/False as response
            res = eval(self.__condition)
            items = None
        else:  # it will get items that satisfy the condition
            for ng in self.get_neighbors(agent):
                if eval(self.__condition):
                    items.append(ng)
                    res = True
        return res, items

    def percept(self, agent):
        return self.__trigger(agent)
