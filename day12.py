from pathlib import Path
import networkx as nx

input = Path.read_text(Path('input/day12.txt')).strip().split('\n')
height, width = len(input), len(input[1])

G = nx.DiGraph()
for i, row in enumerate(input):
    left = -10
    for j, col in enumerate(row):
        current = ord(col) - 96

        if abs(current - left) <= 1:
            G.add_edge((i, j-1), (i, j))
            G.add_edge((i, j), (i, j - 1))
        elif current > left + 1:
            G.add_edge((i, j), (i, j-1))
        elif current < left - 1:
            G.add_edge((i, j -1), (i, j))

        if i != 0:
            up = ord(input[i - 1][j]) - 96
            if abs(current - up) <= 1:
                G.add_edge((i-1, j), (i, j))
                G.add_edge((i, j), (i - 1, j))
            elif current > up + 1:
                G.add_edge((i, j), (i-1, j))
            elif current < up - 1:
                G.add_edge((i-1, j), (i, j))
        left = current

        if col == 'S':
            if i != 0 and input[i-1][j] <= 'b':
                G.add_edge('S', (i - 1, j))
            if i != height - 1 and input[i+1][j] <= 'b':
                G.add_edge('S', (i + 1, j))
            if j != 0 and row[j-1] <= 'b':
                G.add_edge('S', (i, j - 1))
            if j != width - 1 and row[j+1] <= 'b':
                G.add_edge('S', (i, j + 1))

        elif col == 'E':
            if i != 0 and input[i-1][j] >= 'y':
                G.add_edge((i - 1, j), 'E')
            if i != height - 1 and input[i+1][j] >= 'y':
                G.add_edge((i + 1, j), 'E')
            if j != 0 and row[j-1] >= 'y':
                G.add_edge((i, j - 1), 'E')
            if j != width - 1 and row[j + 1] >= 'y':
                G.add_edge((i, j + 1), 'E')

path_lengths = []
for i, row in enumerate(input):
    for j, col in enumerate(row):
        if col == 'a':
            if nx.has_path(G, (i, j), 'E'):
                path_lengths.append(len(nx.shortest_path(G, (i, j), 'E')) - 1)

print(f"Answer Part One: {len(nx.shortest_path(G, 'S', 'E')) - 1}")
print(f"Answer Part Two: {min(path_lengths)}")