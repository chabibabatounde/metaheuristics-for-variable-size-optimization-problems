from Models.Amphibian.Config import *

# amphibian
amphibian = {'type': 'amphibian', 'perceptions': [
    {
        'perception': p_insect,
        'actions': [
            action_factory.get('GoAndEat')(duration_cycle=1, gain=10, move_coast=0, kill=True),
        ]
    }
    ,
    {
        'perception': default_perception,
        'actions': [
            action_factory.get('RandomMove')(duration_cycle=1, max_velocity=(5, 5), move_probability=0.5)
        ]
    }
]}
initial_params = [
    {'position': (10, 10), 'energy': 100, 'eating': False},
    # {'position': (20, 20), 'energy': 100, 'eating': False},
    {'position': (30, 30), 'energy': 100, 'eating': False},
    # {'position': (40, 40), 'energy': 100, 'eating': False},
    {'position': (50, 50), 'energy': 100, 'eating': False},
    # {'position': (60, 60), 'energy': 100, 'eating': False},
    {'position': (70, 70), 'energy': 100, 'eating': False},
    # {'position': (80, 80), 'energy': 100, 'eating': False},
    {'position': (90, 90), 'energy': 100, 'eating': False}
]
simulator = Simulator(amphibian, initial_params, env)
simulator.run(10)
data = simulator.read_data(variable='AgentID', value=1)
data.to_csv('Data.csv')
print("Simulation terminée")
