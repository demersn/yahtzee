# Calculate the upper card of a Yahtzee roll
import numpy as np


def ya_upper(roll, number):
    result = np.count_nonzero(roll == number)
    return result*number
