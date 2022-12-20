from pathlib import Path

numbers, orders, indices = [], [], []
for i, line in enumerate(Path.read_text(Path('input/day20.txt')).strip().split('\n')):
    numbers.append(int(line))
    indices.append(i)

def mixing(numbers, indices):
    sequence = numbers.copy()
    max_index = max(indices)

    j = 0
    while j < len(numbers):
        number = numbers[j]
        index = indices[j]

        if number == 0:
            j += 1
            continue

        new_index = index + number
        new_index %= max_index

        if new_index == 0:
            new_index = max_index

        del sequence[index]
        left, right = sequence[:new_index], sequence[new_index:]

        sequence = left + [number] + right

        indices[j] = new_index
        for k in range(len(indices)):
            if new_index > index:
                if k != j and indices[k] >= index and indices[k] <= new_index:
                    indices[k] -= 1
            else:
                if k != j and indices[k] >= new_index and indices[k] <= index:
                    indices[k] += 1
        j += 1
    return sequence, indices

sequence, post_indices = mixing(numbers, indices)
starting_index = sequence.index(0)
n = len(sequence)

i_1000 = (starting_index + 1000) % n
i_2000 = (starting_index + 2000) % n
i_3000 = (starting_index + 3000) % n

print(f"Answer Part One: {sequence[i_1000] + sequence[i_2000] + sequence[i_3000]}")