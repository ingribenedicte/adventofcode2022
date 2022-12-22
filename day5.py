from pathlib import Path
import copy

input = Path.read_text(Path('input/day5.txt')).split('\n')
ind = input.index('')
n_stacks = int(str.split(input[ind - 1], ' ')[-1])
indices = [0] + [(3 + 4*i) for i in range(n_stacks)]

stacks_horizontal, stacks = [], [[] for i in range(n_stacks)]
for i in range(len(input[:ind])):
    stacks_horizontal.append([input[i][j:k].strip() for j, k in zip(indices[:-1], indices[1:])])

for i in range(n_stacks):
    for j in reversed(range(len(stacks_horizontal)-1)):
        if stacks_horizontal[j][i] != '':
            stacks[i].append(stacks_horizontal[j][i])

initial_stacks = copy.deepcopy(stacks)

for step in input[ind+1:]:
    step = str.split(step, ' ')
    n, f, t = int(step[1]), int(step[3]), int(step[5])

    for i in range(n):
        chunk = stacks[f-1].pop()
        stacks[t-1].append(chunk)

top_crates = "".join([stack[-1][1] for stack in stacks])
print(f"Answer Part One: {top_crates}")

stacks = initial_stacks
for step in input[ind+1:]:
    step = str.split(step, ' ')
    n, f, t = int(step[1]), int(step[3]), int(step[5])
    chunk = []
    for i in range(n):
        chunk.insert(0, stacks[f-1].pop())
    stacks[t-1].extend(chunk)

top_crates = "".join([stack[-1][1] for stack in stacks])
print(f"Answer Part Two: {top_crates}")