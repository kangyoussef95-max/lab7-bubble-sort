# Bubble Sort Learning App

A beginner-friendly Python command-line app to practice bubble sort algorithm implementation with three interactive visualization modes: none, series (waterfall), and in-place animation.

## Features

- Four visualization modes for learning sorting behavior
- Accepts comma-separated integers from user input
- Robust input validation with friendly error messages
- Sorts numbers in ascending order using bubble sort
- Early-exit optimization (stops when sorted)
- 5 automated pytest tests
- Clean, well-documented code

## Project Structure

- `main.py`: application logic and CLI entry point
- `pygame_visualizer.py`: 2D Pygame visualization module (requires pygame)
- `tests/test_main.py`: pytest test suite (5 tests)
- `pytest.ini`: pytest discovery configuration
- `JOURNAL.md`: interaction/change log

## Requirements

- Python 3.10+ (project currently runs on Python 3.13)
- `pytest` for running tests
- `pygame` (optional, for 2D visualization mode)

## Setup

### Prerequisites
- Python 3.10+ (project currently runs on Python 3.13)

### Installation

1. **Create and activate a virtual environment** (recommended):

```powershell
python -m venv .venv
.\.venv\Scripts\Activate.ps1
```

2. **Install dependencies from requirements.txt**:

```powershell
pip install -r requirements.txt
```

This installs:
- `pytest==9.0.2` - Testing framework for running automated tests
- `pygame==2.6.1` - 2D graphics library for Mode 4 visualization (optional but recommended)

**Alternative:** If you only want to run without visualizations:
```powershell
pip install pytest
```

### Verify Installation

Test that everything is working:

```powershell
pytest
```

You should see `5 passed` in the output.

## Run the App

```powershell
python main.py
```

### Example Session

**Input:**
```text
Numbers: 5, 1, 4, 2
Choose visualization mode (1-3): 3
```

**Output (Mode 3: Animation):**
```
Pass 1, Swap at (0,1): [# #    ##   ]
Pass 1, Swap at (1,2): [#  #   ##   ]
Pass 1, Swap at (2,3): [#  #  ## ]
Pass 2, Swap at (0,1): [#  #   ## ]
Sorted: [1, 2, 4, 5]
```

## Visualization Modes

The app offers three visualization approaches:

### Mode 1: No Visualization
- Fast execution with only final result output
- Best for: checking correctness quickly, large lists
- Output: `Sorted: [1, 2, 4, 5]`

### Mode 2: Series (Waterfall)
- Each swap prints on a new line
- Shows full history of all swaps for debugging
- Best for: understanding swap sequence, learning how passes work
- Output: Multiple lines with pass numbers and bar charts

### Mode 3: In-Place Animation
- Each swap redraws on the same terminal line using carriage return (`\r`)
- Creates smooth animation effect
- Delay: 0.1s per swap (can be customized)
- Best for: visual learners, interactive demos
- Terminal requirement: supports carriage return (most modern terminals)

### Mode 4: Pygame 2D Visualization (Requires pygame)
- Full 2D graphics window with animated bar charts
- Color feedback:
  - Blue: normal state
  - Yellow: elements being compared
  - Red: elements being swapped
  - Green: correctly sorted elements
- Real-time statistics: pass number, comparison/swap count
- Smooth animations for swap operations
- Best for: visual learners, understanding algorithm flow, demos
- Window interaction: close window or press ESC to finish
- Performance: ~60 FPS animation (configurable)



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

### Core Algorithm
- Bubble sort compares adjacent values and swaps out-of-order pairs
- After each pass, the largest unsorted value moves to its final position
- Early-exit optimization reduces passes when list becomes sorted

### Complexity
- Worst-case time complexity: O(n²) (reverse sorted list)
- Best-case time complexity: O(n) (already sorted, with early exit)
- Space complexity: O(1) (in-place sorting)

### Code Organization
**Core functions** (non-visual):
- `parse_user_input()` - input validation
- `bubble_sort_pass()` - single comparison pass
- `bubble_sort()` - full sort algorithm

**Visualization functions** (series mode):
- `format_swap_display()` - bar chart renderer
- `bubble_sort_pass_visual()` - pass with output
- `bubble_sort_visual()` - full sort with series output

**Animation functions** (carriage return mode):
- `format_swap_display_animated()` - single-line renderer
- `bubble_sort_pass_animated()` - pass with animation
- `bubble_sort_animated()` - full sort with animation

**2D Graphics** (separate module: `pygame_visualizer.py`):
- `BubbleSortVisualizer` class - Pygame window management and rendering
- `visualize_bubble_sort()` - convenience function to run visualization
- Color-coded bars with real-time statistics display

### Terminal Tips
- Animation mode works best in modern terminals (Windows 10+, macOS, Linux)
- Older terminals may show jumbled output with animation—use Series mode instead
- Adjust `delay` parameter for faster/slower animation

## Future Improvements

- Add tests for `parse_user_input` with valid inputs and empty input
- Add property-based tests for sorting behavior
- Separate CLI and core logic into modules for scalability
