import mesa
from copy import deepcopy


class Agent(mesa.Agent):
    __perceptions = []
    __perception_match_table = {}
    name = ''
    type = ''
    energy = 0
    position = None
    active = False
    alive = False

    def __init__(self, agent_type, model=None, initial_params=None):
        if model is not None:
            unique_id = model.get_unique_id()
            super().__init__(model=model, unique_id=unique_id)
            self.name = 'Agent N° ' + str(unique_id)
        self.__perceptions = []
        self.__perception_match_table = {}
        self.energy = 0
        self.position = None
        self.active = True
        self.alive = True
        self.type = agent_type
        if initial_params is not None:
            self.__initial_params(initial_params)

    def __initial_params(self, params):
        for p in params:
            self.__setattr__(p, params[p])

    def initial_params(self, params):
        self.__initial_params(params)

    def add_perception(self, perception):
        perception = deepcopy(perception)
        self.__perceptions.append(perception['perception'])
        self.__perception_match_table[perception['perception'].name] = perception['actions']

    def perception_match_table(self):
        return self.__perception_match_table

    def perceptions(self):
        return self.__perceptions

    def step(self):
        # Percept
        perceptions = []
        for p in self.__perceptions:
            res, items = p.percept(self)
            if res:
                perceptions.append({
                    'perception': p,
                    'item': items,
                    'strength': p.strengh(self, items)
                })
        # Deliberate
        actions = []
        params = []
        if len(perceptions) != 0:
            perceptions = sorted(perceptions, key=lambda x: x["strength"], reverse=True)
            p = perceptions[0]
            actions = self.__perception_match_table[p['perception'].name]
            params = p['item']
        else:
            pass
        # Execute
        for action in actions:
            action.execute(self, params)
