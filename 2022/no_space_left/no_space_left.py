# nombre,size,parent, subnodos
fs = {'name':'/','size':0,'parent':None,'children': []}
cwd = fs  


def printDir(dir, tabs = '\t'):
    print(f"{tabs}name: {dir['name']}, size: {dir['size']}")
    if dir['children'] != None:
        print(f"{tabs}and children are:\n")
        for x in dir['children']:
            printDir(x, tabs + '\t')

def parse(cmds):
    global cwd
    for cmd in cmds:
        spl_cmd = cmd.split()
        if 'cd' in spl_cmd:
            cwd = cd(spl_cmd, cwd)
        elif 'ls' in spl_cmd:
            pass
        elif 'dir' in spl_cmd:
            mkdir(spl_cmd)
        else: 
            touch(cmd.split())

def cd(cmd, cwd):
    if cmd[2] == '/':
        cwd = fs
    elif cmd[2] == '..':
        cwd = cwd['parent']
    else:
        cwd = list(filter(lambda x: cmd[2] == x['name'], cwd['children']))[0]
    return cwd

def touch(file):
   elem = {'name': file[1],'size': int(file[0]),'parent':cwd, 'children':None}
   cwd['children'].append(elem)

def mkdir(cmd):
    dir = {'name':cmd[1],'size':0, 'parent':cwd, 'children':[]}
    cwd['children'].append(dir)

def findDirSize(dir):
    total = 0
    for file in dir['children']:
        if file['children'] != None:
            total += findDirSize(file)
        else:
            total += file['size']
    return total;

def findDirSizes(dir):
    allDirSizes = []
    for file in dir['children']:
        if file['children'] != None:
            allDirSizes.extend(findDirSizes(file))

    allDirSizes.append(findDirSize(dir))

    return allDirSizes


with open('input.txt', 'r') as f:
    cmds = f.read().strip().split('\n')
    parse(cmds)
    # printDir(fs)
    lista_orig = findDirSizes(fs)
    lista = list(filter(lambda x: x<= 100000,lista_orig))
    print(f"First result {sum(lista)}")

    lista = list(filter(lambda x: x> 6975962,lista_orig))
    lista.sort(reverse=True)
    
    print(f"Second result {min(lista)}")
