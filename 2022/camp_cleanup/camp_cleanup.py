
with open('input.txt','r') as f:
    #La = [x.split(',') for x in f.read().strip().split('\n')]
    La = [[x.split('-'),y.split('-')] for [x,y] in [y.split(',') for y in f.read().strip().split('\n')]] 

    print(La)
    sum = 0
    for pair in La:
        print(f"pair {pair}")
        ranges = []
        for elf in pair:
            ranges.append(set(range(int(elf[0]),int(elf[1])+1)))
        print(f"ranges{ranges}")
        if ranges[0].issuperset(ranges[1]) or ranges[1].issuperset(ranges[0]):
            sum += 1

    print(sum)

    # L = [y.split('-') for y in La]


    # print(L)
