import random
from System.Algorithms.Algorithm import Algorithm


class Genetic(Algorithm):

    def __init__(self, partial, score_wanted, iteration, size):
        super().__init__(partial, score_wanted, iteration, size)

    def optimize(self, params):
        population = []
        # initialize population
        for _ in range(self.size):
            population.append(self.partial.get_some())

        # ---WHILE---
        # Choose_candidates
        # Crossover
        # Check lethality
        # Evaluate
        # Generate and evaluate new solutions
        # Update population
        # ---END WHILE---
        return random.uniform(0, 100)
