from System.Optimizer.Partial import Partial
from System.Optimizer.ActionFactory import ActionFactory


class Animeta(Partial):
    __perceptions = []
    __perception_match_table = {}
    __agent_type = None

    def __init__(self, agent_type):
        self.__agent_type = agent_type
        self.__perceptions = []
        self.__perception_match_table = {}

    def add_perception(self, perception, actions=[]):
        self.__perceptions.append(perception)
        for action in actions:
            if perception.name in self.__perception_match_table:
                self.__perception_match_table[perception.name].append(action)
            else:
                self.__perception_match_table[perception.name] = actions
                break

    def get_some(self):
        solution = {
            'type': self.__agent_type,
            'perceptions': []
        }
        action_factory = ActionFactory()
        for p in self.__perceptions:
            actions = []
            for action in self.__perception_match_table[p.name]:
                actions.append(action_factory.get_action(action))
            solution['perceptions'].append({
                'perception': p,
                'actions': actions
            })
        return solution

    def get_match_table(self):
        return self.__perception_match_table
