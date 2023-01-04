from pathlib import Path
import networkx as nx

G = nx.Graph()
flow_rates = dict()
for line in Path.read_text(Path('input/day16.txt')).strip().split('\n'):
    line_list = line.split(' ')
    source = line_list[1]
    flow_rates[source] = int(line_list[4][5:-1])
    sinks = [sink.strip(',') for sink in line_list[9:]]
    for sink in sinks:
        G.add_edge(source, sink)

valid_valves = {valve for valve in flow_rates.keys() if flow_rates[valve] > 0}

def find_maximum_pressure(G, minutes_left, current_valve, current_pressure, current_open_valves):
    current_open_valves = current_open_valves.copy()

    remaining_valves = valid_valves - current_open_valves
    if minutes_left <= 0 or not remaining_valves:
        return current_pressure, current_open_valves

    if current_valve in remaining_valves:
        minutes_left -= 1
        current_open_valves.add(current_valve)
        remaining_valves -= {current_valve}
        current_pressure += flow_rates[current_valve] * minutes_left

    pressure_list, open_valves_list = [], []
    for valve in remaining_valves:
        distance = len(nx.shortest_path(G, current_valve, valve)) - 1
        pressure, open_valves = find_maximum_pressure(G, minutes_left - distance, valve, current_pressure, current_open_valves)
        pressure_list.append(pressure)
        open_valves_list.append(open_valves)

    max_pressure = max(pressure_list)
    max_pressure_index = pressure_list.index(max_pressure)
    open_valves = open_valves_list[max_pressure_index]

    return max_pressure, open_valves

print(f"Answer Part One: {find_maximum_pressure(G, 30, 'AA', 0, set())[0]}")