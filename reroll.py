# Reroll ONE dice
import numpy as np


def reroll_1(roll, score):  # Possibilities when rerolling ONE dice
    up = []
    low = []
    choice = []
    for dice in range(len(roll)):
        for n in range(1, 7):
            temp_roll = np.array(roll)
            temp_roll[dice] = n
            # print(temp_roll)
            up.append(ya_upper(temp_roll, score))
            low.append(ya_lower(temp_roll, score))
            choice.append(ya_lower_find(temp_roll, score)[0])
    # low = np.array(low)
    return up, low, choice
