from pathlib import Path

S, B, distances = [], [], []
for line in Path.read_text(Path('input/day15.txt')).strip().split('\n'):
    sensor = line.split(':')[0].split(' ')
    s_x, s_y = int(sensor[2][2:-1]), int(sensor[3][2:])
    S.append((s_x, s_y))

    beacon = line.split(':')[1].split(' ')
    b_x, b_y = int(beacon[5][2:-1]), int(beacon[6][2:])
    B.append((b_x, b_y))

    distances.append(abs(b_x - s_x) + abs(b_y - s_y))

row = 2000000
no_beacon_positions = set()
for i in range(len(S)):
    s_x, s_y, b, distance = S[i][0], S[i][1], B[i], distances[i]
    n_rows = abs(s_y - row)
    if n_rows > distance:
        continue

    n_cols = abs(distance - n_rows)
    for col in range(s_x - n_cols, s_x + n_cols + 1):
        no_beacon_positions.add((col, row))

no_beacon_positions = no_beacon_positions - set(B)
print(f"Answer Part One: {len(no_beacon_positions)}")