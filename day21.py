from pathlib import Path

monkeys, numbers, operations = [], [], []
for i, line in enumerate(Path.read_text(Path('input/day21.txt')).strip().split('\n')):
    monkeys.append(line.split(':')[0])
    if line[6:].split(' ')[0].isnumeric():
        numbers.append(int(line[6:].split(' ')[0]))
        operations.append(None)
        continue
    operations.append(line.split(' ')[1:])
    numbers.append(None)

def get_number(monkey, monkeys, numbers, operations):
    monkey_index = monkeys.index(monkey)

    while numbers[monkey_index] is None:
        for i in range(len(operations)):
            if operations[i] is None:
                continue
            operation = operations[i]
            first_monkey, second_monkey = operation[0], operation[2]
            first_monkey_index, second_monkey_index = monkeys.index(first_monkey), monkeys.index(second_monkey)
            first_monkey_number, second_monkey_number = numbers[first_monkey_index], numbers[second_monkey_index]

            if first_monkey_number is not None and second_monkey_number is not None:
                operation = [str(first_monkey_number), operations[i][1], str(second_monkey_number)]
                result = eval("".join(operation))
                operations[i] = None
                numbers[i] = result
    return numbers[monkey_index]

print(f"Answer Part One: {get_number('root', monkeys, numbers, operations)}")