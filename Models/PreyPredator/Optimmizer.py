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
        2,
        PartialKnowledge(
            name='move_coast',
            value=1
        )
    ),
    PartialAction(
        'Sleep',
        5,
        PartialKnowledge(
            name='gain',
            value=1
        )
    ),
])
partial.add_perception(p2, [
    PartialAction(
        'Sleep',
        3,
        PartialKnowledge(
            name='gain',
            value=1
        )
    ),
])
res = []
initial_params = [
    {'position': (00, 00), 'energy': '100'},
    {'position': (10, 10), 'energy': '100'},
    {'position': (20, 20), 'energy': '100'},
    {'position': (30, 30), 'energy': '100'},
    {'position': (40, 40), 'energy': '100'}
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
        size=10,
        algorithm='AG',
        params={'nb_cross': 10, 'nb_new': 10, 'p_mutation': 0.5}
    )
    res.append(result)
