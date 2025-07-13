from System.Core.Actions.Action import Action
from System.Core.Actions.Primitives import *
import random
import copy


class Void(Action):

    def __init__(self, duration_cycle=1):
        self.name = "Void"
        self.perception_need = False
        Action.__init__(self, duration_cycle)

    def process(self, agent, perception_result):
        pass
