import numpy as np
# from upper_card import ya_upper_score
from upper_card import ya_upper
from lower_card import ya_lower
from lower_card import ya_lower_find
from reroll import reroll_1

n_dices = 5
# roll = np.random.randint(1, 7, n_dices)
roll = np.array([2, 3, 4, 5, 5])
print(roll)


# l_card = [0, 0, 0, 0, 0, 1, 0, 0, 0, 0, 0, 0, 0]
# print(l_cardnp.argmax(l_card) != 0)
score_u = [0, 0, 0, 0, 0, 0]
score_l = [0, 0, 0, 0, 0, 0, 0]
print(ya_upper(roll, score_u))

lower_score_find = ya_lower_find(roll, score_l)
print(lower_score_find)
low = ya_lower(roll, score_l)

up, low, choice = reroll(roll, score_u)
print(low)
print(choice)

