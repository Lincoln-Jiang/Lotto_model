import numpy as np 
import math
import random

ball_max = 49
choose_n = 7


def nCr(n,r):
    f = math.factorial
    return f(n) / f(r) / f(n-r)

def get_prob(ball_max, choose_n):
    prob_dict ={}
    base = nCr(ball_max, choose_n)
    
    # t1 =0
    for i in list(range(0,choose_n + 1)):
        t = nCr(choose_n, i) * nCr(ball_max-choose_n, choose_n - i)/base
        prob_dict[str(i)] = t
        # t1 += t
    return prob_dict

# print(get_prob(49,7))

def get_winning_number(round):
    n_keep = 0
    keep_list = []
    for i in range(1, round + 1):
        pop = list(range(0, choose_n - n_keep + 1))
        weight = get_prob(49-(i-1)*7, 7 - n_keep).values()
        print(weight)
        print(len(weight))
        number = random.choices(pop, weights = list(weight))[0]
        n_keep += number
        keep_list.append(number)
    return keep_list, n_keep

# print(get_winning_number(4))
def simple_play(n_ticket, ball_max, choose_n):

    keep_list, _ = get_winning_number(n_ticket)
    all_number = list(range(1, ball_max + 1))
    ticket_list = []
    # remove_list = []
    keep_number = []
    for i in range(1, n_ticket + 1):   
        ticket = np.random.choice(all_number, choose_n - len(keep_number), replace = False)
        ticket = list(np.sort(np.append(ticket, keep_number)))
        ticket_list.append(ticket)

        keep_1 = list(np.random.choice(ticket, keep_list[i-1], replace = False))
        keep_number.extend(keep_1)

        all_number = [x for x in all_number if x not in ticket]
        
    return ticket_list, keep_number

print(simple_play(3,49,7))