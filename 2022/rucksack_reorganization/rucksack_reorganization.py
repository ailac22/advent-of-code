
def getItemPriorityValue(item):
    if item.isupper():
        return ord(item) - 65 + 27
    else:
        return ord(item) - 96

def getPriority(rucksack):
    half_length = len(rucksack) // 2

    hl1 = set(rucksack[:half_length])
    hl2 = set(rucksack[half_length:])
    duplicate_item_set = hl1.intersection(hl2)

    duplicate_item = list(duplicate_item_set)[0]

    return getItemPriorityValue(duplicate_item)

def findBadgeInGroup(list):
    pass

def findBadgePriorities(list):
    chunk_size = 3
    chunked_list = [L[i:i+chunk_size] for i in range(0, len(L), chunk_size)]

    print(chunked_list)


with open('input.txt','r') as f:
    L = f.read().split()
# set(L[:len(L/2)])
    res = sum(map(getPriority,L))

    findBadgePriorities(L)
    # res2 = sum(map(findBadgePriorities,L))

    print(res)

        # L2 = [  1  ,  set(L[half_length:])] ##  ] for x in L]

