import re
import itertools
import copy

def parse_crates(L):
    L = [ x.replace('\n','') for x in L]
    crates = []
    for crate in L:
        c1 = re.findall(r'(\w|\s{4})', crate)
        crates.append(c1)
    with_spaces = [list(reversed(x)) for x in zip(*crates)]
    return [ list(filter(lambda x: not x.isspace(), y)) for y in with_spaces]

def parse_input(L):
    L_orders = []
    for order in L:
        mo = re.search('move (\\d+) from (\\d) to (\\d)', order.strip())
        if mo:
            L_orders.append([int(x) for x in mo.groups()]) 
    return L_orders

def move_with_CrateMover_9000(fr,to,crates,times):
    for _ in itertools.repeat(None, times):
        crates[to].append(crates[fr].pop())

def move_with_CrateMover_9001(fr,to,crates,times):
    crates[to].extend(crates[fr][-times:])
    del crates[fr][-times:]

def do_orders(orders,crates,mover_crane):
    for order in orders:
        mover_crane(order[1]-1,order[2]-1,crates,order[0])
    return crates

def getResult(moved_crates):
    return "".join([ x[-1] for x in moved_crates if len(x)>0])

with open('input.txt','r') as f:
    
    L = f.readlines()
    crates_info = L[0:8]
    orders_info = L[10:]
    crates = parse_crates(crates_info)
    crates_2 = copy.deepcopy(crates)

    orders = parse_input(orders_info)
    
    crates = do_orders(orders,crates, move_with_CrateMover_9000)
    crates_2 = do_orders(orders,crates_2, move_with_CrateMover_9001)
    
    first_result = getResult(crates)
    second_result = getResult(crates_2)

    print(f"First result: {first_result}")
    print(f"Second result: {second_result}")

