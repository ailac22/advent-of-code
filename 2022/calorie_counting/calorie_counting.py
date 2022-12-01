import itertools

def parse_input(f):
    lines = f.read().split("\n")
    return [int(x) if x.isdigit() else 0 for x in lines ]

def find_elf(input_list):
    L = [list(g) for _, g in itertools.groupby(input_list, key=lambda x: x == 0)]
    return max([sum(x) for x in L if x])

with open("input.txt","r") as f:
    L = parse_input(f) 
    print(find_elf(L))
