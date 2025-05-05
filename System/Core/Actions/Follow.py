from System.Core.Actions.Action import Action
import random
import copy

class Follow(Action):
    def __init__(self, duration_cycle=1, move_coast=1, spacing=2):
        Action.__init__(self, duration_cycle)
        self.name = "Follow"
        self.move_coast = move_coast
        self.spacing = spacing
        self.perception_need = True

    def executes(self, agent, perception_result):
        heading_x = (perception_result.closer_agent_position[0] - agent.position[0])
        heading_y = (perception_result.closer_agent_position[1] - agent.position[1])
        if heading_x != 0:
            heading_x = abs(heading_x) / heading_x
        else:
            heading_x = 0

        if heading_y != 0:
            heading_y = abs(heading_y) / heading_y
        else:
            heading_y = 0
        heading = (int(heading_x), int(heading_y))
        positions = []
        x_start_end = (agent.position[0], perception_result.closer_agent_position[0])
        y_start_end = (agent.position[1], perception_result.closer_agent_position[1])
        if x_start_end[0] > x_start_end[1]:
            x_start_end = (x_start_end[1], x_start_end[0])
        if y_start_end[0] > y_start_end[1]:
            y_start_end = (y_start_end[1], y_start_end[0])
        for x in range(x_start_end[0], x_start_end[1] + 1):
            for y in range(y_start_end[0], y_start_end[1] + 1):
                dist = agent.grid.distance((x, y), perception_result.closer_agent_position, is_agent=False)
                if dist >= self.spacing and agent.grid.is_move_possible((x, y)):
                    positions.append({'pos': (x, y), 'dist': dist})
        if len(positions) > 0:
            place_agent(agent, positions[0]['pos'])
            agent.energy -= agent.grid.distance(agent.position, positions[0]['pos'], False) * self.move_coast

    def get_some_instance(self):
        element = copy.deepcopy(self)
        element.move_coast = random.uniform(0, 10)
        element.spacing = random.randint(1, 5)
        return element