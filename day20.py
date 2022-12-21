from pathlib import Path

numbers = [int(line) for line in Path.read_text(Path('input/day20.txt')).strip().split('\n')]
n = len(numbers)
indices = [i for i in range(n)]

def mixing(sequence, numbers, indices):
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

sequence = numbers.copy()
mixed_sequence, mixed_indices = mixing(sequence, numbers, indices)
starting_index = mixed_sequence.index(0)
i_1000, i_2000, i_3000 = (starting_index + 1000) % n, (starting_index + 2000) % n, (starting_index + 3000) % n
print(f"Answer Part One: {mixed_sequence[i_1000] + mixed_sequence[i_2000] + mixed_sequence[i_3000]}")

decrypted_numbers = [(number * 811589153) for number in numbers]
sequence = decrypted_numbers.copy()
indices = [i for i in range(len(decrypted_numbers))]
for i in range(10):
    sequence, post_mix_indices = mixing(sequence, decrypted_numbers, indices)
    indices = post_mix_indices.copy()

starting_index = sequence.index(0)
i_1000, i_2000, i_3000 = (starting_index + 1000) % n, (starting_index + 2000) % n, (starting_index + 3000) % n
print(f"Answer Part Two: {sequence[i_1000] + sequence[i_2000] + sequence[i_3000]}")