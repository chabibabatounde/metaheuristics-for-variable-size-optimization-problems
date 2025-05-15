from System.Core.Actions.Action import Action
import random
import copy
from System.Core.Actions.Primitives import *


class RandomMove(Action):
    move_probability = None
    max_velocity = None
    max_attempt = None
    lost = None

    def __init__(self, duration_cycle=0, max_velocity=(2, 2), lost=0, move_probability=0.5, max_attempt=4):
        if move_probability < 0 or move_probability > 1:
            exit("The probability value must be between 0 and 1")
        Action.__init__(self, duration_cycle)
        self.name = "RandomMove"
        self.max_attempt = max_attempt
        self.max_velocity = max_velocity
        self.move_probability = move_probability
        self.lost = lost
        self.perception_need = False

    def process(self, agent, perception_result=None):
        if random.uniform(0, 1) > self.move_probability:
            random_move(agent, self.max_velocity)
