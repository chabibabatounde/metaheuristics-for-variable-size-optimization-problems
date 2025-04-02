from System.Optimizer.Problem import Problem
from System.Optimizer.Animeta import Animeta
from System.Optimizer.Perception import Perception
from System.Optimizer.PartialAction import PartialAction
from System.Optimizer.PartialKnowledge import PartialKnowledge

partial = Animeta()
percept_1 = Perception('p1', '€.timer%9==0')
# percept_2 = Perception('p2', '€.timer%7==0')
# percept_3 = Perception('p3', '€.timer%13==0')

partial.add_perception(percept_1, [
    PartialAction(
        'Eat',
        5,
        PartialKnowledge(
            name='duration',
            value=1
        )
    )
])


pb = Problem(
    partial=partial,
    data_set_path='Data/positions.csv'
)

result = pb.minimise(
    score_wanted=0,
    iteration=100,
    size=100,
    algorithm='AG',
    params={
        'n_new': 10,
        'p_m': 0.2,
        'n_crossing': 20
    }
)

