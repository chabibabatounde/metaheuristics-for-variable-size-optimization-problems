from System.Optimizer.PartialKnowledge import PartialKnowledge
from System.Optimizer.Actions.Eat import Eat


class PartialAction:
    name = None
    duration_cycle = None
    variables_partial_knowledge = []
    values = []

    def __init__(self, name, duration, *partial_knowledge):
        partial_knowledge = list(partial_knowledge)
        self.name = name
        self.duration = duration
        if duration is not None:
            self.variables_partial_knowledge.append(PartialKnowledge(name='duration_cycle', value=duration))
        self.variables_partial_knowledge = []
        self.values = []
        self.partial_knowledge(partial_knowledge)

    def partial_knowledge(self, partial_knowledges):
        if len(self.variables_partial_knowledge) == 0:
            self.variables_partial_knowledge = []
        for element in partial_knowledges:
            if element.value is not None:
                self.values.append(element)
            else:
                self.variables_partial_knowledge.append(element)
                if element.name == 'duration_cycle':
                    self.duration_cycle = element

    def get_some(self):
        instance = type(self.name, (object,), {})()
        print(self)
        exit(instance)

        print(self.name)
        for param in self.variables_partial_knowledge:
            print(param.name)
        return instance
