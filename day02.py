from pathlib import Path

rps_translate = {'A': 'X', 'B': 'Y', 'C': 'Z'}
score_shapes_p1 = {'X': 1, 'Y': 2, 'Z': 3}

def score_p1(round):
    opponent, you = round[0], round[1]
    score = score_shapes_p1.get(you)
    if you == rps_translate.get(opponent):
        score += 3
    elif (opponent == 'A' and you == 'Y') or (opponent == 'B' and you == 'Z') or (opponent == 'C' and you == 'X'):
        score += 6
    return score

rps_win = {'A': 'C', 'B': 'A', 'C': 'B'}
score_shapes_p2 = {'A': 1, 'B': 2, 'C': 3}

def score_p2(round):
    opponent, result = round[0], round[1]
    if result == 'X':
        you = rps_win.get(opponent)
        return score_shapes_p2.get(you)
    if result == 'Y':
        you = opponent
        return score_shapes_p2.get(you) + 3
    if result == 'Z':
        key_list, val_list = list(rps_win.keys()), list(rps_win.values())
        you = key_list[val_list.index(opponent)]
        return score_shapes_p2.get(you) + 6

input = Path.read_text(Path('input/day2.txt')).strip().split('\n')
print(f"Answer Part One: {sum(score_p1(round.split(' ')) for round in input)}")
print(f"Answer Part Two: {sum(score_p2(round.split(' ')) for round in input)}")
