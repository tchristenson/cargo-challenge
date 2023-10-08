WIDTH = 10
HEIGHT = 53
EMPTY = '_'

deltas = {'O': [(0, 0), (0, -1), (1, 0), (1, -1)],
                'I': [(0, 0), (0, -1), (0, -2), (0, -3)],
                'S': [(0, 0), (1, 0), (1, -1), (2, -1)],
                'Z': [(0, 0), (1, 0), (1, 1), (2, 1)],
                'L': [(0, 0), (0, -1), (0, -2), (1, 0)],
                'J': [(0, 0), (1, 0), (1, -1), (1, -2)],
                'T': [(0, 0), (1, 0), (2, 0), (1, 1)]}

trailer = [[EMPTY] * WIDTH for _ in range(HEIGHT)]


def get_valid_start(trailer, letter, x, y):
    while y >= 0:
        all_positions_valid = True

        for delta in deltas[letter]:
            # print('delta ---->', delta)
            delta_row, delta_column = delta
            # print('delta_row ---->', delta_row)
            # print('delta_column ---->', delta_column)
            neighbor_row = x + delta_row
            neighbor_column = y + delta_column
            # print('neighbor_row ---->', neighbor_row)
            print('neighbor_column ---->', neighbor_column)
            row_inbounds = 0 <= neighbor_row < WIDTH
            column_inbounds = 0 <= neighbor_column < HEIGHT

            if not (row_inbounds and column_inbounds and trailer[neighbor_column][neighbor_row] == '_'):
                # print('Invalid position found:', neighbor_row, neighbor_column)
                all_positions_valid = False
                break

        if all_positions_valid:
            return x, y

        y -= 1
    return None


def fill_trailer(trailer, letter, x, lowest_y):
    # print(trailer)
    # letter = list(positions.keys())[0]
    start_pos = get_valid_start(trailer, letter, x, HEIGHT - 1)
    x, y = start_pos

    print('x:', x)
    print('y:', y)
    print('letter ---->', letter)
    print('lowest_y ---->', lowest_y)
    for delta in deltas[letter]:
        delta_row, delta_column = delta
        # print('delta_row ---->', delta_row)
        # print('delta_column ---->', delta_column)
        neighbor_row = x + delta_row
        neighbor_column = y + delta_column
        trailer[neighbor_column][neighbor_row] = letter
        print('test ---->', neighbor_column < lowest_y)
        if neighbor_column < lowest_y:
            lowest_y = neighbor_column
    return lowest_y


def print_trailer():
    for row in trailer:
        print(' '.join(row))


def main(entries):
    entries = entries.split(',')
    lowest_y = float('inf')
    print('entries ---->', entries)
    for entry in entries:
        # print('entry ---->', entry)
        x = int(entry[0])
        letter = entry[1]
        # print('x-axis:', x, 'shape:', shape)
        lowest_y = fill_trailer(trailer, letter, x, lowest_y)
        # get_cargo_positions(letter, x)
    print_trailer()
    return HEIGHT - 1 - lowest_y


# print(main('0O,2I,3S'))
print(main('7S,7I,5Z'))
# print(main('7S,7I,5Z,5Z,5I,5I'))
