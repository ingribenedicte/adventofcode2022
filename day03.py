from pathlib import Path

rucksacks = Path.read_text(Path('input/day3.txt')).strip().split('\n')

def get_priority(c):
    if c.islower():
        return ord(c) - 96
    if c.isupper():
        return ord(c.lower()) - 96 + 26

# Part 1
sum_priorities = 0
for rucksack in rucksacks:
    m, l = int(len(rucksack) / 2), len(rucksack)
    first_compartment, second_compartment = set(rucksack[0: m]), set(rucksack[m: l])
    common_item = max(first_compartment.intersection(second_compartment))
    sum_priorities += get_priority(common_item)

# Part 2
n_teams = len(rucksacks)//3
sum_team_priorities = 0
for i in range(n_teams):
    team_rucksacks = rucksacks[i*3: (i*3)+3]
    common_item = max(set(team_rucksacks[0]) & set(team_rucksacks[1]) & set(team_rucksacks[2]))
    sum_team_priorities += get_priority(common_item)

print(f"Answer Part One: {sum_priorities}")
print(f"Answer Part Two: {sum_team_priorities}")
