import pandas as pd
from System.Algorithms.Genetic import Genetic


class Problem:
    __dataframe = None
    __partial = None
    __algorithms = None

    def __init__(self, partial, data_set_path):
        self.__partial = partial
        self.__dataframe = pd.read_csv(data_set_path)

    def minimise(self, score_wanted=0, iteration=100, size=100, algorithm=None, params={}):
        return self.__resolve(score_wanted, iteration, size, algorithm, params)

    def maximise(self, score_wanted=0, iteration=100, size=100, algorithm=None, params={}):
        if score_wanted == 0:
            exit('0 as score @Problem.maximise')
        score = 1 / score_wanted
        return self.__resolve(score, iteration, size, algorithm, params)

    def __resolve(self, score_wanted, iteration, size, algo, params):
        solution = None
        if algo == 'AG':
            algorithm = Genetic(self.__partial, score_wanted, iteration, size)
            solution = algorithm.optimize(self.__dataframe, params)
        else:
            raise ValueError("0 as score @Problem.maximize")
        return solution
