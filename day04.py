from pathlib import Path

pairs = [str.split(p, ',') for p in Path.read_text(Path('input/day4.txt')).strip().split('\n')]

fully_contained_pairs, overlapping_pairs = 0, 0
for pair in pairs:
    first_range, second_range = str.split(pair[0], '-'), str.split(pair[1], '-')

    if int(first_range[0]) >= int(second_range[0]) and int(first_range[1]) <= int(second_range[1]):
        fully_contained_pairs += 1

    elif int(first_range[0]) <= int(second_range[0]) and int(first_range[1]) >= int(second_range[1]):
        fully_contained_pairs += 1

    first_sections = set([*range(int(first_range[0]), int(first_range[1])+1)])
    second_sections = set([*range(int(second_range[0]), int(second_range[1])+1)])

    if not first_sections.isdisjoint(second_sections):
        overlapping_pairs += 1

print(f"Answer Part One: {fully_contained_pairs}")
print(f"Answer Part Two: {overlapping_pairs}")
