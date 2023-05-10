from pathlib import Path

input = Path.read_text(Path('input/day6.txt')).strip()
print(f"Answer Part One: {[i for i in range(len(input[3:])) if len(set(input[i-4:i])) == 4][0]}")
print(f"Answer Part Two: {[i for i in range(len(input[13:])) if len(set(input[i-14:i])) == 14][0]}")
