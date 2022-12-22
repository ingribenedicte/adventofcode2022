from pathlib import Path

input = Path.read_text(Path('input/day14.txt')).strip().split('\n')

rocks = set()
for line in input:
    line_list = line.split(' -> ')
    for start, stop in zip(line_list[:-1], line_list[1:]):
        x_1, y_1 = [int(n) for n in start.split(',')]
        x_2, y_2 = [int(n) for n in stop.split(',')]

        x_range = range(min(x_1, x_2), max(x_1, x_2)+1)
        y_range = range(min(y_1, y_2), max(y_1, y_2)+1)

        for x in x_range:
            for y in y_range:
                rocks.add((x, y))

max_y = max(rock[1] for rock in rocks)
free_fall = False
sand = set()
while not free_fall:
    caves = rocks.union(sand)
    x, y = 500, 0
    falling = True
    for i in range(1000):
        next = (x, y + 1)
        if next in caves:
            left_down = (x - 1, y + 1)
            right_down = (x + 1, y + 1)
            if left_down not in caves:
                next = left_down
            else:
                right_down = (x + 1, y + 1)
                if right_down not in caves:
                    next = right_down
                else:
                    sand.add((x, y))
                    break
        (x, y) = next
        if y > max_y:
            free_fall = True

print(f"Answer Part One: {len(sand)}")

y = max_y + 2
for x in range(-10000, 10000):
    rocks.add((x, y))

sand = set()
while (500, 0) not in sand:
    caves = rocks.union(sand)
    x, y = 500, 0
    falling = True
    for i in range(1000):
        next = (x, y + 1)
        if next in caves:
            left_down = (x - 1, y + 1)
            right_down = (x + 1, y + 1)
            if left_down not in caves:
                next = left_down
            else:
                right_down = (x + 1, y + 1)
                if right_down not in caves:
                    next = right_down
                else:
                    sand.add((x, y))
                    break
        (x, y) = next

print(f"Answer Part Two: {len(sand)}")