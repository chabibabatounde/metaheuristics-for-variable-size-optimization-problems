from System.Evaluation.Model1 import Model1


class Simulator:
    solution = None
    model = None
    env = None

    def __init__(self, solution, env=None):
        self.model = None
        self.solution = solution
        self.env = env
        self.model = self.__create_model(solution, env)

    def run(self, time):
        for _ in range(time):
            self.model.step()
        data = {
            'model_data': self.model.datacollector.get_model_vars_dataframe(),
            'agent_data': self.model.datacollector.get_agent_vars_dataframe(),
        }
        return data

    def __create_model(self, solution, env):
        model = Model1(solution, env)
        return model
