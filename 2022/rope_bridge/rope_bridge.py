

H = (0,0)
H_prev = (0,0)
T = (0,0)

rope = [(0,0)]*9
print(f"rope:{rope}")
T_positions = set() 

def vector_sum(a,b):
    import operator
    return tuple(map(operator.add, a, b))

def vector_sub(a,b):
    import operator
    return tuple(map(operator.sub, a, b))

def tightRope(a,b):
    distance = vector_sub(a,b)
    return distance[0] > 1 or distance[1] > 1 or distance[0] < -1 or distance[1] < -1 

def moveH(mymov):
    global H
    global H_prev
    global T

    for _ in range(mymov[2]):
        H_prev = H
        H = vector_sum(H,mymov[:2])
        if tightRope(H,T):
            T = H_prev
            T_positions.add(T)
        
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

with open('input.txt','r') as f:
    L = [ (x.split()[0], int(x.split()[1])) for x in f.read().strip().split('\n')]
    
    for move in L:
        transMov = transfMov(move)
        moveH(transMov)

    print(len(T_positions))

