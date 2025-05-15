from System.Core.AnimetaModel import AnimetaModel
from System.Core.Agent import Agent


class Simulator:
    solution = None
    model = None
    env = None
    __simulation_data = None

    def __init__(self, solution, initial_params=None, env=None):
        self.model = None
        self.solution = solution
        self.env = env
        self.__simulation_data = None
        self.initial_params = initial_params
        self.model = self.__create_model(solution, initial_params, env)

    def read_data(self, variable, value=1, data='agent_data'):
        data = self.__simulation_data[data].xs(value, level=variable)
        return data

    def run(self, time):
        for _ in range(time):
            self.model.step()
        data = {
            'model_data': self.model.datacollector.get_model_vars_dataframe(),
            'agent_data': self.model.datacollector.get_agent_vars_dataframe(),
        }
        self.__simulation_data = data
        return data

    def __create_model(self, solution, initial_params, env):
        model = AnimetaModel()
        if not isinstance(solution, dict):
            solution = solution.get_dict()
        n = len(initial_params)
        if n == 0:
            print('\nDefine if number of agent is not')
            exit(self)
        for _ in range(n):
            agent = Agent(
                model=model,
                agent_type=solution['type'],
                initial_params=initial_params[_]
            )
            for perception in solution['perceptions']:
                agent.add_perception(perception)
        model.setup(env)
        return model
