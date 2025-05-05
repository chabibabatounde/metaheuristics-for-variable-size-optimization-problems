import pandas as pd
from System.Algorithms.Genetic import Genetic


class Problem:
    __dataframe = None
    __partial = None
    __initial_params = None
    __env = None

    def __init__(self, partial, data_set_path, funct, variables=[], initial_params=[], env=None):
        self.__dataframe = pd.read_csv(data_set_path)
        self.__partial = partial
        self.__initial_params = initial_params
        self.__function = funct
        self.__variables = variables
        self.__env = env
        if 'pos' in list(self.__dataframe.columns):
            self.__dataframe['pos'] = self.__dataframe['pos'].apply(eval)
            self.__dataframe['x'] = self.__dataframe['pos'].apply(lambda pos: pos[0])
            self.__dataframe['y'] = self.__dataframe['pos'].apply(lambda pos: pos[1])
            self.__dataframe = self.__dataframe.drop(['timer', 'pos'], axis=1)


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
            solution = algorithm.optimize(
                self.__dataframe,
                params,
                self.__initial_params,
                self.__env,
                self.__function,
                self.__variables
            )
        else:
            raise ValueError("0 as score @Problem.maximize")
        return solution
