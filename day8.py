from pathlib import Path

tree_rows = Path.read_text(Path('input/day8.txt')).strip().split('\n')
width, length = len(tree_rows[0]), len(tree_rows)

tree_cols = [[] for w in range(width)]
for row in tree_rows:
    for i, val in enumerate(row):
        tree_cols[i].append(val)

def is_visible(row, col, coord):
    row, row_coord = str(row), coord[0]
    if row_coord == 0 or row_coord == width - 1:
        return 1

    left, tree, right = row[:row_coord], row[row_coord], row[row_coord+1:]
    if tree > max(left) or tree > max(right):
        return 1

    col, col_coord = "".join(col), coord[1]
    if col_coord == 0 or col_coord == length - 1:
        return 1

    up, tree, down = col[:col_coord], col[col_coord], col[col_coord+1:]
    if tree > max(up) or tree > max(down):
        return 1

    return 0

def get_scenic_score(row, col, coord):
    row, row_coord = str(row), coord[0]
    left, tree, right = row[:row_coord], row[row_coord], row[row_coord + 1:]
    col, col_coord = "".join(col), coord[1]

    if row_coord == 0 or row_coord == width - 1 or col_coord == 0 or col_coord == length - 1:
        return 0

    for i, val in enumerate(reversed(left)):
        if val >= tree or i == len(left) - 1:
            left_view = i + 1
            break

    for i, val in enumerate(right):
        if val >= tree or i == len(right) - 1:
            right_view = i + 1
            break

    up, tree, down = col[:col_coord], col[col_coord], col[col_coord + 1:]
    for i, val in enumerate(reversed(up)):
        if val >= tree or i == len(up) - 1:
            up_view = i + 1
            break

    for i, val in enumerate(down):
        if val >= tree or i == len(down) - 1:
            down_view = i + 1
            break
    return left_view*right_view*up_view*down_view

grid = [[0 for i in range(width)] for j in range(length)]
scenic_scores = [[0 for i in range(width)] for j in range(length)]
for row, tree_line in enumerate(tree_rows):
    for col, tree in enumerate(tree_line):
        coord = (col, row)
        grid[row][col] = is_visible(tree_line, tree_cols[col], coord)
        scenic_scores[row][col] = get_scenic_score(tree_line, tree_cols[col], coord)

print(f"Answer Part One: {sum(sum(g) for g in grid)}")
print(f"Answer Part Two: {max(max(s) for s in scenic_scores)}")