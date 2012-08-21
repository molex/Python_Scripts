def more_pour_problem(capacities, goal, start=None):
    """The first argument is a tuple of capacities (numbers) of glasses; the
    goal is a number which we must achieve in some glass.  start is a tuple
    of starting levels for each glass; if None, that means 0 for all.
    Start at start state and follow successors until we reach the goal.
    Keep track of frontier and previously explored; fail when no frontier.
    On success return a path: a [state, action, state2, ...] list, where an
    action is one of ('fill', i), ('empty', i), ('pour', i, j), where
    i and j are indices indicating the glass number."""

    glass_filled.goal = goal
    pour_successors.capacities = capacities
    state = start if start is not None else (tuple([0] * len(capacities)))

    return shortest_path_search(state, pour_successors, glass_filled)


def pour_successors(glasses):
    """Return a dict of {state:action} pairs describing what can be reached from
     the (x, y) state and how."""
    num_glasses = len(pour_successors.capacities)

    assert num_glasses == len(glasses)
    for i in range(num_glasses): assert pour_successors.capacities[i] >= glasses[i]

    successors = {}
    successors.update(
        dict(( fill_glass(i, glasses), ('fill', i))
                for i in range(num_glasses) if not glasses[i] == pour_successors.capacities[i]
        )
    )
    successors.update(
        dict(( empty_glass(i, glasses), ('empty', i))
                for i in range(num_glasses) if not glasses[i] == 0
        )
    )
    successors.update(
        dict(( pour_glass(i, j, glasses), ('pour', i, j))
                for i in range(num_glasses) if not glasses[i] == 0
                for j in range(num_glasses) if not i == j
        )
    )

    return successors

def glass_filled(state):
    return glass_filled.goal in state

def fill_glass(i, glasses):
    glasses_copy = list(glasses)
    glasses_copy[i] = pour_successors.capacities[i]
    return tuple(glasses_copy)

def empty_glass(i, glasses):
    glasses_copy = list(glasses)
    glasses_copy[i] = 0
    return tuple(glasses_copy)

def pour_glass(i, j, glasses):
    """ Pour from glass i into glass j """

    c = pour_successors.capacities
    g = list(glasses)

    new_i = 0 if g[i] + g[j] <= c[j] else g[i]-(c[j]-g[j])
    g[j] = g[i] + g[j] if g[i] + g[j] <= c[j] else c[j]
    g[i] = new_i

    return tuple(g)

def shortest_path_search(start, successors, is_goal):
    """Find the shortest path from start state to a state
    such that is_goal(state) is true."""
    if is_goal(start):
        return [start]
    explored = set()
    frontier = [ [start] ]
    while frontier:
        path = frontier.pop(0)
        s = path[-1]
        for (state, action) in successors(s).items():
            if state not in explored:
                explored.add(state)
                path2 = path + [action, state]
                if is_goal(state):
                    return path2
                else:
                    frontier.append(path2)
    return Fail

Fail = []

def test_more_pour():
    assert more_pour_problem((1, 2, 4, 8), 4) == [
        (0, 0, 0, 0), ('fill', 2), (0, 0, 4, 0)]
    assert more_pour_problem((1, 2, 4), 3) == [
        (0, 0, 0), ('fill', 2), (0, 0, 4), ('pour', 2, 0), (1, 0, 3)] 
    starbucks = (8, 12, 16, 20, 24)
    assert not any(more_pour_problem(starbucks, odd) for odd in (3, 5, 7, 9))
    assert all(more_pour_problem((1, 3, 9, 27), n) for n in range(28))
    assert more_pour_problem((1, 3, 9, 27), 28) == []
    return 'test_more_pour passes'

print test_more_pour()
