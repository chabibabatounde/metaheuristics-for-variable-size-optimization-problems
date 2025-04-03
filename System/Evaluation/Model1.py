import mesa
from System.Evaluation.Agent import Agent


class Model1(mesa.Model):
    nb_agent = 0
    timer = 0
    """Un modèle avec un certain nombre d'agents."""

    def __init__(self, solution, n=10, seed=None):
        super().__init__(seed=seed)
        self.nb_agent = 0
        self.timer = 0
        self.schedule = mesa.time.BaseScheduler(self)
        self.grid = mesa.space.MultiGrid(width=10, height=10, torus=True)

        def get_timer(model):
            return model.timer

        self.datacollector = mesa.DataCollector(
            model_reporters={"time": get_timer},
            agent_reporters={"energy": "energy", 'position': 'pos'}
        )

        for i in range(self.nb_agent, self.nb_agent + n):
            agent = Agent(self, i, solution)
            self.schedule.add(agent)
            x = self.random.randrange(self.grid.width)
            y = self.random.randrange(self.grid.height)
            self.grid.place_agent(agent, (x, y))

    def step(self):
        self.datacollector.collect(self)
        self.schedule.step()
        self.timer += 1
