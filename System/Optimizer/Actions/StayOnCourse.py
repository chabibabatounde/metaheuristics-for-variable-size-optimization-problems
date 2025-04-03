from System.Optimizer.Actions.Action import Action
import random
import copy


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

    def get_some_instance(self):
        element = copy.deepcopy(self)
        element.acceleration = (random.randint(0, 0), random.randint(0, 0))
        element.duration_cycle = 1
        # element.duration_cycle = random.randint(1, 100)
        return element
