from functools import partial
import operator

## I did not know solution to part 2 and I had to look it up (The mcm thing + modulus, I'm not quite good at math), so I did not include it here

rounds = 20
worry_decrease = 3

# no parsing today
monkeys = [{'items': [72, 97], 'worry_mult': partial(operator.mul,13), 'test': 19, 'throw_to': (5,6), 'processed_items': 0},
           {'items': [55, 70, 90, 74, 95], 'worry_mult': lambda x: x**2, 'test':7, 'throw_to': (5,0), 'processed_items': 0},
           {'items': [74, 97, 66, 57], 'worry_mult': partial(operator.add,6), 'test': 17, 'throw_to': (1,0), 'processed_items': 0},
           {'items': [86, 54, 53], 'worry_mult': partial(operator.add,2), 'test': 13, 'throw_to': (1,2), 'processed_items': 0},
           {'items': [50, 65, 78, 50, 62, 99], 'worry_mult': partial(operator.add,3), 'test':11 , 'throw_to': (3,7) , 'processed_items': 0},
           {'items': [90], 'worry_mult': partial(operator.add,4), 'test':2 , 'throw_to': (4,6), 'processed_items': 0},
           {'items': [88, 92, 63, 94, 96, 82, 53, 53], 'worry_mult': partial(operator.add,8), 'test':5 , 'throw_to': (4,7), 'processed_items': 0},
           {'items': [70, 60, 71, 69, 77, 70, 98], 'worry_mult': partial(operator.mul,7), 'test':3 , 'throw_to': (2,3), 'processed_items': 0}
           ]

def round(monkeys):
    for monkey in monkeys:
        for _ in range(len(monkey['items'])):
            item = monkey['items'].pop(0)
            item = monkey['worry_mult'](item) 
            item = item // 3
            if (item % monkey['test']) == 0:
                monkeys[monkey['throw_to'][0]]['items'].append(item)
            else:
                monkeys[monkey['throw_to'][1]]['items'].append(item)

            monkey['processed_items'] += 1


for i in range(rounds):
    round(monkeys)

res = [monkey['processed_items'] for monkey in monkeys]
res.sort(reverse=True)
print(f"First solution: {res[0]*res[1]}")
