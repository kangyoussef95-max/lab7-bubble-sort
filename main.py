"""Bubble sort learning app with three visualization modes.

Provides core bubble sort implementation with non-visual, series (waterfall),
and in-place animation (carriage return) visualization options. Includes
input validation and CLI for interactive sorting.
"""

import sys
import time


def parse_user_input(raw_text: str) -> list[int]:
    """Convert comma-separated user text into a list of integers.

    Example: parse_user_input("5, 1, 4, 2") → [5, 1, 4, 2]
    Raises ValueError if input is invalid (empty values, non-integers).
    """
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
    
    Compares adjacent elements and swaps if out of order.
    After one pass, the largest unsorted value moves to index last_index.
    
    Args:
        values: list to sort (mutated in place)
        last_index: upper bound (exclusive) for comparisons
        
    Returns:
        True if any swap occurred, False if already sorted in range.
    """
    swapped = False
    for j in range(0, last_index):
        if values[j] > values[j + 1]:
            values[j], values[j + 1] = values[j + 1], values[j]
            swapped = True

    return swapped


def bubble_sort(values: list[int]) -> list[int]:
    """Sort values in ascending order using bubble sort (in-place).
    
    Runs up to n-1 passes, with early exit when no swaps occur.
    Time complexity: O(n²) worst case, O(n) best case (already sorted).
    Space complexity: O(1).
    """
    n = len(values)
    for i in range(n):
        swapped = bubble_sort_pass(values, n - i - 1)
        if not swapped:
            break

    return values


def format_swap_display(values: list[int], pass_num: int, pos_a: int, pos_b: int) -> str:
    """Return a formatted string showing bars and swap position (series mode).
    
    Generates horizontal bar chart with pass and swap position info.
    Bars are space-separated and scaled to fit terminal width.
    
    Example: "Pass 1, Swap at (0,1): [##      #   ]"
    """
    if not values:
        bars = ""
    else:
        max_bar_width = 40
        max_value = max(values)

        if max_value <= 0:
            bar_parts = [""] * len(values)
        else:
            scale = max_value / max_bar_width if max_value > max_bar_width else 1
            bar_parts = []

            for value in values:
                if value <= 0:
                    bar_parts.append("")
                else:
                    bar_length = max(1, round(value / scale))
                    bar_parts.append("#" * bar_length)

        bars = " ".join(bar_parts)

    return f"Pass {pass_num}, Swap at ({pos_a},{pos_b}): [{bars}]"


def bubble_sort_pass_visual(values: list[int], last_index: int, pass_num: int) -> bool:
    """Do one bubble pass with series visualization (waterfall dumps).
    
    Prints each swap on a new line showing bars and positions.
    This preserves full history of swaps in terminal output.
    """
    for j in range(0, last_index):
        if values[j] > values[j + 1]:
            values[j], values[j + 1] = values[j + 1], values[j]
            display = format_swap_display(values, pass_num, j, j + 1)
            print(display)
            swapped = True
    
    return swapped


def bubble_sort_visual(values: list[int]) -> list[int]:
    """Sort values with series visualization (waterfall mode).
    
    Each swap is printed on a new line for review and debugging.
    """
    n = len(values)
    for i in range(n):
        swapped = bubble_sort_pass_visual(values, n - i - 1, i + 1)
        if not swapped:
            break
    
    return values


def format_swap_display_animated(values: list[int], pass_num: int, pos_a: int, pos_b: int) -> str:
    """Return a single-line formatted string for in-place animation redraw.
    
    Optimized for carriage return (\r) redraws. Returns string starting with \r
    so it overwrites previous line in same terminal row, creating animation effect.
    
    Example: "\rPass 1, Swap at (0,1): [##      #   ]"
    """
    if not values:
        bars = ""
    else:
        max_bar_width = 50
        max_value = max(values)

        if max_value <= 0:
            bar_parts = [""] * len(values)
        else:
            scale = max_value / max_bar_width if max_value > max_bar_width else 1
            bar_parts = []

            for value in values:
                if value <= 0:
                    bar_parts.append("")
                else:
                    bar_length = max(1, round(value / scale))
                    bar_parts.append("#" * bar_length)

        bars = " ".join(bar_parts)

    return f"\rPass {pass_num}, Swap at ({pos_a},{pos_b}): [{bars}]"


def bubble_sort_pass_animated(values: list[int], last_index: int, pass_num: int, delay: float = 0.1) -> bool:
    """Do one bubble pass with in-place animation redraw (\\r carriage return).
    
    Each swap overwrites the previous line using carriage return, creating
    a smooth animation effect. Delay controls speed of animation.
    """
    for j in range(0, last_index):
        if values[j] > values[j + 1]:
            values[j], values[j + 1] = values[j + 1], values[j]
            display = format_swap_display_animated(values, pass_num, j, j + 1)
            print(display, end="", flush=True)
            sys.stdout.flush()
            time.sleep(delay)
            swapped = True

    if swapped:
        print()

    return swapped


def bubble_sort_animated(values: list[int], delay: float = 0.1) -> list[int]:
    """Sort values with in-place animation redraw (animation mode).
    
    Uses carriage return (\\r) to redraw bars on same terminal line,
    creating smooth animation effect. Adjustable delay for speed control.
    """
    n = len(values)
    for i in range(n):
        swapped = bubble_sort_pass_animated(values, n - i - 1, i + 1, delay)
        if not swapped:
            break

    return values


def main() -> None:
    """Interactive CLI for bubble sort with three visualization modes.
    
    Modes:
    1. No visualization - fast sort with no output
    2. Series (waterfall) - each swap on new line
    3. Animation - in-place redraw using carriage return
    """
    print("Bubble Sort Learning App")
    print("Enter numbers separated by commas (example: 5, 1, 4, 2)")

    while True:
        raw_text = input("Numbers: ")
        try:
            numbers = parse_user_input(raw_text)
            break
        except ValueError as error:
            print(f"Input error: {error}")
            print("Please try again.")
    print("1. No visualization")
    print("2. Series visualization (waterfall dumps)")
    print("3. In-place animation (redraws on same line)")
    viz_mode = input("Choose visualization mode (1-3): ").strip()

    if viz_mode == "2":
        sorted_numbers = bubble_sort_visual(numbers)
    elif viz_mode == "3":
        sorted_numbers = bubble_sort_animated(numbers)
    else:
        sorted_numbers = bubble_sort(numbers)

    print(f"Sorted: {sorted_numbers}")


if __name__ == "__main__":
    main()