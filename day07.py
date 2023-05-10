from pathlib import Path
import networkx as nx

directories = set()
G = nx.DiGraph()
current_path = []
level = 0

for line in Path.read_text(Path('input/day7.txt')).strip().split('\n'):
    if line[0:4] == '$ cd' and line[5:7] != '..':
        level += 1
        current_directory = "".join([str(item) + '/' for item in current_path]) + line[5:]
        current_path.append(line[5:])
        G.add_node(current_directory)
        directories.add((current_directory, level))
    elif line[0:4] == '$ cd' and line[5:7] == '..':
        level -= 1
        current_path.pop()
        current_directory = current_path[-1]
    elif line == '$ ls':
        continue
    else:
        type, node = line.split(' ')
        next_node = current_directory + '/' + node
        if type == 'dir':
            G.add_edge(current_directory, next_node, weight = 0)
        else:
            G.add_edge(current_directory, next_node, weight = int(type))

edge_weights = nx.get_edge_attributes(G, 'weight')

levels = list(set([d[1] for d in directories]))
directories_sizes = dict()
for level in reversed(levels):
    dirs = [d[0] for d in directories if d[1] == level]
    for d in dirs:
        tot_dir_size = 0
        for edge in G.out_edges(d):
            tot_dir_size += edge_weights[edge]
            if edge_weights[edge] == 0:
                dir_node = edge[1]
                tot_dir_size += directories_sizes[dir_node]
        directories_sizes[d] = tot_dir_size

used_space = directories_sizes['/']
max_space = 40000000
smallest_dir_size = used_space
for dir in directories_sizes:
    dir_size = directories_sizes[dir]
    if used_space - dir_size <= max_space:
        if dir_size < smallest_dir_size:
            smallest_dir_size = dir_size

print(f"Answer Part One: {sum(directories_sizes[d] for d in directories_sizes if directories_sizes[d] < 100000)}")
print(f"Answer Part Two: {smallest_dir_size}")
