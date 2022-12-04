

def fully_contained(ranges):
    return ranges[0].issuperset(ranges[1]) or ranges[1].issuperset(ranges[0])

def overlap_at_all(ranges):
    return len(ranges[0] & (ranges[1])) > 0

def check_overlaps(pairs,check_method):
    sum = 0
    for pair in pairs: 
        ranges = []
        for elf in pair:
            ranges.append(set(range(int(elf[0]),int(elf[1])+1)))
        if check_method(ranges):
            sum += 1

    return sum

with open('input.txt','r') as f:
    La = [[x.split('-'),y.split('-')] for [x,y] in [y.split(',') for y in f.read().strip().split('\n')]] 

    print(f"First result {check_overlaps(La,fully_contained)}")

    print(f"Second result {check_overlaps(La,overlap_at_all)}")
