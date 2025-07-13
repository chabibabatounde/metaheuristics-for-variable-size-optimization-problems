from System.Core.Actions.Action import Action
from System.Core.Actions.Primitives import *
import random
import copy


class GoAndEat(Action):

    def __init__(self, duration_cycle=1, gain=None, move_coast=None, kill=None):
        self.name = "GoAndEat"
        self.gain = gain
        self.kill = kill
        self.move_coast = move_coast
        self.perception_need = True
        self.__default_init()
        Action.__init__(self, duration_cycle)

    def __default_init(self):
        if self.gain is None:
            self.gain = random.randint(0, 100)
        if self.kill is None:
            self.kill = False
        if self.move_coast is None:
            self.move_coast = random.randint(0, 100)

    def process(self, agent, perception_result):
        agent.energy -= self.move_coast
        agent.energy += self.gain
        target = perception_result[0]
        move_agent_to(agent, target.pos)
        if self.kill:
            die(target)

    def start_action(self, agent):
        agent.eating = True

    def stop_action(self, agent):
        agent.eating = False
