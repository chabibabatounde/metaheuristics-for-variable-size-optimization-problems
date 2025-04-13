import numpy as np

class Grid:
    __timer = 1
    timer = 0
    width = 0
    height = 0
    content = []
    agents = []
    __active_agents = []
    __off_agents = []
    symbol_tab = ["o", "*", "s", ">"]
    is_toroidal = False
    single_in_grid = True

    def __init__(self, width, height, timer=0, single_in_grid=True, toroidal=False):
        self.__id = 1
        self.__timer = timer
        self.timer = timer
        self.width = width  # X-axis
        self.height = height  # Y-axis
        self.content = np.empty((self.width, self.height), dtype=object)
        self.is_toroidal = toroidal
        self.single_in_grid = single_in_grid
        self.symbol_tab = ["o", "*", ">"]
        self.agents = []
        self.__active_agents = []
        self.__off_agents = []
