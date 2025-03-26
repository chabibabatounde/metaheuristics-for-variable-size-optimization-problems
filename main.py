from System.Optimizer.Problem import Problem
from System.Optimizer.Partial import Partial

partial = Partial()

pb = Problem(
    partial=partial,
    data_set_path='Data/positions.csv'
)

pb.minimise(
    score_wanted=0,
    iteration=100,
    size=100,
    algorithm='AG',
    params={}
)
