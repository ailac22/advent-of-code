import numpy as np
import time

def my_normalize(la,lb):
    if type(la) == int and type(lb) == list:
        la,lb = [la],lb
    if type(la) == list and type(lb) == list:
        for i in range(len(la)):
            if (len(lb) > i):
                la[i],lb[i] = my_normalize(la[i],lb[i])
    return la,lb



with open('input.txt') as f:

    L = [ list(map(eval, x.split('\n') )) for x in f.read().strip().split('\n\n') ]

    correct_indexes = []
    for i in range(len(L)):
        l = L[i][0]
        r = L[i][1]
        l,r = my_normalize(l,r)
        r,l = my_normalize(r,l)
        if l < r:
            correct_indexes.append(i+1)

    print("First result: ", sum(correct_indexes))
