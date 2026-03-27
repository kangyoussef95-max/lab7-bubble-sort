"""Bubble sort learning scaffold.

This file is intentionally written as a guided skeleton with TODOs.
Complete each TODO in order to build your own working app.
"""


def parse_user_input(raw_text: str) -> list[int]:
    """Convert comma-separated user text into a list of integers.

    Example input: "5, 1, 4, 2"
    """
    # Done:
    # 1) Split raw_text by commas.
    # 2) Strip spaces from each item.
    # 3) Convert each item to int.
    # 4) Return the final list.
    # Hint: Start with: parts = raw_text.split(",")
    if raw_text.strip() == "":
        return []

    parts = raw_text.split(",")
    numbers = []

    for item in parts:
        item = item.strip()

        if item == "":
            raise ValueError("Empty value found. Please enter only numbers separated by commas.")

        try:
            numbers.append(int(item))
        except ValueError:
            raise ValueError(f"Invalid number: '{item}'. Please enter integers only.")

    return numbers


def bubble_sort_pass(values: list[int], last_index: int) -> bool:
    """Do one left-to-right bubble pass up to last_index.

    Return True if at least one swap happened, otherwise False.
    """
    swapped = False

    # Done:
    # Loop j from 0 to last_index - 1.
    # Compare values[j] and values[j + 1].
    # If left > right, swap them and set swapped = True.
    for j in range(0, last_index):
        if values[j] > values[j + 1]:
            values[j], values[j + 1] = values[j + 1], values[j]
            swapped = True

    return swapped


def bubble_sort(values: list[int]) -> list[int]:
    """Sort values in ascending order using bubble sort and return it."""
    n = len(values)

    # Done:
    # Run multiple passes with i from 0 to n - 1.
    # On pass i, call bubble_sort_pass(values, n - i - 1).
    # If no swaps happened on a pass, break early.
    for i in range(n):
        swapped = bubble_sort_pass(values, n - i - 1)
        if not swapped:
            break

    return values


def main() -> None:
    """Simple CLI app entry point."""
    print("Bubble Sort Learning App")
    print("Enter numbers separated by commas (example: 5, 1, 4, 2)")

    while True:
        raw_text = input("Numbers: ")

        # Done:
        # Use parse_user_input(raw_text) to get a list of ints.
        # Store it in a variable, for example: numbers.
        try:
            numbers = parse_user_input(raw_text)
            break
        except ValueError as error:
            print(f"Input error: {error}")
            print("Please try again.")

    # Done:
    # Call bubble_sort(numbers) and print the result.
    # Example output: Sorted: [1, 2, 4, 5]
    sorted_numbers = bubble_sort(numbers)
    print(f"Sorted: {sorted_numbers}")


def test_empty_list() -> None:
    assert bubble_sort([]) == []


def test_already_sorted() -> None:
    assert bubble_sort([1, 2, 3, 4]) == [1, 2, 3, 4]


def test_reverse_sorted() -> None:
    assert bubble_sort([4, 3, 2, 1]) == [1, 2, 3, 4]


def test_duplicates() -> None:
    assert bubble_sort([3, 1, 2, 1, 3]) == [1, 1, 2, 3, 3]


def test_invalid_input() -> None:
    try:
        parse_user_input("1, 2, , 4")
        assert False
    except ValueError:
        assert True

    try:
        parse_user_input("1, two, 3")
        assert False
    except ValueError:
        assert True


if __name__ == "__main__":
    main()