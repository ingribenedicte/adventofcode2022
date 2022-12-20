from pathlib import Path

calories_list = []
calories = 0
for c in Path.read_text(Path('input/day1.txt')).strip().split('\n'):
    if c == '':
        calories_list.append(calories)
        calories = 0
    else:
        calories += int(c)

print(f"Answer Part One: {sorted(calories_list, reverse = True)[0]}")
print(f"Answer Part Two: {sum(sorted(calories_list, reverse = True)[0:3])}")