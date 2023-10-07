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

# cargo_shapes = [O, I, S, Z, L, J, T]

cargo_shapes = {'O': O,
                'I': I,
                'S': S,
                'Z': Z,
                'L': L,
                'J': J,
                'T': T}

trailer = [[EMPTY] * WIDTH for _ in range(HEIGHT)]

def get_cargo_positions(string_shape, positions):
    shape = cargo_shapes[string_shape]
    shape_positions = []

    for row in range(len(shape)):
        for column in range(len(shape[0])):
            if shape[row][column] == string_shape:
                shape_positions.append((row, column))
    positions[string_shape] = shape_positions
    print('positions ---->', positions)
    return positions

def fill_trailer(entries):
    entries = entries.split(',')
    positions = {}
    print('entries ---->', entries)
    for entry in entries:
        # print('entry ---->', entry)
        x_axis = int(entry[0])
        shape = entry[1]
        # print('x-axis:', x_axis, 'shape:', shape)
        get_cargo_positions(shape, positions)

def print_trailer():
    for row in trailer:
        print(' '.join(row))

# print_trailer()
# print(trailer)

fill_trailer('7S,7I,5Z')




# shape_pos = convert_shape_format(current_piece)

# # add piece to the grid for drawing
# for i in range(len(shape_pos)):
#     x, y = shape_pos[i]
#     if y > -1:
#         grid[y][x] = current_piece.color
