from pathlib import Path
import math

def move_head(x_h, y_h, direction):
    if direction == 'R':
        x_h += 1
    elif direction == 'L':
        x_h -= 1
    elif direction == 'U':
        y_h += 1
    elif direction == 'D':
        y_h -= 1
    return x_h, y_h

def move_tail(x_h, y_h, x_t, y_t):
    if abs(x_h - x_t) > 1 and abs(y_h - y_t) > 0:
        x_t += 1 * math.copysign(1, x_h - x_t)
        y_t += 1 * math.copysign(1, y_h - y_t)
    elif abs(x_h - x_t) > 0 and abs(y_h - y_t) > 1:
        x_t += 1 * math.copysign(1, x_h - x_t)
        y_t += 1 * math.copysign(1, y_h - y_t)
    elif abs(x_h - x_t) > 1:
        x_t += 1 * math.copysign(1, x_h - x_t)
    elif abs(y_h - y_t) > 1:
        y_t += 1 * math.copysign(1, y_h - y_t)
    return x_t, y_t

positions_first_tail = set()
positions_last_tail = set()
x, y = [0 for i in range(10)], [0 for i in range(10)]
for step in Path.read_text(Path('input/day9.txt')).strip().split('\n'):
    direction, length = step.split(' ')
    for n in range(int(length)):
        x[0], y[0] = move_head(x[0], y[0], direction)
        for i in range(1, 10):
            x[i], y[i] = move_tail(x[i - 1], y[i - 1], x[i], y[i])
        positions_first_tail.add((x[1], y[1]))
        positions_last_tail .add((x[9], y[9]))

print(f"Answer Part One: {len(positions_first_tail)}")
print(f"Answer Part Two: {len(positions_last_tail)}")