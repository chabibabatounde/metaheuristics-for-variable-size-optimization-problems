from System.Optimizer.Actions.Action import Action
import random


class RunAway(Action):
    name = "RunAway"
    move_coast = 0
    perception_need = True

    def __init__(self, duration_cycle=0, move_coast=0):
        self.name = "RunAway"
        self.move_coast = move_coast
        self.perception_need = True
        Action.__init__(self, duration_cycle)

    def executes(self, agent, perception_result):
        if self.is_executable(agent, perception_result):
            if 1 == random.choice([0, 1]):
                velocity = (
                    perception_result.closer_agent.velocity[0],
                    (-1) * perception_result.closer_agent.velocity[1]
                )
            else:
                velocity = (
                    (-1) * perception_result.closer_agent.velocity[0],
                    perception_result.closer_agent.velocity[1]
                )
            acceleration = (0, 0)
            move(agent, velocity, acceleration, coast=self.move_coast)
            """
            velocity = (
                -1 * perception_result.closer_agent.velocity[0], -
                1 * perception_result.closer_agent.velocity[1]
            )
            while np.linalg.norm(acceleration) < self.max_acceleration:
                tick = random.randint(1, 2)
                if tick == 1:
                    if velocity[0] < 0:
                        acceleration = (acceleration[0]-1, acceleration[1])
                    else:
                        acceleration = (acceleration[0]+1, acceleration[1])
                else:
                    if velocity[1] < 0:
                        acceleration = (acceleration[0], acceleration[1]-1)
                    else:
                        acceleration = (acceleration[0], acceleration[1]+1)
            """

