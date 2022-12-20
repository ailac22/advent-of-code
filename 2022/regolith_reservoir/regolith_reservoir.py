from itertools import pairwise, zip_longest

c = 200
r = 200
cave = [ ["."] * c for i in range(r) ]

with open('input.txt') as f:
    L = [ list(map(eval,x.strip().split(' -> '))) for x in f.readlines()]

    for x in L:
        for x,y in pairwise(x):
            print(x,y)

            ranges = [ range(x[0],x[1],1 if x[1]-x[0] >= 0 else -1) for x in zip(x,y)]
            fv = y[0] if len(ranges[0]) == 0 else y[1]

            for a in zip_longest(*ranges, fillvalue=fv):
                print("cave rock!")
                cave[a[1]][a[0]-400] = 'o'
                # for z in zip(b,a):
                #     print(z)

    for x in cave:
        for y in x:
            print(y,sep='',end='')
        print("\n")
