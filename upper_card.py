# Calculate the upper card of a Yahtzee roll
import numpy as np


def ya_upper_score(roll, number):
    result = np.count_nonzero(roll == number)
    return result*number


def ya_upper(roll, card):
    pot_score_u = np.zeros(6)
    pot_index_u = 0
    for ii in range(1, 7):
        pot_score_u[ii-1] = ya_upper_score(roll, ii)
    while pot_index_u == 0:
        if card[np.argmax(pot_score_u)] == 0:
            # print(score[np.argmax(pot_score_u)])
            pot_index_u = np.argmax(pot_score_u)
        elif sum(pot_score_u) == 0:
            pot_index_u = ''
        else:
            pot_score_u[np.argmax(pot_score_u)] = 0
    return pot_score_u, pot_index_u
