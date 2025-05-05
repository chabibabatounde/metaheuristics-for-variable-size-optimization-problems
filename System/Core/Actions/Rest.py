from System.Core.Actions.Action import Action


class Rest(Action):
    def __init__(self, duration_cycle=1):
        self.name = "Rest"
        Action.__init__(self, duration_cycle)
        self.perception_need = False

    def executes(self, agent, perception_desire):
        pass
