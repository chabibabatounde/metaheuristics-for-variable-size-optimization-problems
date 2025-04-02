from System.Optimizer.Actions.Action import Action
import random


class StayOnCourse(Action):
    acceleration = None

    def __init__(self, duration_cycle=0, acceleration=None):
        self.name = "StayOnCourse"
        self.acceleration = acceleration
        self.perception_need = True
        Action.__init__(self, duration_cycle)

    def executes(self, agent, perception_result):
        if self.acceleration is not None:
            move(agent, acceleration=self.acceleration)
        else:
            move(agent)
