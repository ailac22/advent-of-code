def vector_sum(a,b):
    import operator
    return tuple(map(operator.add, a, b))

def vector_sub(a,b):
    import operator
    return tuple(map(operator.sub, a, b))

def tight_knot(a,b):
    distance = vector_sub(a,b)
    return distance[0] > 1 or distance[1] > 1 or distance[0] < -1 or distance[1] < -1 

def displacement_dir(a,b):
    dist = vector_sub(a,b)
    return (max(-1, min(1, dist[0])),max(-1, min(1, dist[1])))

def move_rope(mymov, rope, t_positions):
    for _ in range(mymov[2]):
        rope[0] = vector_sum(rope[0],mymov[:2])
        for i in range(1,len(rope)):
            if tight_knot(rope[i],rope[i-1]):
                rope[i] = vector_sum(rope[i],displacement_dir(rope[i-1],rope[i]))
        t_positions.add(rope[-1])
        
    
def transfMov(origMov):
    times = origMov[1]

    match origMov[0]:
        case 'R':
            return (1,0,times)
        case 'U':
            return (0,1,times)
        case 'L':
            return (-1,0,times)
        case 'D':
            return (0,-1,times)

def getTailPositions(L,rope,t_positions):
    for move in L:
        transMov = transfMov(move)
        move_rope(transMov,rope,t_positions)
    return t_positions

with open('input.txt','r') as f:
    L = [ (x.split()[0], int(x.split()[1])) for x in f.read().strip().split('\n')]

    rope1 = [(int(0),int(0))]*2
    rope2 = [(int(0),int(0))]*10

    t_positions_1 = set() 
    t_positions_2 = set() 

    print(f"First solution: {len(getTailPositions(L,rope1,t_positions_1))}")
    print(f"Second solution: {len(getTailPositions(L,rope2,t_positions_2))}")
