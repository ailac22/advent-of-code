import re
import itertools

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

# def move_with_CrateMover_9000()

def do_orders(orders,crates):
    for order in orders:
        for i in itertools.repeat(None, order[0]):
            crates[order[2]-1].append(crates[order[1]-1].pop())

    return crates

with open('input.txt','r') as f:
    
    L = f.readlines()
    crates_info = L[0:8]
    orders_info = L[10:]
    crates = parse_crates(crates_info)
    # print(crates)
    orders = parse_input(orders_info)
    
    crates = do_orders(orders,crates)
    first_result = "".join([ x[-1] for x in crates])
    print(f"First result: {first_result}")

