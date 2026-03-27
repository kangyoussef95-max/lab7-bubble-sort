"""Bubble sort learning scaffold.

This file is intentionally written as a guided skeleton with TODOs.
Complete each TODO in order to build your own working app.
"""


def parse_user_input(raw_text: str) -> list[int]:
    """Convert comma-separated user text into a list of integers.

    Example input: "5, 1, 4, 2"
    """
    # TODO 1: 
    # 1) Split raw_text by commas.
    # 2) Strip spaces from each item.
    # 3) Convert each item to int.
    # 4) Return the final list.
    # Hint: Start with: parts = raw_text.split(",")
    if raw_text.strip() == "":
        return []
    parts = raw_text.split(",")
    numbers = [int(item.strip()) for item in parts]
    return numbers


def bubble_sort_pass(values: list[int], last_index: int) -> bool:
    """Do one left-to-right bubble pass up to last_index.

    Return True if at least one swap happened, otherwise False.
    """
    swapped = False

    # TODO 2:
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

    # TODO 3:
    # Run multiple passes with i from 0 to n - 1.
    # On pass i, call bubble_sort_pass(values, n - i - 1).
    # If no swaps happened on a pass, break early.
    for i in range(n):
        bubble_sort_pass(values, n - i - 1)
        if not bubble_sort_pass(values, n - i - 1):
            break

    return values


def main() -> None:
    """Simple CLI app entry point."""
    print("Bubble Sort Learning App")
    print("Enter numbers separated by commas (example: 5, 1, 4, 2)")

    raw_text = input("Numbers: ")

    # TODO 4:
    # Use parse_user_input(raw_text) to get a list of ints.
    # Store it in a variable, for example: numbers.
    raise NotImplementedError("TODO 4: parse and store input list")

    # TODO 5:
    # Call bubble_sort(numbers) and print the result.
    # Example output: Sorted: [1, 2, 4, 5]


if __name__ == "__main__":
    main()
