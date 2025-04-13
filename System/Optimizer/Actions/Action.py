class Action:

    def surcharge(self, param, value):
        self.__setattr__(param, value)

    def __init__(self, duration_cycle):
        self.duration_cycle = 0

    def execute(self, agent, perception_result):
        pass
