from mesa.space import MultiGrid


def move_agent_to(agent, pos):
    agent.model.grid.remove_agent(agent)
    agent.model.grid.place_agent(agent, pos)
    agent.pos = pos


def random_move(agent, max_v=(2, 2)):
    current_x, current_y = agent.pos
    possible_steps = []
    for dx in range(-max_v[0], max_v[0] + 1):
        for dy in range(-max_v[1], max_v[1] + 1):
            distance = int(round((dx ** 2 + dy ** 2) ** 0.5))
            if 0 < distance <= int(round((max_v[0] ** 2 + max_v[1] ** 2) ** 0.5)):
                new_x = current_x + dx
                new_y = current_y + dy
                new_position = (new_x, new_y)
                if not agent.model.grid.out_of_bounds(new_position):
                    if not isinstance(agent.model.grid, MultiGrid) or agent.model.grid.is_cell_empty(new_position):
                        possible_steps.append(new_position)
                    elif isinstance(agent.model.grid, MultiGrid):
                        possible_steps.append(new_position)
    if possible_steps:
        new_position = agent.random.choice(possible_steps)
        move_agent_to(agent, new_position)


def die(agent):
    agent.active = False
    agent.alive = False
    if hasattr(agent.model, 'grid') and agent.model.grid is not None:
        agent.model.grid.remove_agent(agent)
    else:
        agent.model.space.remove_agent(agent)
