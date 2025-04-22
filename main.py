from System.Optimizer.Problem import Problem
from System.Optimizer.Animeta import Animeta
from System.Optimizer.Perception import Perception
from System.Optimizer.PartialAction import PartialAction
from System.Optimizer.PartialKnowledge import PartialKnowledge






partial = Animeta()
percept_1 = Perception('p1', 'π.@.energy < 50', perception_type='items')
percept_2 = Perception('p2', '€.timer%9 == 0', perception_type='bool')

partial.add_perception(percept_1, [
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

partial.add_perception(percept_2, [
    PartialAction(
        'Sleep',
        3,
        PartialKnowledge(
            name='gain',
            value=1
        )
    ),
])

pb = Problem(
    partial=partial,
    data_set_path='Data/positions.csv'
)

result = pb.minimise(
    score_wanted=0,
    iteration=100,
    size=2,
    algorithm='AG',
    params={'nb_cross': 10, 'nb_new': 5, 'p_mutation': 0.5}
)

