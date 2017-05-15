# Calculate the lower card of a Yahtzee roll
import numpy as np


def ya_lower_find(roll, score):  # Find lower card possibilities from ROLL
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
        for jj in range(1, 7):  # Full House
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
    if sum(np.in1d(ss_1, roll)) == 4:  # Small Straight
        choice.append('ss')
        numbers.append(1)
    if sum(np.in1d(ss_2, roll)) == 4:
        choice.append('ss')
        numbers.append(2)
    if sum(np.in1d(ss_3, roll)) == 4:
        choice.append('ss')
        numbers.append(3)
    if sum(np.in1d(ls_1, roll)) == 5:  # Large Straight
        choice.append('ls')
        numbers.append(1)
    if sum(np.in1d(ls_2, roll)) == 5:
        choice.append('ls')
        numbers.append(2)
    if not choice:  # Choice is used as a last resort only
        choice.append('ch')
    return choice, numbers


# Calculates score from previous possibilities
def ya_lower_score(roll, choice):
    if choice == 'tok':
        pts = sum(roll)
    elif choice == 'fok':
        pts = sum(roll)
    elif choice == 'fh':
        pts = 25
    elif choice == 'ss':
        pts = 30
    elif choice == 'ls':
        pts = 40
    elif choice == 'ya':
        pts = 50
    elif choice == 'ch':
        pts = sum(roll)
    else:
        pts = 0
    return pts


# Returns the potiential score and category, NOT considering the card
def ya_lower(roll, card):
    choice = np.array(ya_lower_find(roll, card)[0])
    pot_score_l = np.zeros(len(choice))
    # pot_choice_l = np.zeros(len(choice))
    if len(card) == 0:
        pot_score_l = [0]
    for ii in range(len(choice)):
        pot_score_l[ii] = ya_lower_score(roll, choice[ii])
    pot_score_l = np.array(pot_score_l)
    pot_l = zip(pot_score_l, choice)  # zip here returns a list of list of list
    return pot_l


# Returns the potiential score and category, considering the card
def ya_lower2(roll, card):
    choice = np.array(ya_lower_find(roll, card)[0])
    pot_score_l = np.zeros(len(choice))
    # pot_choice_l = np.zeros(len(choice))
    if len(card) == 0:
        pot_score_l = [0]
    for ii in range(len(choice)):
        pot_score_l[ii] = ya_lower_score(roll, choice[ii])
    pot_score_l = np.array(pot_score_l)
    zzip = list(zip(pot_score_l, choice))  # zip here returns a list of list of list
    pot_lt = zzip[:]
    pot_l = pot_lt
#    print(pot_l)
    for jj in range(len(pot_l)):  # We remove choices if card is already full
        cat = pot_l[jj][1]
#        print(cat)
#        print(type(cat))
        is_match = [s for s in card if cat in s]
#        print(is_match)
        if is_match[0][1] != 0:
            pot_l[jj] = []
    return pot_l
