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

    if not (np[0] <= len(hill[0]) - 1 and np[0] >= 0 and np[1] <= len(hill) - 1 and np[1] >= 0):
        return False

    print(f"cp {cp}")
    print(f"np {np}")
    print(hill[cp[1]][cp[0]])
    print(hill[np[1]][np[0]])

    print(f"len hill {len(hill[0]) - 1}")
    print(f"len hill {len(hill) - 1}")

    cl = hill[cp[1]][cp[0]] 
    cl = cl if cl != 'S' else 'a'
    nl = hill[np[1]][np[0]]
    nl = nl if nl != 'E' else 'z'

    return ascii_letters.index(cl) + 1 >= ascii_letters.index(nl) 

def eagerHeur(cp):
    global E
    dist = vector_sub(E,cp)
    return abs(dist[0])+abs(dist[1])

# algorithm adapted from https://www.pythonpool.com/a-star-algorithm-python/

def get_neighbors(v):
    return list(filter(lambda x: canGo(v,x,hill), map(lambda x: vector_sum(v,x),[(1,0), (-1,0), (0,1), (0,-1)])))

# This is heuristic function which is having equal values for all nodes
def h( n):
    return eagerHeur(n)

def a_star_algorithm(start, stop):
    # In this open_lst is a lisy of nodes which have been visited, but who's 
    # neighbours haven't all been always inspected, It starts off with the start 
#node
    # And closed_lst is a list of nodes which have been visited
    # and who's neighbors have been always inspected
    open_lst = set([start])
    closed_lst = set([])

    # poo has present distances from start to all other nodes
    # the default value is +infinity
    poo = {}
    poo[start] = 0

    # par contains an adjac mapping of all nodes
    par = {}
    par[start] = start

    while len(open_lst) > 0:
        n = None

        # it will find a node with the lowest value of f() -
        for v in open_lst:
            if n == None or poo[v] + h(v) < poo[n] + h(n):
                n = v;

        if n == None:
            print('Path does not exist!')
            return None

        # if the current node is the stop
        # then we start again from start
        if n == stop:
            reconst_path = []

            while par[n] != n:
                reconst_path.append(n)
                n = par[n]

            reconst_path.append(start)

            reconst_path.reverse()

            print('Path found: {}'.format(reconst_path))
            print(len(reconst_path)-1)
            return reconst_path

        # for all the neighbors of the current node do
        for m in get_neighbors(n):
            weight = 1
          # if the current node is not presentin both open_lst and closed_lst
            # add it to open_lst and note n as it's par
            if m not in open_lst and m not in closed_lst:
                open_lst.add(m)
                par[m] = n
                poo[m] = poo[n] + weight

            # otherwise, check if it's quicker to first visit n, then m
            # and if it is, update par data and poo data
            # and if the node was in the closed_lst, move it to open_lst
            else:
                if poo[m] > poo[n] + weight:
                    poo[m] = poo[n] + weight
                    par[m] = n

                    if m in closed_lst:
                        closed_lst.remove(m)
                        open_lst.add(m)

        # remove n from the open_lst, and add it to closed_lst
        # because all of his neighbors were inspected
        open_lst.remove(n)
        closed_lst.add(n)

    print('Path does not exist!')
    return None

# def advance(cp,steps,best,hill,visited):
#     
#     time.sleep(0.5)
#     print(visited)
#     if cp == E:
#         print("OJO")
#         exit(1)
#     print("in ",cp, " -- ", hill[cp[1]][cp[0]])
#     if cp not in visited:
#         visited.add(cp)
#     else:
#         return best

#     if steps > best:
#         return best

#     if hill[cp[1]][cp[0]] == 'E':
#         # print(visited)
#         return min(best,steps)

#     possibleNext = list(filter(canGo,map(lambda x: vector_sum(cp,x),[(1,0), (-1,0), (0,1), (0,-1)])))

#     possibleNext.sort(key=eagerHeur)
#     
#     print('-- possible next -- ')
#     for x in possibleNext:
#         print(hill[x[1]][x[0]], "(",x,")",end=",")

#     print("\n")
#     for np in possibleNext:
#         # print("manhattan: ", manhattanHeuristic(np))
#         if canGo(cp,np,hill):
#             best = min(best,advance(np, steps + 1, best, hill,visited))


#     visited.discard(cp)
#     return best


with open('input.txt') as f:
    hill = [x.strip() for x in f.readlines()]

    
    for i,x in enumerate(hill):
        print(i, x)

    visited = set() 
    reconst_path = a_star_algorithm(S,E)
    
    # part 2
    # for j in range(len(hill)):
    #     for i in range(len(hill[0])):
    #         if hill[]
    
    if reconst_path != None:
            for x in reconst_path:
                a = hill[x[1]] 
                hill[x[1]] = a[:x[0]] + '.' + a[x[0]+1:] 

    for x in hill:
        print(x)
    # print(advance(S,0,maxsize,hill,visited))
