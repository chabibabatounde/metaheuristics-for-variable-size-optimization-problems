from System.Optimizer.Perception import Perception
from System.Core.AnimetaModel import AnimetaModel
from System.Core.Agent import Agent
from System.Core.ActionGetter import action_factory
from System.Core.Environment import Environment
from System.Core.Simulator import Simulator

model = AnimetaModel()

# plants
plant = Agent(agent_type='plant')
plant.add_perception(
    {
        'perception': Perception('default', condition="$.type=='plant'"),
        'actions': [
            action_factory.get('Void')(duration_cycle=1)
        ]
    }
)

# insects
insect = Agent(agent_type='insect')
insect.add_perception(
    {
        'perception': Perception('default', condition="$.type=='insect'"),
        'actions': [
            action_factory.get('RandomMove')(duration_cycle=1, max_velocity=(2, 2), move_probability=0.5)
        ]
    }
)
insect.add_perception(
    {
        'perception':
            Perception('p_plant', perception_type='not_bool', radius=10, condition="π.@.type=='plant'", priority=10),
        'actions': [
            action_factory.get('GoAndEat')(duration_cycle=1, gain=1, move_coast=0, kill=True)
        ]
    }
)
# amphibians
default_perception = Perception('default', condition="$.type=='amphibian'")
p_insect = Perception('p_insect', perception_type='not_bool', radius=10, condition="π.@.type=='insect'", priority=10)


