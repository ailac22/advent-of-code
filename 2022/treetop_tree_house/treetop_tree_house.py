def isEdge(i,j,forest):
    return i == 0 or i == len(forest[0])-1 or j == 0 or j == len(forest[0])-1

def isVisible(i,j,forest):
    if isEdge(i,j,forest):
        return True

    forest_zip = list(zip(*forest))
    tree = forest[j][i]

    a = all(map(lambda x: int(x) < int(tree),forest[j][:i]))
    b = all(map(lambda x: int(x) < int(tree),forest[j][i+1:]))
    c = all(map(lambda x: int(x) < int(tree),forest_zip[i][:j]))
    d = all(map(lambda x: int(x) < int(tree),forest_zip[i][j+1:]))
    return a or b or c or d

def treeScene(lst,tree):
    for i,v in enumerate(lst):
        if int(v) >= int(tree):
            return len(lst[:i+1])
    return len(lst)

def find_scenic_score(i,j,forest):

    forest_zip = list(zip(*forest))
    tree = forest[j][i]

    a = treeScene(list(reversed(forest[j][:i])),tree)
    b = treeScene(list(forest[j][i+1:]),tree)
    c = treeScene(list(reversed(forest_zip[i][:j])),tree)
    d = treeScene(list(forest_zip[i][j+1:]),tree)

    return a*b*c*d

with open('input.txt','r') as f:
    forest = [list(x.strip()) for x in f.readlines()]

    acc = 0
    scenicScores = []
    for j in range(len(forest)):
        for i in range(len(forest[0])):
            # print(f"checking {forest[j][i]}, {i},{j}")
            scenicScores.append(find_scenic_score(i,j,forest))
            if isVisible(i,j,forest):
                
                acc += 1

    print(f"First result {acc}")
    print(f"Second result: {max(scenicScores)}")


