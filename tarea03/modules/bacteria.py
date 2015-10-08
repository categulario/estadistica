#
# If you want to optimize, be the bacteria
#
import numpy as np
from random import random

def random_direction(size):
    # Create a random direction
    start_direction = np.array([random()*2-1 for i in range(size)])

    # Normalize
    start_direction /= np.linalg.norm(start_direction)

    return start_direction

def bacteria(function, position, max_iterations=1000):
    """
    The idea is simple, if things are going well, keep going in that direction,
    else randomize
    """
    # Create a random direction for the bacteria
    direction = random_direction(len(position))
    # Start with zero iterations
    iterations = 0
    # start from minus infinity
    value = function(position)
    print('start value: ', value)

    # The main loop
    while iterations < max_iterations:
        # take a step in direction
        next_position = position + direction
        next_value    = function(next_position)

        if next_value > value:
            # things are going well
            position = next_position
            value    = next_value
            print('got new position with value ', value)
        else:
            # things are getting worse, randomize
            direction = random_direction(len(position))

        iterations += 1
    return position
