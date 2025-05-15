from System.Optimizer.PartialKnowledge import PartialKnowledge
import importlib


class PartialAction:
    name = None
    duration_cycle = None
    variables_partial_knowledge = []

    def __init__(self, name, duration=None, *partial_knowledge):
        partial_knowledge = list(partial_knowledge)
        self.name = name
        self.duration = duration
        if duration is not None:
            self.variables_partial_knowledge.append(PartialKnowledge(name='duration_cycle', value=duration))
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
        return instance
