from pathlib import Path
import re

description_row = 0
tiles, walls = set(), set()
for i, row in enumerate(Path.read_text(Path('input/day22.txt')).split('\n')):
    if row == '':
        description_row = i+1
        break
    for j, col in enumerate(row):
        if col == '.':
            tiles.add((j, i))
        elif col == '#':
            tiles.add((j, i))
            walls.add((j, i))

description = re.split('(R|L)', Path.read_text(Path('input/day22.txt')).split('\n')[description_row])

y = min(tile[1] for tile in tiles)
x = min(tile[0] for tile in tiles if tile[1] == y)
facing = 0

for step in description:
    if step.isnumeric():
        n_steps = int(step)
        for n in range(n_steps):
            if facing == 0:
                next = (x + 1, y) if (x + 1, y) in tiles else (min(tile[0] for tile in tiles if tile[1] == y), y)
            elif facing == 1:
                next = (x, y + 1) if (x, y + 1) in tiles else (x, min(tile[1] for tile in tiles if tile[0] == x))
            elif facing == 2:
                next = (x - 1, y) if (x - 1, y) in tiles else (max(tile[0] for tile in tiles if tile[1] == y), y)
            elif facing == 3:
                next = (x, y - 1) if (x, y - 1) in tiles else (x, max(tile[1] for tile in tiles if tile[0] == x))
            if next in walls:
                break
            (x, y) = next
    else:
        facing = (facing - 1) % 4 if step == 'L' else (facing + 1) % 4

print(f"Answer Part One: {4 * (x + 1) + 1000 * (y + 1) + facing}")