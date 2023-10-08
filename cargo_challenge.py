WIDTH = 10
HEIGHT = 53
EMPTY = '_'

# Cargo Shapes
O = [
    ['O', 'O'],
    ['O', 'O'],
]

I = [
    ['I'],
    ['I'],
    ['I'],
    ['I'],
]

S = [
    ['_', 'S', 'S'],
    ['S', 'S', '_'],
]

Z = [
    ['Z', 'Z', '_'],
    ['_', 'Z', 'Z'],
]

L = [
    ['L', '_'],
    ['L', '_'],
    ['L', 'L'],
]

J = [
    ['_', 'J'],
    ['_', 'J'],
    ['J', 'J'],
]

T = [
    ['T', 'T', 'T'],
    ['_', 'T', '_'],
    ['_', 'T', '_'],
]

cargo_shapes = {'O': O,
                'I': I,
                'S': S,
                'Z': Z,
                'L': L,
                'J': J,
                'T': T}

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
            print('delta ---->', delta)
            delta_row, delta_column = delta
            print('delta_row ---->', delta_row)
            print('delta_column ---->', delta_column)
            neighbor_row = x + delta_row
            neighbor_column = y + delta_column
            print('neighbor_row ---->', neighbor_row)
            print('neighbor_column ---->', neighbor_column)
            row_inbounds = 0 <= neighbor_row < WIDTH
            column_inbounds = 0 <= neighbor_column < HEIGHT
            print('row_inbounds ---->', row_inbounds)
            print('column_inbounds ---->', column_inbounds)

            if not (row_inbounds and column_inbounds and trailer[neighbor_column][neighbor_row] == '_'):
                print('Invalid position found:', neighbor_row, neighbor_column)
                all_positions_valid = False
                break

        if all_positions_valid:
            return x, y

        y -= 1
    return None



def get_cargo_positions(string_shape, x):
    shape = cargo_shapes[string_shape]
    positions = {}
    shape_positions = []

    for row in range(len(shape)):
        for column in range(len(shape[0])):
            if shape[row][column] == string_shape:
                shape_positions.append((row, column))
    positions[string_shape] = shape_positions

    print('positions ---->', positions)
    fill_trailer(trailer, positions, x)

def add_cargo(letter, x, y):
    if letter == 'O':
        trailer[y][x] = letter
        trailer[y - 1][x] = letter
        trailer[y][x + 1] = letter
        trailer[y - 1][x + 1] = letter
    elif letter == 'I':
        trailer[y][x] = letter
        trailer[y - 1][x] = letter
        trailer[y - 2][x] = letter
        trailer[y - 3][x] = letter
    elif letter == 'S':
        trailer[y][x] = letter
        trailer[y][x + 1] = letter
        trailer[y - 1][x + 1] = letter
        trailer[y - 1][x + 2] = letter
    elif letter == 'Z':
        trailer[y][x] = letter
        trailer[y][x + 1] = letter
        trailer[y + 1][x + 1] = letter
        trailer[y + 1][x + 2] = letter
    elif letter == 'L':
        trailer[y][x] = letter
        trailer[y - 1][x] = letter
        trailer[y - 2][x] = letter
        trailer[y - 2][x + 1] = letter
    elif letter == 'L':
        trailer[y][x] = letter
        trailer[y][x + 1] = letter
        trailer[y + 1][x + 1] = letter
        trailer[y + 2][x + 1] = letter
    elif letter == 'T':
        trailer[y][x] = letter
        trailer[y][x + 1] = letter
        trailer[y][x + 2] = letter
        trailer[y - 1][x + 1] = letter

def fill_trailer(trailer, positions, x):
    print(trailer)
    letter = list(positions.keys())[0]
    start_pos = get_valid_start(trailer, letter, x, HEIGHT - 1)
    x, y = start_pos
    print('x:', x)
    print('y:', y)
    print('letter ---->', letter)
    add_cargo(letter, x, y)

def print_trailer():
    for row in trailer:
        print(' '.join(row))

def main(entries):
    entries = entries.split(',')
    print('entries ---->', entries)
    for entry in entries:
        # print('entry ---->', entry)
        x = int(entry[0])
        shape = entry[1]
        # print('x-axis:', x, 'shape:', shape)
        get_cargo_positions(shape, x)
    print_trailer()

main('0O,2I,3S')
# main('7S,7I,5Z')
