# Reroll ONE dice
import numpy as np
from upper_card import ya_upper
from lower_card import ya_lower
from lower_card import ya_lower_find


def reroll_1(roll, card):  # Possibilities when rerolling ONE dice
    up = []
    low = []
    choice = []
    for dice in range(len(roll)):
        for n in range(1, 7):
            temp_roll = np.array(roll)
            temp_roll[dice] = n
            # print(temp_roll)
            up.append(ya_upper(temp_roll, card))
            low.append(ya_lower(temp_roll, card))
            choice.append(ya_lower_find(temp_roll, card)[0])
    # low = np.array(low)
    return up, low, choice
