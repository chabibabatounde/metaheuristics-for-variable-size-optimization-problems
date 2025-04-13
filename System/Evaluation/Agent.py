import mesa


class Agent(mesa.Agent):
    __perceptions = []
    __perception_match_table = {}
    name = ''
    energy = 0

    def __init__(self, model, unique_id, solution):
        self.__perceptions = []
        self.__perception_match_table = {}
        self.energy = 0
        self.name = 'Agent N° ' + str(unique_id)
        super().__init__(model=model, unique_id=unique_id)
        self.wealth = 1
        solution_dict = solution.get_dict()
        for perception in solution_dict['perceptions']:
            self.__perceptions.append(perception['perception'])
            self.__perception_match_table[perception['perception'].name] = perception['actions']

    def step(self):
        # Percept
        perceptions = []
        for p in self.__perceptions:
            res, items = p.percept(self)
            if res:
                perceptions.append({
                    'perception': p,
                    'item': items,
                    'strength': p.strengh(self, items)
                })

        # Deliberate
        actions = []
        params = []
        if len(perceptions) != 0:
            perceptions = sorted(perceptions, key=lambda x: x["strength"], reverse=True)
            p = perceptions[0]
            actions = self.__perception_match_table[p['perception'].name]
            params = p['item']
        else:
            pass

        # Execute
        for action in actions:
            action.execute(self, items)
