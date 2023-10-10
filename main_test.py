from main import get_valid_start, fill_trailer, main, clear_trailer, WIDTH, HEIGHT, EMPTY

def test_get_valid_start():
    trailer = [[EMPTY] * WIDTH for _ in range(HEIGHT)]

    # Valid
    assert get_valid_start(trailer, 'O', 0, HEIGHT - 1) == (0, HEIGHT - 1)
    # Invalid
    assert get_valid_start(trailer, 'O', 0, 0) is None


def test_fill_trailer():
    trailer = [[EMPTY] * WIDTH for _ in range(HEIGHT)]

    # Valid
    assert fill_trailer(trailer, 'O', 0, float('inf')) == 51
    # Invalid
    assert fill_trailer(trailer, 'X', 0, float('inf')) is None


def test_main():
    # Valid
    clear_trailer()
    entries_1 = "0O,2I,3S"
    expected_result_1 = 3
    assert main(entries_1) == expected_result_1

    # Valid
    clear_trailer()
    entries_2 = "7S,7I,5Z"
    expected_result_2 = 6
    assert main(entries_2) == expected_result_2

    # Valid
    clear_trailer()
    entries_3 = "5I,5I,5I,5I,5I,5I,5I,5I,5I,5I,5I,5I,5I"
    expected_result_3 = 51
    assert main(entries_3) == expected_result_3

    # Invalid - overflows trailer vertically
    clear_trailer()
    entries_4 = "5I,5I,5I,5I,5I,5I,5I,5I,5I,5I,5I,5I,5I,5I"
    expected_result_4 = -1
    assert main(entries_4) == expected_result_4

    # Invalid - negative x value
    clear_trailer()
    entries_5 = "-6Z"
    expected_result_5 = -1
    assert main(entries_5) == expected_result_5

    # Invalid - x value greater than 9
    clear_trailer()
    entries_6 = "10Z"
    expected_result_6 = -1
    assert main(entries_6) == expected_result_6

    # Invalid - letter not in valid letters
    clear_trailer()
    entries_7 = "5A"
    expected_result_7 = -1
    assert main(entries_7) == expected_result_7

    # Valid
    clear_trailer()
    entries_8 = "7T"
    expected_result_8 = 1
    assert main(entries_8) == expected_result_8

    # Invalid - selected letter overflows trailer horizontally at provided x coordinate
    clear_trailer()
    entries_9 = "8T"
    expected_result_9 = -1
    assert main(entries_9) == expected_result_9

    # Invalid - empty string passed as the cargo entries
    clear_trailer()
    entries_10 = ""
    expected_result_10 = -1
    assert main(entries_10) == expected_result_10

    # Invalid - spaces passed as the cargo entries
    clear_trailer()
    entries_11 = "   "
    expected_result_11 = -1
    assert main(entries_11) == expected_result_11

    # Invalid - incorrect entry (excludes cargo type)
    clear_trailer()
    entries_12 = "5"
    expected_result_12 = -1
    assert main(entries_12) == expected_result_12

    # Invalid - incorrect entry (excludes x axis)
    clear_trailer()
    entries_13 = "Z"
    expected_result_13 = -1
    assert main(entries_13) == expected_result_13

    # Valid
    clear_trailer()
    entries_14 = "5Z"
    expected_result_14 = 1
    assert main(entries_14) == expected_result_14

    # Valid
    clear_trailer()
    entries_15 = "5T,5I,2O,3S,7Z,1J,4L,7T,9I,3O,5Z,2L,3T,2Z,7S,1I,1T,4L,6J,0O"
    expected_result_15 = 12
    assert main(entries_15) == expected_result_15

if __name__ == "__main__":
    test_get_valid_start()
    test_fill_trailer()
    test_main()
