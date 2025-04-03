from System.Optimizer.Actions.Action import Action
import random
import copy

class GetCloser(Action):

    def __init__(self, duration_cycle=1, max_attempt=10, target='closer'):
        self.name = "GetClose"
        self.target = target
        self.max_attempt = max_attempt
        self.perception_need = True
        Action.__init__(self, duration_cycle)

    def executes(self, agent, perception_result):
        position_found = False
        count = 0
        if self.target == 'closer':
            reference = perception_result.closer_agent.position
        elif self.target == 'maximum_agent':
            reference = perception_result.maximum_agent.position
        else:
            exit(self)

        gap = 1
        while not position_found and count < self.max_attempt:
            propositions = []
            for i in range(-1, 2):
                for j in range(-1, 2):
                    proposition = (reference[0] + (i * gap), reference[1] + (j * gap))
                    if proposition != reference and agent.grid.is_move_possible(proposition):
                        propositions.append(
                            {
                                'distance': agent.grid.distance(agent.position, proposition, is_agent=False),
                                'position': proposition
                            }
                        )
            propositions = sorted(propositions, key=lambda d: d['distance'])
            if len(propositions) == 0:
                gap += 1
            else:
                position_found = True
                place_agent(agent, propositions[0]['position'])
    def get_some_instance(self):
        element = copy.deepcopy(self)
        element.duration_cycle = 1
        return element