# Decisions criterias for Yahtzee
import numpy as np

from upper_card import ya_upper
# from lower_card import ya_lower


def comparison_upper(roll, score):
    pot_score_u = np.zeros(6)
    pot_index_u = 0
    for ii in range(1, 7):
        pot_score_u[ii-1] = ya_upper(roll, ii)
    while pot_index_u == 0:
        if score[np.argmax(pot_score_u)] == 0:
            # print(score[np.argmax(pot_score_u)])
            pot_index_u = np.argmax(pot_score_u)
        elif sum(pot_score_u) == 0:
            pot_index_u = ''
        else:
            pot_score_u[np.argmax(pot_score_u)] = 0
    return pot_score_u, pot_index_u


# def comparison_lower(roll, score):
