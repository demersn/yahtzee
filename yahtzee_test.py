import numpy as np
from upper_card import ya_upper
from lower_card import ya_lower_score
from lower_card import ya_lower_find
from comparison import comparison_upper


# roll = np.random.randint(1, 7, 5)
roll = np.array([2, 3, 4, 5, 6])
print(roll)

number = 6
upper_score = ya_upper(roll, number)
print(upper_score)


lower_score_find = ya_lower_find(roll)
print(lower_score_find)

l_card = [0, 0, 0, 0, 0, 1, 0, 0, 0, 0, 0, 0, 0]
# print(l_cardnp.argmax(l_card) != 0)
score = [1, 1, 1, 1, 1, 0]
print(comparison_upper(roll, score))
# Git