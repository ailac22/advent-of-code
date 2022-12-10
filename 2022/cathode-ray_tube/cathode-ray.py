key_cycles = [20, 60, 100, 140, 180, 220]
current_cycle = 1
X_register = 1
X_values_over_t = []
screen = [ ['.'] * 40 for _ in range(6) ]

def render_sprite(x_register,current_cycle):
    global screen
    screen_width = len(screen[0])

    h_index = (current_cycle - 1) % screen_width
    v_index = (current_cycle - 1) // screen_width
    if h_index in [x_register, x_register+1,x_register-1]:
        screen[v_index][h_index] = '#'

def print_screen(screen):
    for x in screen:
        print(x)

def add_instruction(inst):
    global X_register
    X_register += int(inst[1])

def dot(K, L): # dot is from stackoverflow (dot product)
   if len(K) != len(L):
      return 0

   return sum(i[0] * i[1] for i in zip(K, L))

def registerIfKeyCycle():
    if current_cycle in key_cycles: 
        X_values_over_t.append(X_register)

def execute_instruction(inst):
    global current_cycle
    global X_register
    match inst[0]:
        case 'noop':
            pass
        case 'addx':
            current_cycle += 1
            registerIfKeyCycle()
            render_sprite(X_register, current_cycle)
            add_instruction(inst)
    
    current_cycle += 1
    

with open('input.txt') as f:
    L = [x.strip().split() for x in f.readlines()]

    for inst in L:
        render_sprite(X_register, current_cycle)
        registerIfKeyCycle()
        execute_instruction(inst)
        assert X_register < 40

    print(f"First result: {dot(key_cycles,X_values_over_t)}")

    print("Print of second result:")
    print_screen(screen)
