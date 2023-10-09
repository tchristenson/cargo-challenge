from main import get_valid_start, fill_trailer, main, WIDTH, HEIGHT, EMPTY

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
    entries_1 = "0O,2I,3S"
    expected_result_1 = 3
    assert main(entries_1) == expected_result_1

    entries_2 = "7S,7I,5Z"
    expected_result_2 = 6
    assert main(entries_2) == expected_result_2

if __name__ == "__main__":
    test_get_valid_start()
    test_fill_trailer()
    test_main()
