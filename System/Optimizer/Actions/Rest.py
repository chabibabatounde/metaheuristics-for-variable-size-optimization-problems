from System.Optimizer.Actions.Action import Action
import random
import copy

class Rest(Action):
    def __init__(self, duration_cycle=1):
        self.name = "Rest"
        Action.__init__(self, duration_cycle)
        self.perception_need = False

    def executes(self, agent, perception_desire):
        pass
