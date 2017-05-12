# Calculate the lower card of a Yahtzee roll
import numpy as np


def ya_lower_find(roll):
    choice = []
    numbers = []
    for ii in range(1, 7):
        if np.count_nonzero(roll == ii) == 3:  # Three of a kind
            choice.append('tok')
            numbers.append(ii)
        elif np.count_nonzero(roll == ii) == 4:  # Four of a kind
            choice.append('fok')
            numbers.append(ii)
        elif np.count_nonzero(roll == ii) == 5:  # Yahtzee
            choice.append('ya')
            numbers.append(ii)
        for jj in range(1, 7):
            if ii != jj:
                if (np.count_nonzero(roll == ii) == 3
                   and np.count_nonzero(roll == jj) == 2):
                    choice.append('fh')
                    numbers.append(ii)
    ss_1 = [1, 2, 3, 4]
    ss_2 = [2, 3, 4, 5]
    ss_3 = [3, 4, 5, 6]
    ls_1 = [1, 2, 3, 4, 5]
    ls_2 = [2, 3, 4, 5, 6]
    if sum(np.in1d(ss_1, roll)) == 4:
        choice.append('ss')
        numbers.append(1)
    if sum(np.in1d(ss_2, roll)) == 4:
        choice.append('ss')
        numbers.append(2)
    if sum(np.in1d(ss_3, roll)) == 4:
        choice.append('ss')
        numbers.append(3)
    if sum(np.in1d(ls_1, roll)) == 5:
        choice.append('ls')
        numbers.append(1)
    if sum(np.in1d(ls_2, roll)) == 5:
        choice.append('ls')
        numbers.append(2)

    # if 3 in roll is True and 4 in roll is True:  # Small Straight
    #     if 1 in roll is True and 2 in roll is True:
    #         choice.append('ss')
    #         numbers.append(1)
    #     elif 2 in roll is True and 5 in roll is True:
    #         choice.append('ss')
    #         numbers.append(2)
    #     elif 5 in roll is True and 6 in roll is True:
    #         choice.append('ss')
    #         numbers.append(3)
    # elif 2 in roll is True and 3 in roll is True and 4 in roll is True:  # Large Straight
    #     if 1 in roll is True:
    #         choice.append('ls')
    #         numbers.append(1)
    #     elif 2 in roll is True:
    #         choice.append('ls')
    #         numbers.append(2)

    return choice, numbers


def ya_lower_score(roll, choice):
    if choice == 'tok':
        score = sum(roll)
    elif choice == 'fok':
        score = sum(roll)
    elif choice == 'fh':
        score = 25
    elif choice == 'ss':
        score = 30
    elif choice == 'ls':
        score = 40
    elif choice == 'ya':
        score = 50
    elif choice == 'ch':
        score = sum(roll)
    return score
