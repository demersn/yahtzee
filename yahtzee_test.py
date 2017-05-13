import numpy as np
# from upper_card import ya_upper_score
from upper_card import ya_upper
from lower_card import ya_lower
from lower_card import ya_lower_find

n_dices = 5
# roll = np.random.randint(1, 7, n_dices)
roll = np.array([2, 3, 4, 5, 5])
print(roll)


def reroll(roll, score):  # Possibilities when rerolling ONE dice
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

