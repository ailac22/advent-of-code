key_cycles = [20, 60, 100, 140, 180, 220]
current_cycle = 1
X_register = 1
X_values_over_t = []

def add_instruction(inst):
    global X_register
    print(f"adding {inst[1]} in cycle {current_cycle}")
    X_register += int(inst[1])

def dot(K, L): # from stackoverflow
   if len(K) != len(L):
      return 0

   return sum(i[0] * i[1] for i in zip(K, L))

def registerIfKeyCycle():
    if current_cycle in key_cycles: 
        print(f"adding {X_register} to values")
        X_values_over_t.append(X_register)

def execute_instruction(inst):
    global current_cycle
    match inst[0]:
        case 'noop':
            print('pass')
            # pass
        case 'addx':
            current_cycle += 1
            registerIfKeyCycle()
            add_instruction(inst)
    
    current_cycle += 1
    

with open('input.txt') as f:
    L = [x.strip().split() for x in f.readlines()]

    for inst in L:
        registerIfKeyCycle()
        execute_instruction(inst)

    print(key_cycles)
    print(X_values_over_t)
    print(dot(key_cycles,X_values_over_t))
