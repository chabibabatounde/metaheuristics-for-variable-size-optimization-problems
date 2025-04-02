class Action:

    def surcharge(self, param, value):
        self.__setattr__(param, value)

    def __init__(self, name):
        self.name = name
