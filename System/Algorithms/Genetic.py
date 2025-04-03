import random
from System.Algorithms.Algorithm import Algorithm


class Genetic(Algorithm):

    def __init__(self, partial, score_wanted, iteration, size):
        super().__init__(partial, score_wanted, iteration, size)

    def __candidates(self, len):
        c1 = random.randint(0, len)
        c2 = random.randint(0, len)
        while c1 == c2:
            c2 = random.randint(0, len)
        return c1, c2

    def optimize(self, df, params=None):
        if params is None:
            params = {'nb_cross': 3, 'nb_new': 2, 'p_mutation': 0.5}
        population = []
        iteration = 0
        # initialize population
        for _ in range(self.size):
            s = self.partial.get_some(self.partial)
            population.append({
                'solution': s,
                'score': s.eval(df)
            })
        # ---WHILE---
        while iteration < self.iteration:
            iteration += 1
            # Choose_candidates
            for _ in range(params['nb_cross']):
                c1, c2 = self.__candidates(len(population))
                # Crossover
                # Check lethality
                # Evaluate
            for _ in range(params['nb_new']):
                s = self.partial.get_some(self.partial)
                population.append({
                    'solution': s,
                    'score': s.eval(df)
                })
            # Update population
            population = sorted(population, key=lambda x: x["score"], reverse=False)[:self.size]
            # ---END WHILE---
        exit('Genetic Algorithm')
        return random.uniform(0, 100)
