# -----------------
# User Instructions
# 
# In this problem, you will solve the pouring problem for an arbitrary
# number of glasses. Write a function, more_pour_problem, that takes 
# as input capacities, goal, and (optionally) start. This function should 
# return a path of states and actions.
#
# Capacities is a tuple of numbers, where each number represents the 
# volume of a glass. 
#
# Goal is the desired volume and start is a tuple of the starting levels
# in each glass. Start defaults to None (all glasses empty).
#
# The returned path should look like [state, action, state, action, ... ]
# where state is a tuple of volumes and action is one of ('fill', i), 
# ('empty', i), ('pour', i, j) where i and j are indices indicating the 
# glass number. 
from operator import add, sub

def more_pour_problem(capacities, goal, start=None):
    """The first argument is a tuple of capacities (numbers) of glasses; the
    goal is a number which we must achieve in some glass.  start is a tuple
    of starting levels for each glass; if None, that means 0 for all.
    Start at start state and follow successors until we reach the goal.
    Keep track of frontier and previously explored; fail when no frontier.
    On success return a path: a [state, action, state2, ...] list, where an
    action is one of ('fill', i), ('empty', i), ('pour', i, j), where
    i and j are indices indicating the glass number."""
    # your code here
    if goal > max(capacities):
      return []
    return shortest_path_search(start or (0,)*len(capacities), 
      Successors(capacities), lambda s: goal in s)

class Successors(object):
  def __init__(self, capacities):
    self.capacities = capacities
    self._pos = range(len(capacities))

  def __call__(self, state):
    return dict(self.pour(state, src, dest) for src in self._pos
                                            for dest in self._pos
                                            if self._canact(state, src, dest))

  def pour(self, state, src, dest):
    diff = [self._addend(state, src, dest)(i) for i in self._pos]
    if src != dest:
      return tuple(map(add, state, diff)), ('pour', src, dest)
    else:
      op, action = (add, 'fill') if state[src] == 0 else (sub, 'empty')
      return tuple(map(op, state, diff)), (action, src)

  def _addend(self, state, src, dest):
    if src == dest:
      amount = self.capacities[src]
    else:
      amount = min(state[src], self.capacities[dest] - state[dest])
    return lambda i: amount if i == dest else \
                    -amount if i == src else 0

  def _canact(self, state, src, dest):
    if src == dest:
      return state[src] in (0, self.capacities[src])
    return state[src] > 0 and state[dest] < self.capacities[dest]

    
def shortest_path_search(start,successors,is_goal):
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
