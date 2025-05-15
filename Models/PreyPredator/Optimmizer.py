from Models.PreyPredator.Config import *
from System.Optimizer.Problem import Problem
from System.Optimizer.Animeta import Animeta
from System.Optimizer.PartialAction import PartialAction
from System.Optimizer.PartialKnowledge import PartialKnowledge
from System.Evaluation.Fonctions import *

partial = Animeta('predator')

partial.add_perception(p1, [
    PartialAction(
        'Eat',
        5,
        PartialKnowledge(
            name='gain',
            value=10
        ),
        PartialKnowledge(
            name='move_coast',
            range_start_point=3,
            range_end_point=5,
            attribute_type='int',
        )
    )
])
partial.add_perception(p2, [
    PartialAction(
        'GetClose',
        1
    ),
])
res = []

initial_params = [
    {'position': (00, 00), 'energy': 100, 'eating': False},
    {'position': (10, 10), 'energy': 100, 'eating': False},
    {'position': (20, 20), 'energy': 100, 'eating': False},
    {'position': (30, 30), 'energy': 100, 'eating': False},
    {'position': (40, 40), 'energy': 100, 'eating': False}
]
for i in range(100):
    pb = Problem(
        partial=partial,
        data_set_path='data.csv',
        variables=['position'],
        funct=rmse,
        initial_params=initial_params,
        env=env
    )
    result = pb.minimise(
        score_wanted=0,
        iteration=100,
        size=50,
        algorithm='AG',
        params={'nb_cross': 5, 'nb_new': 5, 'p_mutation': 0.5}
    )
    res.append(result)
