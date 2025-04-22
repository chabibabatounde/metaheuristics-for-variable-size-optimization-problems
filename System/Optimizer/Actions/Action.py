class Action:

    def surcharge(self, param, value):
        self.__setattr__(param, value)

    def __init__(self, duration_cycle):
        self.duration_cycle = 0

    def execute(self, agent, perception_result):
        pass

    def get_attributes(self):
        params = self.__dict__
        keys_list = ['name']
        for p in keys_list:
            if p in params:
                del params[p]
        return params

    def init_params(self, params):
        i = 0
        if len(self.get_attributes()) != len(params):
            print(self.get_attributes(), '\n', params)
        for p in self.get_attributes():
            self.__setattr__(p, params[i])
            i += 1
