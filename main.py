WIDTH = 10
HEIGHT = 53
EMPTY = '_'

valid_letters = {'O', 'I', 'S', 'Z', 'L', 'J', 'T'}

deltas = {'O': [(0, 0), (0, -1), (1, 0), (1, -1)],
                'I': [(0, 0), (0, -1), (0, -2), (0, -3)],
                'S': [(0, 0), (1, 0), (1, -1), (2, -1)],
                'Z': [(0, 0), (1, 0), (1, 1), (2, 1)],
                'L': [(0, 0), (0, -1), (0, -2), (1, 0)],
                'J': [(0, 0), (1, 0), (1, -1), (1, -2)],
                'T': [(0, 0), (1, 0), (2, 0), (1, 1)]}

trailer = [[EMPTY] * WIDTH for _ in range(HEIGHT)]

def main(entries):
    """
    Loads cargo into the trailer based on input entries and calculates the highest
    0-indexed y-coordinate that has an occupied square.

    Args:
        entries (str): A comma-separated string of cargo entries (e.g., "0O,2I,3S").

    Returns:
        positive int or -1: The highest 0-indexed y-coordinate with occupied cargo squares, or
        -1 if there was an issue with the input or loading process.
    """

    if not entries.strip():
        return -1

    entries = entries.strip().split(',')

    print('entries ---->', entries)
    lowest_y = float('inf')
    for entry in entries:
        print('entry ---->', entry)
        if len(entry) != 2:
            return -1
        x = int(entry[:-1])
        letter = entry[-1]
        print('x-axis:', x, 'letter:', letter)
        lowest_y = fill_trailer(trailer, letter, x, lowest_y)
    print_trailer()

    if lowest_y is None:
        return -1

    return HEIGHT - 1 - lowest_y


def fill_trailer(trailer, letter, x, lowest_y):
    """
    Fill the trailer with cargo at a specific position.

    Args:
        trailer ([list]): The trailer grid.
        letter (str): The cargo letter (e.g., 'Z').
        x (int): The x-coordinate where cargo will be placed.
        lowest_y (int): The lowest occupied y-coordinate.

    Returns:
        int or None: The updated lowest occupied y-coordinate if cargo is placed successfully,
        or None if the operation fails (invalid input, overflow, etc.).
    """

    if letter not in valid_letters:
        return None
    if not 0 <= x <= 9:
        return None

    start_pos = get_valid_start(trailer, letter, x, HEIGHT - 1)

    if start_pos is None:
        return None

    x, y = start_pos

    print('x:', x)
    print('y:', y)
    print('letter ---->', letter)
    print('lowest_y ---->', lowest_y)
    for delta in deltas[letter]:
        delta_column, delta_row = delta
        # print('delta_column ---->', delta_column)
        # print('delta_row ---->', delta_row)
        trailer_row = y + delta_row
        trailer_column = x + delta_column
        trailer[trailer_row][trailer_column] = letter
        print('lowest_y ---->', lowest_y)
        if trailer_row < lowest_y:
            lowest_y = trailer_row
        if lowest_y < 0 or lowest_y == float('inf'):
            return None
    print('lowest_y ---->', lowest_y)
    return lowest_y


def get_valid_start(trailer, letter, x, y):
    """
    Find a valid starting position for a given cargo letter within the trailer.

    Args:
        trailer ([list]): The trailer grid.
        letter (str): The cargo letter (e.g., 'Z').
        x (int): The x-coordinate where cargo will be placed.
        y (int): The y-coordinate to start searching for a valid position.

    Returns:
        Tuple[int, int] or None: A tuple representing the starting (x, y) position if found,
        or None if no valid position is available.
    """

    while y >= 0:
        all_positions_valid = True

        for delta in deltas[letter]:
            # print('delta ---->', delta)
            delta_row, delta_column = delta
            # print('delta_row ---->', delta_row)
            # print('delta_column ---->', delta_column)
            trailer_column = x + delta_row
            trailer_row = y + delta_column
            # print('trailer_column ---->', trailer_column)
            print('trailer_row ---->', trailer_row)
            row_inbounds = 0 <= trailer_column < WIDTH
            column_inbounds = 0 <= trailer_row < HEIGHT

            if not (row_inbounds and column_inbounds and trailer[trailer_row][trailer_column] == '_'):
                # print('Invalid position found:', trailer_column, trailer_row)
                all_positions_valid = False
                break

        if all_positions_valid:
            return x, y

        y -= 1
    return None


def print_trailer():
    for row in trailer:
        print(' '.join(row))


def clear_trailer():
    global trailer
    trailer = [[EMPTY] * WIDTH for _ in range(HEIGHT)]


# # Test Cases
# print(main('0O,2I,3S'))
# print(main('7S,7I,5Z'))
# print(main('5I,5I,5I,5I,5I,5I,5I,5I,5I,5I,5I,5I,5I'))
# print(main('5I,5I,5I,5I,5I,5I,5I,5I,5I,5I,5I,5I,5I,5I'))
# print(main('-6Z'))
# print(main('10Z'))
# print(main('5A'))
# print(main('7T'))
# print(main('8T'))
# print(main(''))
# print(main('   '))
# print(main('5'))
# print(main('Z'))
# print(main('5Z'))
# print(main('5T,5I,2O,3S,7Z,1J,4L,7T,9I,3O,5Z,2L,3T,2Z,7S,1I,1T,4L,6J'))
