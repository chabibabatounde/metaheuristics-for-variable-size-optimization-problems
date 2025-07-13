import random

from Models.Amphibian.Config import *
from System.Optimizer.Problem import Problem
from System.Optimizer.Animeta import Animeta
from System.Optimizer.PartialAction import PartialAction
from System.Optimizer.PartialKnowledge import PartialKnowledge
from System.Evaluation.Fonctions import *
from System.Core.ActionGetter import action_factory

partial = Animeta('amphibian')

partial.add_perception(p_insect, [
    PartialAction(
        'GoAndEat',
        1,
        PartialKnowledge(
            name='gain',
            range_start_point=0,
            range_end_point=10,
            attribute_type='int',
        )
    )
])
partial.add_perception(default_perception, [
    action_factory.get('RandomMove')(duration_cycle=1, max_velocity=(5, 5), move_probability=0.5),
])

res = []

initial_params = [
    {'position': (10, 10), 'energy': 100, 'eating': False},
    {'position': (30, 30), 'energy': 100, 'eating': False},
    {'position': (50, 50), 'energy': 100, 'eating': False},
    {'position': (70, 70), 'energy': 100, 'eating': False},
    {'position': (90, 90), 'energy': 100, 'eating': False}
]

for i in range(1):
    size = random.randint(10, 20)
    cross_percentage = random.randint(10, 25)
    diversity_percentage = cross_percentage / 2
    iteration = random.randint(100, 500)

    size = 25
    cross_percentage = 25
    diversity_percentage = cross_percentage / 2
    iteration = 100

    pb = Problem(
        partial=partial,
        data_set_path='Data.csv',
        variables=['energy'],
        funct=rmse,
        initial_params=initial_params,
        env=env
    )
    pb.minimise(
        score_wanted=0,
        iteration=iteration,
        size=size,
        algorithm='AG',
        params={
            'nb_cross': int(size/100*cross_percentage),
            'nb_new': int(size/100*diversity_percentage),
            'p_mutation': 0.5
        }
    )
    pb.log('Results')