env_set = [
    {
        'agent': plant,
        'nb': 100,
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
    },
    {
        'agent': insect,
        'nb': 50,
        'initial_params': [
                {'position': (7, 81), 'energy': 100, 'active': True},
                {'position': (22, 10), 'energy': 100, 'active': True},
                {'position': (43, 94), 'energy': 100, 'active': True},
                {'position': (66, 27), 'energy': 100, 'active': True},
                {'position': (85, 53), 'energy': 100, 'active': True},
                {'position': (11, 68), 'energy': 100, 'active': True},
                {'position': (34, 16), 'energy': 100, 'active': True},
                {'position': (59, 39), 'energy': 100, 'active': True},
                {'position': (76, 99), 'energy': 100, 'active': True},
                {'position': (92, 4), 'energy': 100, 'active': True},
                {'position': (18, 75), 'energy': 100, 'active': True},
                {'position': (37, 22), 'energy': 100, 'active': True},
                {'position': (55, 60), 'energy': 100, 'active': True},
                {'position': (63, 83), 'energy': 100, 'active': True},
                {'position': (26, 44), 'energy': 100, 'active': True},
                {'position': (48, 9), 'energy': 100, 'active': True},
                {'position': (71, 67), 'energy': 100, 'active': True},
                {'position': (3, 31), 'energy': 100, 'active': True},
                {'position': (88, 76), 'energy': 100, 'active': True},
                {'position': (14, 52), 'energy': 100, 'active': True},
                {'position': (32, 98), 'energy': 100, 'active': True},
                {'position': (57, 13), 'energy': 100, 'active': True},
                {'position': (79, 41), 'energy': 100, 'active': True},
                {'position': (95, 85), 'energy': 100, 'active': True},
                {'position': (8, 63), 'energy': 100, 'active': True},
                {'position': (29, 26), 'energy': 100, 'active': True},
                {'position': (46, 70), 'energy': 100, 'active': True},
                {'position': (67, 5), 'energy': 100, 'active': True},
                {'position': (83, 48), 'energy': 100, 'active': True},
                {'position': (21, 90), 'energy': 100, 'active': True},
                {'position': (40, 35), 'energy': 100, 'active': True},
                {'position': (62, 79), 'energy': 100, 'active': True},
                {'position': (4, 56), 'energy': 100, 'active': True},
                {'position': (27, 18), 'energy': 100, 'active': True},
                {'position': (50, 97), 'energy': 100, 'active': True},
                {'position': (72, 30), 'energy': 100, 'active': True},
                {'position': (89, 64), 'energy': 100, 'active': True},
                {'position': (15, 42), 'energy': 100, 'active': True},
                {'position': (38, 86), 'energy': 100, 'active': True},
                {'position': (54, 11), 'energy': 100, 'active': True},
                {'position': (70, 54), 'energy': 100, 'active': True},
                {'position': (94, 28), 'energy': 100, 'active': True},
                {'position': (12, 73), 'energy': 100, 'active': True},
                {'position': (31, 49), 'energy': 100, 'active': True},
                {'position': (58, 84), 'energy': 100, 'active': True},
                {'position': (80, 20), 'energy': 100, 'active': True},
                {'position': (96, 37), 'energy': 100, 'active': True},
                {'position': (6, 61), 'energy': 100, 'active': True},
                {'position': (24, 93), 'energy': 100, 'active': True},
                {'position': (45, 25), 'energy': 100, 'active': True},
                {'position': (64, 69), 'energy': 100, 'active': True},
                {'position': (87, 2), 'energy': 100, 'active': True},
                {'position': (9, 45), 'energy': 100, 'active': True},
                {'position': (33, 78), 'energy': 100, 'active': True},
                {'position': (52, 14), 'energy': 100, 'active': True},
                {'position': (73, 51), 'energy': 100, 'active': True},
                {'position': (98, 32), 'energy': 100, 'active': True},
                {'position': (17, 65), 'energy': 100, 'active': True},
                {'position': (41, 23), 'energy': 100, 'active': True},
                {'position': (60, 87), 'energy': 100, 'active': True},
                {'position': (82, 38), 'energy': 100, 'active': True},
                {'position': (1, 72), 'energy': 100, 'active': True},
                {'position': (28, 6), 'energy': 100, 'active': True},
                {'position': (49, 59), 'energy': 100, 'active': True},
                {'position': (68, 95), 'energy': 100, 'active': True},
                {'position': (90, 21), 'energy': 100, 'active': True},
                {'position': (13, 43), 'energy': 100, 'active': True},
                {'position': (36, 77), 'energy': 100, 'active': True},
                {'position': (53, 8), 'energy': 100, 'active': True},
                {'position': (74, 50), 'energy': 100, 'active': True},
                {'position': (99, 36), 'energy': 100, 'active': True},
                {'position': (19, 82), 'energy': 100, 'active': True},
                {'position': (42, 17), 'energy': 100, 'active': True},
                {'position': (61, 66), 'energy': 100, 'active': True},
                {'position': (86, 29), 'energy': 100, 'active': True},
                {'position': (5, 91), 'energy': 100, 'active': True},
                {'position': (30, 55), 'energy': 100, 'active': True},
                {'position': (51, 3), 'energy': 100, 'active': True},
                {'position': (69, 74), 'energy': 100, 'active': True},
                {'position': (93, 46), 'energy': 100, 'active': True},
                {'position': (16, 62), 'energy': 100, 'active': True},
                {'position': (39, 12), 'energy': 100, 'active': True},
                {'position': (56, 80), 'energy': 100, 'active': True},
                {'position': (77, 34), 'energy': 100, 'active': True},
                {'position': (97, 7), 'energy': 100, 'active': True},
                {'position': (10, 47), 'energy': 100, 'active': True},
                {'position': (35, 88), 'energy': 100, 'active': True},
                {'position': (54, 24), 'energy': 100, 'active': True},
                {'position': (75, 58), 'energy': 100, 'active': True},
                {'position': (91, 40), 'energy': 100, 'active': True},
                {'position': (20, 71), 'energy': 100, 'active': True},
                {'position': (44, 15), 'energy': 100, 'active': True},
                {'position': (65, 96), 'energy': 100, 'active': True},
                {'position': (81, 33), 'energy': 100, 'active': True},
                {'position': (2, 57), 'energy': 100, 'active': True},
                {'position': (25, 92), 'energy': 100, 'active': True},
                {'position': (47, 19), 'energy': 100, 'active': True},
                {'position': (63, 65), 'energy': 100, 'active': True},
                {'position': (84, 0), 'energy': 100, 'active': True}
            ]
    }
]

env = Environment(width=100, height=100, environment_set=env_set, single_in_grid=False, toroidal=True)
