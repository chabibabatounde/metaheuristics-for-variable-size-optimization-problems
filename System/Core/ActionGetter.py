from System.Core.Actions.Eat import Eat
from System.Core.Actions.RandomMove import RandomMove
from System.Core.Actions.GetClose import GetClose


class ActionGetter:
    __class_items = {}

    def __init__(self):
        self.__class_items = {
            'Eat': Eat,
            'RandomMove': RandomMove,
            'GetClose': GetClose
        }

    def get(self, action_name):
        return self.__class_items[action_name]

    def get_parameters(self, action_name):
        c = self.__class_items[action_name]
        c = c(0)
        return c.get_attributes()


action_factory = ActionGetter()
