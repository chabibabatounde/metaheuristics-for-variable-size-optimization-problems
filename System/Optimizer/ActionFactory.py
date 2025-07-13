import copy

from System.Optimizer.PartialAction import PartialAction


class ActionFactory:

    def get_action(self, element):
        if isinstance(element, PartialAction):
            return element.get_some()
        else:
            return copy.deepcopy(element)
