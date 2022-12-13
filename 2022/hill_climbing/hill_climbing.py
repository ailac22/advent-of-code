from string import ascii_letters 
from sys import maxsize
import time

def vector_sum(a,b):
    import operator
    return tuple(map(operator.add, a, b))

def vector_sub(a,b):
    import operator
    return tuple(map(operator.sub, a, b))

S = 0,20 # Hardcoded
E = 77,20

def canGo(cp,np,hill):

    cl = hill[cp[1]][cp[0]] 
    cl = cl if cl != 'S' else 'a'
    nl = hill[np[1]][np[0]]
    nl = nl if nl != 'E' else 'z'

    # print(f"probando {cp} & {np} ({cl} & {nl})")
    return (np[0] < len(hill[0]) and np[0] >= 1 and np[1] < len(hill) and np[1] >= 0) and \
            ascii_letters.index(cl) + 1 >= ascii_letters.index(nl) 

def eagerHeur(cp):
    global E
    # print("werwerfwf: ",abs(E[0]-cp[0])+abs(E[1]-cp[1]))
    dist = vector_sub(E,cp)
    return abs(dist[0])+abs(dist[1])

def advance(cp,steps,best,hill,visited):
    
    print(visited)
    if cp == E:
        print("OJO")
        exit(1)
    print("in ",cp, " -- ", hill[cp[1]][cp[0]])
    if cp not in visited:
        visited.add(cp)
    else:
        return best

    if steps > best:
        return best

    if hill[cp[1]][cp[0]] == 'E':
        # print(visited)
        return min(best,steps)

    possibleNext = list(map(lambda x: vector_sum(cp,x),[(1,0), (-1,0), (0,1), (0,-1)]))

    possibleNext.sort(key=eagerHeur)
    
    print('-- possible next -- ')
    for x in possibleNext:
        print(hill[x[1]][x[0]], "(",x,")",end=",")

    print("\n")
    for np in possibleNext:
        # print("manhattan: ", manhattanHeuristic(np))
        if canGo(cp,np,hill):
            best = min(best,advance(np, steps + 1, best, hill,visited))


    visited.discard(cp)
    return best


with open('input.txt') as f:
    hill = [x.strip() for x in f.readlines()]

    for i,x in enumerate(hill):
        print(i, x)

    visited = set() 
    print(advance(S,0,maxsize,hill,visited))
