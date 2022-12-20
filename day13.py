from pathlib import Path

pairs, pair = [], []
for line in Path.read_text(Path('input/day13.txt')).strip().split('\n'):
        if line != '':
            pair.append(eval(line))
            continue
        pairs.append(pair)
        pair = []
pairs.append(pair)

def process_lists(left, right):
    for i in range(min(len(left), len(right))):
        l_val, r_val = left[i], right[i]

        # compare integers
        if type(l_val) == type(r_val) and type(l_val) == int:
            if l_val < r_val:
                return True
            elif l_val > r_val:
                return False

        # compare lists
        elif type(l_val) == type(r_val) and type(l_val) == list:
            correct_order = process_lists(l_val, r_val)
            if correct_order:
                return True
            elif correct_order == False:
                return False

        # different types
        elif type(l_val) == list and type(r_val) == int:
            correct_order = process_lists(l_val, [r_val])
            if correct_order:
                return True
            elif correct_order == False:
                return False
        elif type(l_val) == int and type(r_val) == list:
            correct_order = process_lists([l_val], r_val)
            if correct_order:
                return True
            elif correct_order == False:
                return False

    if len(left) < len(right):
        return True
    elif len(left) > len(right):
        return False

    return None

all_packets = [[[2]], [[6]]]
for p in pairs:
    all_packets.append(p[0])
    all_packets.append(p[1])

# insertion sort
for i in range(1, len(all_packets)):
    current_packet = all_packets[i]
    j = i - 1
    in_order = process_lists(all_packets[j], current_packet)
    while j >= 0 and in_order == False:
        all_packets[j + 1] = all_packets[j]
        j -= 1
        in_order = process_lists(all_packets[j], current_packet)
    all_packets[j + 1] = current_packet

print(f"Answer Part One: {sum(i + 1 for i, p in enumerate(pairs) if process_lists(p[0], p[1]))}")
print(f"Answer Part Two: {(all_packets.index([[2]]) + 1) * (all_packets.index([[6]]) + 1)}")