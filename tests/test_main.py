import pytest

from main import bubble_sort, parse_user_input


def test_bubble_sort_empty_list() -> None:
    assert bubble_sort([]) == []


def test_bubble_sort_already_sorted() -> None:
    assert bubble_sort([1, 2, 3, 4]) == [1, 2, 3, 4]


def test_bubble_sort_reverse_sorted() -> None:
    assert bubble_sort([4, 3, 2, 1]) == [1, 2, 3, 4]


def test_bubble_sort_with_duplicates() -> None:
    assert bubble_sort([3, 1, 2, 1, 3]) == [1, 1, 2, 3, 3]


def test_parse_user_input_invalid_value_raises() -> None:
    with pytest.raises(ValueError):
        parse_user_input("1, two, 3")
