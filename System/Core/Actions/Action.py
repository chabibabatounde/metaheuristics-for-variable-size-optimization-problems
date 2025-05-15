import copy


class Action:

    def __init__(self, duration_cycle):
        self.duration_cycle = duration_cycle

    def __start_action(self, agent):
        agent.active = False
        self.start_action(agent)

    def __end_action(self, agent):
        agent.action_time_count = 0
        agent.current_actions = []
        agent.current_priority = 0
        agent.active = True
        self.end_action(agent)

    def start_action(self, *params):
        pass

    def end_action(self, *params):
        pass

    def execute(self, agent, perception_result):
        if agent.alive:
            if agent.action_time_count == 0:
                self.__start_action(agent)
                self.process(agent, perception_result)
            agent.action_time_count += 1
            if agent.action_time_count == self.duration_cycle:
                self.__end_action(agent)

    def get_attributes(self):
        params = self.__dict__
        keys_list = ['name']
        for p in keys_list:
            if p in params:
                del params[p]
        return params

    def process(self, agent, perception_result):
        exit('Please define process method Process for ' + self.name)

    def init_params(self, params):
        i = 0
        if len(self.get_attributes()) != len(params):
            print(self.get_attributes(), '\n', params)
        for p in self.get_attributes():
            self.__setattr__(p, params[i])
            i += 1

    def sample(self):
        return copy.deepcopy(self)
