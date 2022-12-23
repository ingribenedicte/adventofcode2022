from pathlib import Path

elves = set()
for y, row in enumerate(Path.read_text(Path('input/day23.txt')).splitlines()):
    for x, col in enumerate(row):
        if col == '#':
            elves.add((x, y))
initial_elves = elves.copy()

directions = ['N', 'S', 'W', 'E']

def propose_move(adjacency, adjacent_elves, direction_index):
    directions_considered = set()

    while len(directions_considered) < 4:
        direction = directions[direction_index]

        if direction == 'N':
            if set(adjacency[0:3]).isdisjoint(adjacent_elves):
                return (x, y - 1)
        elif direction == 'S':
            if set(adjacency[4:7]).isdisjoint(adjacent_elves):
                return (x, y + 1)
        elif direction == 'W':
            if {adjacency[0], adjacency[6], adjacency[7]}.isdisjoint(adjacent_elves):
                return (x - 1, y)
        elif direction == 'E':
            if set(adjacency[2:5]).isdisjoint(adjacent_elves):
                return (x + 1, y)

        directions_considered.add(direction)
        direction_index = (direction_index + 1) % 4

    return None

def move_elves(elves, propositions):
    propostions_list = list(propositions.values())

    illegal_moves = set()
    for value in propostions_list:
        if propostions_list.count(value) > 1 or value is None:
            illegal_moves.add(value)

    propostions = {key: val for key, val in propositions.items() if val not in illegal_moves}

    for position, new_position in propostions.items():
        elves.remove(position)
        elves.add(new_position)

    return elves

for i in range(10):
    direction_index = i%4
    propostions = dict()

    for elf in elves:
        (x, y) = elf
        adjacency = [(x - 1, y - 1), (x, y - 1), (x + 1, y - 1), (x + 1, y), (x + 1, y + 1), (x, y + 1), (x - 1, y + 1), (x - 1, y)]
        adjacent_elves = elves.intersection(set(adjacency))

        if not adjacent_elves:
            continue

        propostions[elf] = propose_move(adjacency, adjacent_elves, direction_index)

    elves = move_elves(elves, propostions)

min_x, max_x = min(elf[0] for elf in elves), max(elf[0] for elf in elves)
min_y, max_y = min(elf[1] for elf in elves), max(elf[1] for elf in elves)

print(f"Answer Part One: {(max_x - min_x + 1) * (max_y - min_y + 1) - len(elves)}")

elves = initial_elves
i = 0
while i < 3000:
    direction_index = i%4
    propostions = dict()

    for elf in elves:
        (x, y) = elf
        adjacency = [(x - 1, y - 1), (x, y - 1), (x + 1, y - 1), (x + 1, y), (x + 1, y + 1), (x, y + 1), (x - 1, y + 1), (x - 1, y)]
        adjacent_elves = elves.intersection(set(adjacency))

        if not adjacent_elves:
            continue

        propostions[elf] = propose_move(adjacency, adjacent_elves, direction_index)

    if not bool(propostions):
        break

    elves = move_elves(elves, propostions)
    i += 1

print(f"Answer Part Two: {i+1}")