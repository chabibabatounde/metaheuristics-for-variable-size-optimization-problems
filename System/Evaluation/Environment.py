class Environment:
    width = 0
    height = 0
    symbol_tab = ["o", "*", "s", ">"]
    is_toroidal = False
    single_in_grid = True
    environment_set = []

    def __init__(self, width, height, single_in_grid=True, toroidal=False):
        self.width = width  # X-axis
        self.height = height  # Y-axis
        self.is_toroidal = toroidal
        self.single_in_grid = single_in_grid
        self.symbol_tab = ["o", "*", "s", ">"]
        self.environment_set = []
