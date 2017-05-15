# Reroll ONE dice
import numpy as np
from upper_card import ya_upper
from lower_card import ya_lower2
from lower_card import ya_lower_find


def reroll_1(roll, card_u, card_l):  # Possibilities when rerolling ONE dice
    up = []
    low = []
    # choice = []
    for dice in range(len(roll)):
        for n in range(1, 7):
            temp_roll = np.array(roll)
            temp_roll[dice] = n
            # print(temp_roll)
            up.append(ya_upper(temp_roll, card_u))
            low.append(ya_lower2(temp_roll, card_l))  # ya_lower2 to get card influence
            # choice.append(ya_lower_find(temp_roll, card)[0])
    # low = np.array(low)
    return up, low  # , choice
