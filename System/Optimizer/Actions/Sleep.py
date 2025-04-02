import random
from System.Optimizer.Actions.Action import Action


class Sleep(Action):
    def __init__(self, duration_cycle=1, gain=0):
        self.name = "Sleep"
        self.gain = gain
        self.perception_need = False
        Action.__init__(self, duration_cycle)
        # print("\t ", "Action \""+self.name+"\" Created", "ID =", id(self))

    def execute(self, agent, perception_result):
        agent.energy += self.gain

    def init(self, agent):
        agent.sleep()

    def finish(self, agent):
        agent.wake_up()


