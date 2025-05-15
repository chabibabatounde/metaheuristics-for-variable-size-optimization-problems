from System.Core.Actions.Action import Action
import copy
from System.Core.Actions.Primitives import *


class GetClose(Action):

    def __init__(self, duration_cycle=1):
        self.name = "GetClose"
        self.perception_need = True
        Action.__init__(self, duration_cycle)

    def process(self, agent, perception_result):
        target = perception_result[0]
        move_agent_to(agent, target.pos)
