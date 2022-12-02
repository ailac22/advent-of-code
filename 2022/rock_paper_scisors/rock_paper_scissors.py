import itertools

# Rock: A X
# Paper: B Y
# Scissors: C Z

rpsValue = {'X':1, 'Y':2, 'Z': 3}
wdlValue = [6,3,0]
rpsWC = {'A': 'Z', 'B': 'X', 'C': 'Y', 'X':'C', 'Y': 'A', 'Z': 'B'}

def play_round(game):
    if len(game) < 2: return 0;
    roundOutcome = rpsValue[game[1]] 
    if rpsWC[game[0]] == game[1]:
        roundOutcome = roundOutcome + wdlValue[2]
    elif rpsWC[game[1]] == game[0]:
        roundOutcome = roundOutcome + wdlValue[0]
    else:
        roundOutcome = roundOutcome + wdlValue[1]
    return roundOutcome 


with open("input.txt") as f:
    L = [x.split(" ") for x in f.read().split("\n")]

    print(L)
    res = sum(map(play_round,L))
    print(res)
