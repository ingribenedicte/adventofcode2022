from pathlib import Path

directions = Path.read_text(Path('input/day17.txt')).strip()

rocks = [[(0, 0), (1, 0), (2, 0), (3, 0)],
         [(0, 1), (1, 0), (1, 1), (1, 2), (2, 1)],
         [(0, 0), (1, 0), (2, 0), (2, 1), (2, 2)],
         [(0, 0), (0, 1), (0, 2), (0, 3)],
         [(0, 0), (0, 1), (1, 0), (1, 1)]]

direction_index = 0
n = len(directions)
caves = set((x, -1) for x in range(0, 7))
for i in range(2022):
    max_y = max(rock[1] for rock in caves)
    rock = [(x + 2, y + max_y + 4) for (x, y) in rocks[i % 5]]
    landed = False

    while not landed:
        direction = directions[direction_index]
        if direction == '>' and max(position[0] for position in rock) < 6:
            next_rock = [(x + 1, y) for (x, y) in rock]
        elif direction == '<' and min(position[0] for position in rock) > 0:
            next_rock = [(x - 1, y) for (x, y) in rock]
        available = True
        for pos in next_rock:
            if pos in caves:
                available = False
        if available:
            rock = next_rock

        direction_index += 1
        direction_index %= n

        next_rock = [(x, y - 1) for (x, y) in rock]
        for pos in next_rock:
            if pos in caves:
                caves = caves.union(rock)
                landed = True

        rock = next_rock

print(f"Answer Part One: {max(rock[1] for rock in caves) + 1}")