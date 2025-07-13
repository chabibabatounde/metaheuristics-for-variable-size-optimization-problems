import random

from System.Optimizer.PartialKnowledge import PartialKnowledge
from System.Optimizer.Partial import Partial
import importlib


class PartialAction(Partial):
    name = None
    duration_cycle = None
    variables_partial_knowledge = []

    def __init__(self, name, duration=None, *partial_knowledge):
        partial_knowledge = list(partial_knowledge)
        self.name = name
        self.duration_cycle = duration
        self.partial_knowledge(partial_knowledge)

    def partial_knowledge(self, partial_knowledges):
        for element in partial_knowledges:
            if element.value is not None:
                self.variables_partial_knowledge.append(PartialKnowledge(name=element.name, value=element.value))
            else:
                self.variables_partial_knowledge.append(element)

    def get_some(self):
        module_name = f"System.Core.Actions.{self.name}"
        module = importlib.import_module(module_name)
        MyClass = getattr(module, self.name)
        instance = MyClass()
        instance = instance.sample()
        for param in self.variables_partial_knowledge:
            setattr(instance, param.name, param.get_some())

        if self.duration_cycle is None:
            setattr(instance, 'duration_cycle', random.randint(1, 11))
        elif isinstance(self.duration_cycle, Partial):
            setattr(instance, 'duration_cycle', self.duration_cycle.get_some())
        else:
            setattr(instance, 'duration_cycle', self.duration_cycle)

        return instance
