"""Bubble sort learning scaffold.

This file is intentionally written as a guided skeleton with TODOs.
Complete each TODO in order to build your own working app.
"""

import sys
import time


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


def format_swap_display(values: list[int], pass_num: int, pos_a: int, pos_b: int) -> str:
    """Return a formatted string showing bars and swap position.
    
    Example output: "Pass 1, Swap at (0,1): [##      #   ]"
    
    Args:
        values: current list of integers
        pass_num: which pass number (1-indexed)
        pos_a: first index being swapped
        pos_b: second index being swapped
    
    Returns:
        Formatted string with pass info, swap positions, and bar chart.
    """
    # TODO: Visualization Step 1
    # 1) Generate bar chart from values (each # represents one unit).
    # 2) Handle scaling if max value is large (e.g., keep bars under 40 chars).
    # 3) Return format: f"Pass {pass_num}, Swap at ({pos_a},{pos_b}): [{bars}]"
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
    """Do one bubble pass with visualization of each swap.
    
    Returns True if at least one swap happened, otherwise False.
    """
    swapped = False

    # TODO: Visualization Step 2
    # 1) Loop j from 0 to last_index - 1.
    # 2) Compare values[j] and values[j + 1].
    # 3) If swap needed:
    #    a) Perform the swap.
    #    b) Call format_swap_display(...) to get the display string.
    #    c) Print the string.
    #    d) Set swapped = True.
    for j in range(0, last_index):
        if values[j] > values[j + 1]:
            values[j], values[j + 1] = values[j + 1], values[j]
            display = format_swap_display(values, pass_num, j, j + 1)
            print(display)
            swapped = True
    
    return swapped


def bubble_sort_visual(values: list[int]) -> list[int]:
    """Sort values with visualization of every swap."""
    n = len(values)

    # TODO: Visualization Step 3
    # Run multiple passes (similar to bubble_sort).
    # On pass i, call bubble_sort_pass_visual(values, n - i - 1, i + 1).
    # If no swaps happened on a pass, break early.
    for i in range(n):
        swapped = bubble_sort_pass_visual(values, n - i - 1, i + 1)
        if not swapped:
            break
    
    return values


def format_swap_display_animated(values: list[int], pass_num: int, pos_a: int, pos_b: int) -> str:
    """Return a single-line formatted string for in-place animation redraw.
    
    Similar to format_swap_display but optimized for \r carriage return redraws.
    No newline at end—meant to be overwritten.
    
    Example output: "Pass 1, Swap at (0,1): [##      #   ]"
    """
    # TODO: Animated Step 1
    # 1) Generate bar chart from values (reuse scaling logic if possible).
    # 2) Keep bars under fixed width for consistent redraw (e.g., 50 chars total).
    # 3) Return format string without trailing newline for \r redraw.
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
    """Do one bubble pass with in-place animation using \\r carriage return.
    
    Returns True if at least one swap happened, otherwise False.
    """
    swapped = False

    # TODO: Animated Step 2
    # 1) Loop j from 0 to last_index - 1.
    # 2) Compare values[j] and values[j + 1].
    # 3) If swap needed:
    #    a) Perform the swap.
    #    b) Call format_swap_display_animated(...) to get the display string.
    #    c) Print display string with end="", flush=True, then sys.stdout.flush().
    #    d) Import time and time.sleep(delay) for animation speed.
    #    e) Set swapped = True.
    # 4) After swap, print newline so next output starts fresh.
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
    """Sort values with in-place animation for each swap.
    
    Uses \\r carriage return to redraw bars on same line, creating animation effect.
    """
    n = len(values)

    # TODO: Animated Step 3
    # 1) Run multiple passes with i from 0 to n - 1.
    # 2) On pass i, call bubble_sort_pass_animated(values, n - i - 1, i + 1, delay).
    # 3) If no swaps happened on a pass, break early.
    # 4) After last swap of a pass, print a newline so "Sorted: ..." starts fresh.
    for i in range(n):
        swapped = bubble_sort_pass_animated(values, n - i - 1, i + 1, delay)
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

    # TODO: Animated Step 4
    # 1) Print menu options:
    #    - "1. No visualization"
    #    - "2. Series visualization (waterfall dumps)"
    #    - "3. In-place animation (redraws on same line)"
    # 2) Ask user: "Choose visualization mode (1-3): "
    # 3) Store response in a variable, for example: viz_mode.
    # 4) Route to appropriate sort function:
    #    - Mode 1: call bubble_sort(numbers)
    #    - Mode 2: call bubble_sort_visual(numbers)
    #    - Mode 3: call bubble_sort_animated(numbers)
    # 5) Print the sorted result.
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