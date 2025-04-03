from System.Optimizer.Actions.Action import Action
import random
import copy


class Eat(Action):

    def __init__(self, duration_cycle=1, gain=0, move_coast=0, kill=True):
        self.name = "Eat"
        self.gain = gain
        self.kill = kill
        self.move_coast = move_coast
        self.perception_need = True
        Action.__init__(self, duration_cycle)

    def executes(self, agent, perception_result):
        agent.energy -= perception_result.closer_agent_distance * self.move_coast
        agent.energy += self.gain
        if self.kill:
            die(perception_result.closer_agent)
            place_agent(agent, perception_result.closer_agent_position)

    def get_some_instance(self):
        element = copy.deepcopy(self)
        element.duration_cycle = random.randint(0, 10)
        element.gain = random.randint(0, 150)
        element.move_coast = random.uniform(0, 1)
        return element