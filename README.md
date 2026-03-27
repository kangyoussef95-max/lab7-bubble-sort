# Bubble Sort Learning App

A beginner-friendly Python command-line app to practice bubble sort, input parsing, and basic automated testing with pytest.

## Features

- Accepts comma-separated integers from user input
- Validates input and shows friendly error messages
- Sorts numbers in ascending order using bubble sort
- Uses early-exit optimization (`swapped` flag)
- Includes 5 basic pytest tests

## Project Structure

- `main.py`: application logic and CLI entry point
- `tests/test_main.py`: pytest test suite (5 tests)
- `pytest.ini`: pytest discovery configuration
- `JOURNAL.md`: interaction/change log

## Requirements

- Python 3.10+ (project currently runs on Python 3.13)
- `pytest` for running tests

## Setup

Create and activate a virtual environment (recommended):

```powershell
python -m venv .venv
.\.venv\Scripts\Activate.ps1
```

Install test dependency:

```powershell
pip install pytest
```

## Run the App

```powershell
python main.py
```

Example input:

```text
5, 1, 4, 2
```

Example output:

```text
Sorted: [1, 2, 4, 5]
```

## Run Tests

Run all tests:

```powershell
python -m pytest -q
```

You should see output similar to:

```text
.....                                                                    [100%]
5 passed
```

## Learning Notes

- Bubble sort compares adjacent values and swaps out-of-order pairs.
- After each pass, the largest unsorted value moves to the end.
- Worst-case time complexity: O(n^2)
- Best-case (already sorted with early exit): O(n)
- Space complexity: O(1)

## Future Improvements

- Add tests for `parse_user_input` with valid inputs and empty input
- Add property-based tests for sorting behavior
- Separate CLI and core logic into modules for scalability
