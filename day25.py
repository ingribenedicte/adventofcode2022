from pathlib import Path

def snafu_to_decimal(snafu):
    decimal = 0
    for i, c in enumerate(snafu[::-1]):
        if c.isnumeric():
            multiplicator = int(c)
        else:
            multiplicator = -1 if c == '-' else -2
        decimal += multiplicator * 5 ** i
    return decimal

def decimal_to_snafu(decimal):
    # find the maximal exponential to be part of SNAFU string
    last_distance_lower, last_distance_higher = decimal, decimal
    exponent = 0
    close = False
    while not close:
        distance_lower, distance_higher = abs(decimal - 5 ** exponent), abs(decimal - 2 * 5 ** exponent)
        if min(distance_lower, distance_higher) > min(last_distance_lower, last_distance_higher):
            break
        last_distance_lower, last_distance_higher = distance_lower, distance_higher
        exponent += 1

    max_exponent = exponent - 1
    if last_distance_lower < last_distance_higher:
        snafu = '1'
        decimal -= 5 ** max_exponent
    else:
        snafu = '2'
        decimal -= 2 * 5 ** max_exponent

    # find rest of the string
    snafu_str_options = ['=', '-', '0', '1', '2']
    for exponent in range (max_exponent - 1, -1, -1):
        options = [- 2 * 5 ** exponent, - 1 * 5 ** exponent, 0, 5 ** exponent, 2 * 5 ** exponent]

        distances = [abs(decimal - option) for option in options]
        min_distance = min(distances)
        min_option_index = distances.index(min_distance)

        decimal -= options[min_option_index]
        snafu += snafu_str_options[min_option_index]

    return snafu

decimal_sum = sum(snafu_to_decimal(snafu) for snafu in Path.read_text(Path('input/day25.txt')).splitlines())
print(f"Answer Part One: {decimal_to_snafu(decimal_sum)}")