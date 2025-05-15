import mesa
from System.Core.Agent import Agent


class AnimetaModel(mesa.Model):
    nb_agent = 0
    timer = 0
    __agent_id = 0
    __unique_id = 0

    def __init__(self, n=1, init_params=[], seed=None):
        super().__init__(seed=seed)
        self.__agent_id = 0
        self.timer = 0
        self.nb_agent = n
        self.init_params = init_params
        self.schedule = mesa.time.BaseScheduler(self)

        def get_timer(model):
            return model.timer

        self.datacollector = mesa.DataCollector(
            model_reporters={"time": get_timer},
            agent_reporters={"energy": "energy", "type": "type", 'position': 'pos'}
        )

    def get_unique_id(self):
        self.__unique_id += 1
        return self.__unique_id

    def setup(self, env=None):
        if env.single_in_grid:
            self.grid = mesa.space.SingleGrid(width=env.width, height=env.height, torus=env.is_toroidal)
        else:
            self.grid = mesa.space.MultiGrid(width=env.width, height=env.height, torus=env.is_toroidal)
        for element in env.environment_set:
            for _ in range(element['nb']):
                ag = element['agent']
                agent = Agent(model=self, agent_type=ag.type, initial_params=element['initial_params'][_])
                match_table = ag.perception_match_table()
                for perception in ag.perceptions():
                    agent.add_perception({
                        'perception': perception,
                        'actions': match_table[perception.name]
                    })
        for agent in list(self.agents):
            self.__init_agent(agent)

    def __init_agent(self, agent):
        if agent.position is None:
            x = self.random.randrange(self.grid.width)
            y = self.random.randrange(self.grid.height)
        else:
            x = agent.position[0]
            y = agent.position[1]
        self.schedule.add(agent)
        self.grid.place_agent(agent, (x, y))

    def step(self):
        self.datacollector.collect(self)
        self.schedule.step()
        self.timer += 1

