import json
import time

import pandas as pd
from System.Algorithms.Genetic import Genetic
from datetime import datetime


class Problem:
    __dataframe = None
    __partial = None
    __initial_params = None
    __env = None
    __resolve_data = {}

    def log(self, directory=''):
        json_str = json.dumps(self.__resolve_data, indent=2)
        with open(directory+'/'+self.__resolve_data['filename'], "w") as f:
            f.write(json_str)

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
        print("==================================")
        print("   Starting Animeta Optimizer...")
        print("==================================")
        self.__resolve_data['size'] = size
        self.__resolve_data['iteration'] = iteration
        self.__resolve_data['algo'] = algo
        date_now = datetime.now()
        file_format = date_now.strftime("%d-%m-%Y_%H-%M-%S")
        self.__resolve_data['filename'] = f"{file_format}.json"
        # time.sleep(1)
        print("\tPop. size:", size)
        print("\tNum. iteration:", iteration)
        # time.sleep(1)
        print('\tOther params.:')
        for k in params:
            self.__resolve_data[k] = params[k]
            print('\t\t', k, ':', params[k])
        print("==================================")
        print('\n')
        # time.sleep(1)

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
        a, b = solution
        self.__resolve_data['score'] = a['score']
        self.__resolve_data['scores'] = b
        '''
        r = a['solution'].get_graph().nodes(data=True)
        for n in r:
            print(n)
        self.__resolve_data['solution'] = r
        '''
        return solution

