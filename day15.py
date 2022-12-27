from pathlib import Path

S, B, distances = [], [], []
for line in Path.read_text(Path('input/day15.txt')).strip().splitlines():
    sensor = line.split(':')[0].split(' ')
    s_x, s_y = int(sensor[2][2:-1]), int(sensor[3][2:])
    S.append((s_x, s_y))

    beacon = line.split(':')[1].split(' ')
    b_x, b_y = int(beacon[5][2:-1]), int(beacon[6][2:])
    B.append((b_x, b_y))

    distances.append(abs(b_x - s_x) + abs(b_y - s_y))

row = 2000000
no_beacon_positions_row = set()
for i in range(len(S)):
    s_x, s_y, b, distance = S[i][0], S[i][1], B[i], distances[i]
    n_rows = abs(s_y - row)
    if n_rows > distance:
        continue

    n_cols = abs(distance - n_rows)
    for col in range(s_x - n_cols, s_x + n_cols + 1):
        no_beacon_positions_row.add((col, row))

no_beacon_positions = no_beacon_positions_row - set(B)
print(f"Answer Part One: {len(no_beacon_positions_row)}")

rows = {i: [] for i in range(0, 4000001)}
for i in range(len(S)):
    s_x, s_y, b, distance = S[i][0], S[i][1], B[i], distances[i]

    max_row = s_y + distance if s_y + distance <= 4000000 else 4000000
    min_row = s_y - distance if s_y - distance >= 0 else 0

    for row in range(min_row, max_row + 1):
        row_interval_length = distance - abs(s_y - row)

        max_col = s_x + row_interval_length if s_x + row_interval_length <= 4000000 else 4000000
        min_col = s_x - row_interval_length if s_x - row_interval_length >= 0 else 0

        rows[row].append((min_col, max_col))

position_found = False
for row in rows:
    interval_list = sorted(rows[row])
    max_x = 0
    for interval in interval_list:
        if interval[0] > max_x + 1:
            y = row
            x = max_x + 1
            position_found = True
            break
        max_x = max(interval[1], max_x)

    if position_found:
        break

print(f"Answer Part Two: {x * 4000000 + y}")