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
