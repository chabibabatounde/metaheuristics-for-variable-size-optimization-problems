from System.Optimizer.Actions.Action import Action
import random


class RandomMove(Action):
    move_probability = None
    max_velocity = None
    max_attempt = None
    lost = None

    def __init__(self, duration_cycle=0, max_velocity=(2, 2), lost=0, move_probability=0.5, max_attempt=4):
        if move_probability < 0 or move_probability > 1:
            exit("The probability value must be between 0 and 1")
        Action.__init__(self, duration_cycle)
        self.name = "RandomMove"
        self.max_attempt = max_attempt
        self.max_velocity = max_velocity
        self.move_probability = move_probability
        self.lost = lost
        self.perception_need = False
        # print("\t ", "Action \""+self.name+"\" Created", "ID =", id(self))

    def executes(self, agent, perception_result=None):
        raffle_draw = random.uniform(0, 1)
        if raffle_draw > self.move_probability:
            pass
        else:
            ax = random.randint(-1 * self.max_velocity[0], self.max_velocity[0])
            ay = random.randint(-1 * self.max_velocity[1], self.max_velocity[1])

            new_velocity = (agent.velocity[0] + ax, agent.velocity[1] + ay)
            new_velocity = (ax, ay)
            new_position = (agent.position[0] + new_velocity[0], agent.position[1] + new_velocity[1])
            count = 0
            while count < self.max_attempt and not agent.grid.is_move_possible(new_position):
                ax = random.randint(-1 * self.max_velocity[0], self.max_velocity[0])
                ay = random.randint(-1 * self.max_velocity[1], self.max_velocity[1])
                new_velocity = (agent.velocity[0] + ax, agent.velocity[1] + ay)
                new_velocity = (ax, ay)
                new_position = (agent.position[0] + new_velocity[0], agent.position[1] + new_velocity[1])
                count += 1
            if agent.grid.is_move_possible(new_position):
                # print("\n => ", agent.type, agent.position, self.name, new_position)
                move(agent, new_velocity, coast=self.lost)
