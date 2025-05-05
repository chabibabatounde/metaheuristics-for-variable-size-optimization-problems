from System.Core.Actions.Action import Action
from System.Core.Actions.Primitives import *
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

    def execute(self, agent, perception_result):
        if agent.alive:
            if agent.active:
                agent.energy -= self.move_coast
                agent.energy += self.gain
                target = perception_result[0]
                move_agent_to(agent, target.pos)
                print(agent, self.name, '->', target)
                if self.kill:
                    die(target)

    def get_some_instance(self):
        element = copy.deepcopy(self)
        element.duration_cycle = random.randint(0, 10)
        element.gain = random.randint(0, 150)
        element.move_coast = random.uniform(0, 1)
        return element