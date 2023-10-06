WIDTH = 10
HEIGHT = 53
EMPTY = '_'
CARGO = 'X'

# Cargo Shapes
O = [
    ['X', 'X',
     'X', 'X'],
]

I = [
    ['X',
     'X',
     'X',
     'X'],
]

S = [
    ['_', 'X', 'X',
     'X', 'X', '_'],
]

Z = [
    ['X', 'X', '_',
     '_', 'X', 'X'],
]

L = [
    ['X', '_',
     'X', '_',
     'X', 'X'],
]

J = [
    ['_', 'X',
     '_', 'X',
     'X', 'X'],
]

T = [
    ['X', 'X', 'X',
     '_', 'X', '_',
     '_', 'X', '_'],
]

cargo_shapes = [O, I, S, Z, L, J, T]

trailer = [[EMPTY] * WIDTH for _ in range(HEIGHT)]

def fill_trailer(entries):
    entries = entries.split(',')
    print('entries ---->', entries)
    for entry in entries:
        # print('entry ---->', entry)
        x_axis = int(entry[0])
        shape = entry[1]
        print('x-axis:', x_axis, 'shape:', shape)



def print_trailer():
    for row in trailer:
        print(' '.join(row))

# print_trailer()
# print(trailer)

fill_trailer('3O,9I,0J')
