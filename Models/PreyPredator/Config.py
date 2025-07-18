from System.Optimizer.Perception import Perception
from System.Core.AnimetaModel import AnimetaModel
from System.Core.Agent import Agent
from System.Core.ActionGetter import action_factory
from System.Core.Environment import Environment
from System.Core.Simulator import Simulator

model = AnimetaModel()
p1 = Perception('p_prey', perception_type='not_bool', radius=10, condition="π.@.type=='prey'", priority=10)
condition = "π.@.type=='predator' and π.@.eating==True"
p2 = Perception('is_eating', perception_type='not_bool', radius=15, condition=condition, priority=9)

prey = Agent(agent_type='prey')
prey.add_perception(
    {
        'perception': Perception('default', condition="$.type=='prey'"),
        'actions': [
            action_factory.get('RandomMove')(duration_cycle=1, max_velocity=(2, 2), move_probability=0.5)
        ]
    }
)

env_set = [
    {
        'agent': prey,
        'nb': 50,
        'initial_params': [
            {'position': (19, 73), 'energy': 10, 'active': False},
            {'position': (57, 42), 'energy': 10, 'active': False},
            {'position': (0, 1), 'energy': 10, 'active': False},
            {'position': (33, 12), 'energy': 10, 'active': False},
            {'position': (88, 61), 'energy': 10, 'active': False},
            {'position': (45, 29), 'energy': 10, 'active': False},
            {'position': (72, 95), 'energy': 10, 'active': False},
            {'position': (5, 38), 'energy': 10, 'active': False},
            {'position': (63, 77), 'energy': 10, 'active': False},
            {'position': (25, 54), 'energy': 10, 'active': False},
            {'position': (91, 16), 'energy': 10, 'active': False},
            {'position': (14, 82), 'energy': 10, 'active': False},
            {'position': (47, 6), 'energy': 10, 'active': False},
            {'position': (78, 33), 'energy': 10, 'active': False},
            {'position': (36, 69), 'energy': 10, 'active': False},
            {'position': (59, 21), 'energy': 10, 'active': False},
            {'position': (83, 48), 'energy': 10, 'active': False},
            {'position': (11, 93), 'energy': 10, 'active': False},
            {'position': (67, 27), 'energy': 10, 'active': False},
            {'position': (42, 85), 'energy': 10, 'active': False},
            {'position': (95, 57), 'energy': 10, 'active': False},
            {'position': (28, 32), 'energy': 10, 'active': False},
            {'position': (74, 64), 'energy': 10, 'active': False},
            {'position': (3, 19), 'energy': 10, 'active': False},
            {'position': (51, 79), 'energy': 10, 'active': False},
            {'position': (89, 42), 'energy': 10, 'active': False},
            {'position': (17, 66), 'energy': 10, 'active': False},
            {'position': (62, 8), 'energy': 10, 'active': False},
            {'position': (35, 45), 'energy': 10, 'active': False},
            {'position': (80, 71), 'energy': 10, 'active': False},
            {'position': (9, 25), 'energy': 10, 'active': False},
            {'position': (56, 91), 'energy': 10, 'active': False},
            {'position': (23, 39), 'energy': 10, 'active': False},
            {'position': (77, 15), 'energy': 10, 'active': False},
            {'position': (41, 62), 'energy': 10, 'active': False},
            {'position': (93, 35), 'energy': 10, 'active': False},
            {'position': (20, 87), 'energy': 10, 'active': False},
            {'position': (68, 49), 'energy': 10, 'active': False},
            {'position': (34, 23), 'energy': 10, 'active': False},
            {'position': (86, 75), 'energy': 10, 'active': False},
            {'position': (12, 51), 'energy': 10, 'active': False},
            {'position': (54, 18), 'energy': 10, 'active': False},
            {'position': (31, 97), 'energy': 10, 'active': False},
            {'position': (75, 43), 'energy': 10, 'active': False},
            {'position': (49, 67), 'energy': 10, 'active': False},
            {'position': (98, 22), 'energy': 10, 'active': False},
            {'position': (7, 89), 'energy': 10, 'active': False},
            {'position': (61, 36), 'energy': 10, 'active': False},
            {'position': (38, 58), 'energy': 10, 'active': False},
            {'position': (84, 13), 'energy': 10, 'active': False},
            {'position': (16, 74), 'energy': 10, 'active': False},
            {'position': (53, 31), 'energy': 10, 'active': False},
            {'position': (29, 86), 'energy': 10, 'active': False},
            {'position': (96, 47), 'energy': 10, 'active': False},
            {'position': (2, 65), 'energy': 10, 'active': False},
            {'position': (70, 14), 'energy': 10, 'active': False},
            {'position': (43, 52), 'energy': 10, 'active': False},
            {'position': (87, 28), 'energy': 10, 'active': False},
            {'position': (24, 96), 'energy': 10, 'active': False},
            {'position': (64, 41), 'energy': 10, 'active': False},
            {'position': (39, 78), 'energy': 10, 'active': False},
            {'position': (92, 5), 'energy': 10, 'active': False},
            {'position': (15, 59), 'energy': 10, 'active': False},
            {'position': (69, 82), 'energy': 10, 'active': False},
            {'position': (46, 24), 'energy': 10, 'active': False},
            {'position': (81, 60), 'energy': 10, 'active': False},
            {'position': (8, 37), 'energy': 10, 'active': False},
            {'position': (55, 90), 'energy': 10, 'active': False},
            {'position': (32, 17), 'energy': 10, 'active': False},
            {'position': (76, 83), 'energy': 10, 'active': False},
            {'position': (22, 44), 'energy': 10, 'active': False},
            {'position': (97, 70), 'energy': 10, 'active': False},
            {'position': (4, 26), 'energy': 10, 'active': False},
            {'position': (60, 98), 'energy': 10, 'active': False},
            {'position': (37, 53), 'energy': 10, 'active': False},
            {'position': (85, 9), 'energy': 10, 'active': False},
            {'position': (21, 76), 'energy': 10, 'active': False},
            {'position': (66, 34), 'energy': 10, 'active': False},
            {'position': (40, 92), 'energy': 10, 'active': False},
            {'position': (94, 55), 'energy': 10, 'active': False},
            {'position': (27, 3), 'energy': 10, 'active': False},
            {'position': (71, 68), 'energy': 10, 'active': False},
            {'position': (48, 30), 'energy': 10, 'active': False},
            {'position': (1, 84), 'energy': 10, 'active': False},
            {'position': (58, 11), 'energy': 10, 'active': False},
            {'position': (30, 63), 'energy': 10, 'active': False},
            {'position': (79, 40), 'energy': 10, 'active': False},
            {'position': (18, 99), 'energy': 10, 'active': False},
            {'position': (65, 56), 'energy': 10, 'active': False},
            {'position': (44, 20), 'energy': 10, 'active': False},
            {'position': (90, 80), 'energy': 10, 'active': False},
            {'position': (6, 46), 'energy': 10, 'active': False},
            {'position': (52, 2), 'energy': 10, 'active': False},
            {'position': (26, 72), 'energy': 10, 'active': False},
            {'position': (73, 50), 'energy': 10, 'active': False},
            {'position': (10, 7), 'energy': 10, 'active': False},
            {'position': (50, 88), 'energy': 10, 'active': False},
            {'position': (13, 4), 'energy': 10, 'active': False},
            {'position': (99, 94), 'energy': 10, 'active': False},
            {'position': (82, 1), 'energy': 10, 'active': False}
        ]
    }
]
env = Environment(width=100, height=100, environment_set=env_set, single_in_grid=False, toroidal=True)
