from pathlib import Path
import copy

monkeys, items_lists, operations, tests, if_true, if_false = [], [], [], [], [], []
for i, line in enumerate(Path.read_text(Path('input/day11.txt')).split('\n')):
    if line.startswith('Monkey '):
        monkeys.append([int(line.strip().split(' ')[1][0])])
    elif line.strip().startswith('Starting items: '):
        items_lists.append([int(item) for item in line.strip().split('Starting items: ')[1].split(',')])
    elif line.strip().startswith('Operation: '):
        operations.append(line.strip().split(' ')[4:])
    elif line.strip().startswith('Test: '):
        tests.append(int(line.strip().split('Test: ')[1].split(' ')[2]))
    elif line.strip().startswith('If true: '):
        if_true.append(int(line.strip().split(' ')[-1]))
    elif line.strip().startswith('If false: '):
        if_false.append(int(line.strip().split(' ')[-1]))

initial_items_lists = copy.deepcopy(items_lists)

def inspection(item, operation):
    val = item if operation[1] == 'old' else int(operation[1])
    if operation[0] == '*':
        item *= val
    elif operation[0] == '+':
        item += val
    item //= 3
    return item

n_inspections = [0 for i in range(len(monkeys))]

for round in range(20):
    for i in range(len(monkeys)):
        monkey, items, operation, divisor, if_true_monkey, if_false_monkey = monkeys[i], items_lists[i], operations[i], tests[i], if_true[i], if_false[i]

        # inspection
        new_items = [inspection(item, operation) for item in items]

        # test
        for new_item in new_items:
            n_inspections[i] += 1
            if new_item % divisor == 0:
                items_lists[if_true_monkey].append(new_item)
            else:
                items_lists[if_false_monkey].append(new_item)

        items_lists[i] = []

n_inspections.sort()
print(f"Answer Part One: {n_inspections[-1] * n_inspections[-2]}")

items_lists = initial_items_lists.copy()

common_divisor = 1
for divisor in tests:
    common_divisor *= divisor

def inspection(item, operation):
    val = item if operation[1] == 'old' else int(operation[1])
    if operation[0] == '*':
        item *= val
    elif operation[0] == '+':
        item += val
    item %= common_divisor
    return item

n_inspections = [0 for i in range(len(monkeys))]
for round in range(10000):
    for i in range(len(monkeys)):
        monkey, items, operation, divisor, if_true_monkey, if_false_monkey = monkeys[i], items_lists[i], operations[i], tests[i], if_true[i], if_false[i]

        # inspection
        new_items = [inspection(item, operation) for item in items]

        # test
        for new_item in new_items:
            n_inspections[i] += 1
            if new_item % divisor == 0:
                items_lists[if_true_monkey].append(new_item)
            else:
                items_lists[if_false_monkey].append(new_item)

        items_lists[i] = []

n_inspections.sort()
print(f"Answer Part Two: {n_inspections[-1] * n_inspections[-2]}")