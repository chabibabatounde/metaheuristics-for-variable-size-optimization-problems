import mesa
from System.Evaluation.Agent import Agent


class Model1(mesa.Model):
    nb_agent = 0
    timer = 0

    def __init__(self, solution, env, n=1, seed=None):
        super().__init__(seed=seed)
        self.nb_agent = n
        agent_id = 0
        self.timer = 0
        self.schedule = mesa.time.BaseScheduler(self)
        if env.single_in_grid:
            self.grid = mesa.space.SingleGrid(width=env.width, height=env.height, torus=env.is_toroidal)
        else:
            self.grid = mesa.space.MultiGrid(width=env.width, height=env.height, torus=env.is_toroidal)

        def get_timer(model):
            return model.timer

        self.datacollector = mesa.DataCollector(
            model_reporters={"time": get_timer},
            agent_reporters={"energy": "energy", 'position': 'pos'}
        )

        for i in range(self.nb_agent):
            agent_id
            agent = Agent(self, agent_id, solution)
            self.schedule.add(agent)
            x = self.random.randrange(self.grid.width)
            y = self.random.randrange(self.grid.height)
            self.grid.place_agent(agent, (x, y))
            agent_id += 1

        for e in env.environment_set:
            print(e)
            exit(self)

    def step(self):
        self.datacollector.collect(self)
        self.schedule.step()
        self.timer += 1

