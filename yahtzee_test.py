import numpy as np
# from upper_card import ya_upper_score
from upper_card import ya_upper
# from lower_card import ya_lower
from lower_card import ya_lower2
from lower_card import ya_lower_find
from reroll import reroll_1

n_dices = 5
# roll = np.random.randint(1, 7, n_dices)
roll = np.array([2, 3, 4, 5, 6])
print(roll)


# card_u = [0, 0, 0, 0, 1, 0]
card_uu = [['1 -', 0], ['2 -', 0], ['3 -', 0],
           ['4 -', 0], ['5 -', 0], ['6 -', 0]]
# card_l = [0, 0, 0, 0, 0, 0, 0]
card_ll = [['tok', 0], ['fok', 0], ['fh', 0],
           ['ss', 1], ['ls', 0], ['ya', 0], ['ch', 0]]
# print(ya_upper(roll, card_uu))


pot_l = ya_lower2(roll, card_ll)
print(pot_l)
up, low = reroll_1(roll, card_uu, card_ll)
print(up)
print(low)

