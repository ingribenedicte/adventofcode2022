from pathlib import Path

def update_signal_strength(cycle, X, signal):
    if cycle == 20 or (cycle - 20) % 40 == 0:
        return signal + cycle * X
    return signal

cycle, X, signal = 0, 1, 0
for instr in Path.read_text(Path('input/day10.txt')).strip().split('\n'):
    if instr == 'noop':
        cycle += 1
        signal = update_signal_strength(cycle, X, signal)
    elif instr.startswith('addx'):
        V = int(instr.split(' ')[1])
        for i in range(2):
            cycle += 1
            signal = update_signal_strength(cycle, X, signal)
        X += V

cycle, X, CRT, crt_row = 0, 1, [], []
for instr in Path.read_text(Path('input/day10.txt')).strip().split('\n'):
    sprite_position = [X - 1, X, X + 1]
    if instr == 'noop':
        if (cycle - 40 * len(CRT)) in sprite_position:
            crt_row.append('#')
        else:
            crt_row.append('.')
        if len(crt_row) == 40:
            CRT.append(crt_row)
            crt_row = []
        cycle += 1
    else:
        V = int(instr.split(' ')[1])
        for i in range(2):
            if (cycle - 40 * len(CRT)) in sprite_position:
                crt_row.append('#')
            else:
                crt_row.append('.')
            if len(crt_row) == 40:
                CRT.append(crt_row)
                crt_row = []
            cycle += 1
        X += V

print(f"Answer Part One: {signal}")
print("Answer Part Two:")
for row in CRT:
    print("".join(row))