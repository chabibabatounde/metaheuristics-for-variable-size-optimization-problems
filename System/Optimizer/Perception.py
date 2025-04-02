class Perception:
    __condition = None
    name = ''

    def __init__(self, name, condition):
        self.__condition = condition
        self.name = name

    def __trigger(self, simulator):
        exec(self.__condition)
        return True, []

    def percept(self, simulator):
        return self.__trigger(simulator)
