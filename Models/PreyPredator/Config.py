from System.Optimizer.Perception import Perception
from System.Core.AnimetaModel import AnimetaModel
from System.Core.Agent import Agent
from System.Core.Simulator import Simulator
from System.Core.ActionGetter import action_factory
from System.Core.Environment import Environment

model = AnimetaModel()
p1 = Perception('p_prey', perception_type='not_bool', radius=10, condition="π.@.type=='prey'", priority=10)
p2 = Perception('default', condition="$.type=='predator'")
condition = "π.@.type=='predator' and π.@.eating==True"
p3 = Perception('is_eating', perception_type='not_bool', radius=10, condition=condition, priority=9)

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
        'nb': 10,
        'initial_params': [
            {'position': (5, 0), 'energy': 10},
            {'position': (23, 47), 'energy': 10},
            {'position': (82, 16), 'energy': 10},
            {'position': (36, 71), 'energy': 10},
            {'position': (91, 92), 'energy': 10},
            {'position': (14, 63), 'energy': 10},
            {'position': (58, 29), 'energy': 10},
            {'position': (67, 85), 'energy': 10},
            {'position': (42, 38), 'energy': 10},
            {'position': (3, 55), 'energy': 10}
        ]
    }
]
env = Environment(width=100, height=100, environment_set=env_set, single_in_grid=False, toroidal=True)
