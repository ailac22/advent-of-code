import functools

def getItemPriorityValue(item):
    if item.isupper():
        return ord(item) - 65 + 27
    else:
        return ord(item) - 96

def getRepeatedItem(s):
    s2 = [ set(x) for x in s ]
    item_set = functools.reduce(lambda out, el: out.intersection(el), s2)
    return list(item_set)[0]

def divideInChunks(list,chunk_size):
    return [list[i:i+chunk_size] for i in range(0, len(list), chunk_size)] 

def getPriority(rucksack):
    h = divideInChunks(rucksack,len(rucksack) // 2)
    duplicate_item = getRepeatedItem(h)
    return getItemPriorityValue(duplicate_item)

def findPriorityInGroup(group):
    repeated_item = getRepeatedItem(group)
    return getItemPriorityValue(repeated_item)

def findBadgePriorities(list):
    groups = divideInChunks(list, 3)
    return sum(map(findPriorityInGroup,groups))


with open('input.txt','r') as f:
    L = f.read().split()
    res = sum(map(getPriority,L))

    res2 = findBadgePriorities(L)
    print(res2)



