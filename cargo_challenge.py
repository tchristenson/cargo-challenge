WIDTH = 10
HEIGHT = 53
EMPTY = 'O'
CARGO = 'X'

trailer = [[EMPTY] * WIDTH for _ in range(HEIGHT)]

def print_trailer():
    for row in trailer:
        print(' '.join(row))

# print_trailer()
# print(trailer)
