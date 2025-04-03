from System.Evaluation.Model1 import Model1
from System.Evaluation.Agent import Agent


class Simulator:
    df = None
    solution = None
    model = None

    def __init__(self, solution, df):
        self.df = df
        self.solution = solution
        self.model = Model1(solution)

    def run(self, time):
        for _ in range(time):
            self.model.step()
        data = {
            'model_data': self.model.datacollector.get_model_vars_dataframe(),
            'agent_data': self.model.datacollector.get_agent_vars_dataframe(),
        }
        return data
