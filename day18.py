from pathlib import Path

cubes = set()
for line in Path.read_text(Path('input/day18.txt')).strip().split('\n'):
    x, y, z = [int(s) for s in line.split(',')]
    cubes.add((x, y, z))

area = 6 * len(cubes)
for cube in cubes:
    for other_cube in cubes:
        if abs(cube[0] - other_cube[0]) + abs(cube[1] - other_cube[1]) + abs(cube[2] - other_cube[2]) == 1:
            area -= 1

print(f"Answer Part One: {area}")