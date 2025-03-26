class Algorithm:
    partial = None
    score_wanted = 0
    iteration = 100
    size = 100

    def __init__(self, partial=None, score_wanted=0, iteration=100, size=100):
        self.partial = partial
        self.score_wanted = score_wanted
        self.iteration = iteration
        self.size = size

    def optimize(self, params=None):
        exit('Please define the <optimize> method for the algorithm you used')
