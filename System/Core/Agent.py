import mesa
from System.Optimizer.Perception import Perception
from System.Core.Actions.RandomMove import RandomMove
from System.Core.Actions.Void import Void
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
    action_time_count = 0

    def get_actions(self):
        return self.__perception_match_table

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
        self.current_priority = 0
        self.action_time_count = 0
        self.current_actions = []
        if initial_params is not None:
            self.__initial_params(initial_params)


        '''
        self.add_perception(
            {
                'perception': Perception('default', condition="$.type=='" + agent_type + "'"),
                'actions': [
                    RandomMove(duration_cycle=1, max_velocity=(1, 1), move_probability=0.5)
                ]
            }
        )
        '''

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
        if not self.active:
            for action in self.current_actions:
                action.execute(self, [])
            return

        max_perception = None
        max_strength = self.current_priority
        max_items = None
        perceptions_data = [(p, *p.percept(self)) for p in self.__perceptions]
        valid_perceptions = [(p, items, p.strengh(self, items))
                             for p, res, items in perceptions_data if res]

        for perception, items, strength in valid_perceptions:
            if strength > max_strength:
                max_strength = strength
                max_perception = perception
                max_items = items

        if max_perception and max_strength > self.current_priority:
            self.current_priority = max_strength
            self.current_actions = self.__perception_match_table[max_perception.name]
            self.action_time_count = 0
            params = max_items
        else:
            params = max_items if max_items is not None else []

        for action in self.current_actions:
            action.execute(self, params)
