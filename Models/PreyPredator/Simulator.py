from Models.PreyPredator.Config import *

# Predator
agent_dict = {'type': 'predator', 'perceptions': [
    {
        'perception': p1,
        'actions': [
            action_factory.get('Eat')(duration_cycle=5, gain=1, move_coast=0, kill=True),
        ]
    }
    ,
    {
        'perception': p2,
        'actions': [
            action_factory.get('GetClose')(duration_cycle=1)
        ]
    }
]}
initial_params = [
    {'position': (00, 00), 'energy': 100, 'eating': False},
    {'position': (10, 10), 'energy': 100, 'eating': False},
    {'position': (20, 20), 'energy': 100, 'eating': False},
    {'position': (30, 30), 'energy': 100, 'eating': False},
    {'position': (40, 40), 'energy': 100, 'eating': False}
]

simulator = Simulator(agent_dict, initial_params, env)
simulator.run(100)
data = simulator.read_data(variable='AgentID', value=1)
data.to_csv('PreyPredator/Data.csv')
print("Simulation terminée")
