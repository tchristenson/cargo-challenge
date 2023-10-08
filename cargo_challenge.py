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

def find_start_pos(trailer, x_axis):
    for y in range(HEIGHT - 1, -1 , -1):
        if trailer[y][x_axis] == '_':
            return x_axis, y
    return None

def get_cargo_positions(string_shape, x_axis):
    shape = cargo_shapes[string_shape]
    positions = {}
    shape_positions = []

    for row in range(len(shape)):
        for column in range(len(shape[0])):
            if shape[row][column] == string_shape:
                shape_positions.append((row, column))
    positions[string_shape] = shape_positions

    print('positions ---->', positions)
    fill_trailer(trailer, positions, x_axis)

def fill_trailer(trailer, positions, x_axis):
    print(trailer)
    start_pos = find_start_pos(trailer, x_axis)
    x, y = start_pos
    letter = list(positions.keys())[0]
    print('x:', x)
    print('y:', y)
    print('letter ---->', letter)



    for cargo in positions.values():
        print('cargo ---->', cargo)
        for (row, col) in cargo:
            print('row ---->', row)
            print('col ---->', col)
            trailer[y - col][x - row] = letter
        # print('positions[cargo] ---->', positions[cargo])

def print_trailer():
    for row in trailer:
        print(' '.join(row))

def main(entries):
    entries = entries.split(',')
    # positions = {}
    print('entries ---->', entries)
    for entry in entries:
        # print('entry ---->', entry)
        x_axis = int(entry[0])
        shape = entry[1]
        # print('x-axis:', x_axis, 'shape:', shape)
        get_cargo_positions(shape, x_axis)
    print_trailer()



# print(trailer)

main('7S')
# main('7S,7I,5Z')




# shape_pos = convert_shape_format(current_piece)

# # add piece to the grid for drawing
# for i in range(len(shape_pos)):
#     x, y = shape_pos[i]
#     if y > -1:
#         grid[y][x] = current_piece.color
