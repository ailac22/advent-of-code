import copy 
from functools import cmp_to_key
import itertools

def my_normalize(la,lb):
    if type(la) == int and type(lb) == list:
        la,lb = [la],lb
    if type(la) == list and type(lb) == list:
        for i in range(len(la)):
            if (len(lb) > i):
                la[i],lb[i] = my_normalize(la[i],lb[i])
    return la,lb

def compare(l,r):
    ml,mr = copy.deepcopy(l),copy.deepcopy(r)
    ml,mr = my_normalize(ml,mr)
    mr,ml = my_normalize(mr,ml)
    if ml < mr: return 1
    elif ml == mr: return 0
    else: return -1

with open('input.txt') as f:

    L = [ list(map(eval, x.split('\n') )) for x in f.read().strip().split('\n\n') ]

    correct_indexes = []
    for i,(l,r) in enumerate(L):
        if compare(l,r) == 1:
            correct_indexes.append(i+1)

    print("First result:", sum(correct_indexes))

    L2 = list(itertools.chain(*L))

    divider_1,divider_2 = [[2]],[[6]]
    
    L2.append(divider_1)
    L2.append(divider_2)

    L2.sort(key=cmp_to_key(compare))
    print("Second result:", L2.index(divider_1) * L2.index(divider_2))
