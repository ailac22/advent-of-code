import itertools


rpsValue = {'A':1, 'B':2, 'C': 3}
rpsWC = {'A': 'C', 'B': 'A', 'C':'B' }
rpsLC = {val: key for (key, val) in rpsWC.items()}

def roundOutcome(game):

    wdlValue = [6,3,0]
    if rpsWC[game[0]] == game[1]:
        return wdlValue[2]
    elif rpsWC[game[1]] == game[0]:
        return  wdlValue[0]
    else:
        return wdlValue[1]

def play_round_strategy_1(game):
    equivalences = {'X': 'A', 'Y': 'B', 'Z': 'C'}
    # Rock: A X
    # Paper: B Y
    # Scissors: C Z
    #rpsWC = {'A': 'Z', 'B': 'X', 'C': 'Y', 'X':'C', 'Y': 'A', 'Z': 'B'}
    if len(game) < 2: return 0;
    transformed_game = game 
    transformed_game[1] = equivalences[game[1]]
    return roundOutcome(game) + rpsValue[game[1]] 


def play_round_strategy_2(game):
    
    # Rock: A 
    # Paper: B 
    # Scissors: C 
    # rpsNeed2Do = {'X': 2, 'Y':1, 'Z': 0}

    
    if len(game) < 2: return 0;
    selected = '?'
    print("game")
    print(game)
    if game[1] == 'X':
        selected = rpsWC[game[0]]
    elif game[1] == 'Z':
        selected = rpsLC[game[0]]
    else:
        selected = game[0]

    print("selected")
    print(selected)
    return rpsValue[selected] + roundOutcome([game[0],selected])

    # roundOutcome = rpsValue[game[1]] 
    # if rpsWC[game[1]] == 'X':
    #     roundOutcome += wdlValue[2]

with open("input.txt") as f:
    L = [x.split(" ") for x in f.read().split("\n")]

    print(L)
    # res1 = sum(map( play_round_strategy_1,L))
    # print(f"first strategy: {res1}")
    res2 = sum(map(play_round_strategy_2,L))
    print(f"second strategy: {res2}")
