"""Pygame-based 2D visualization for bubble sort.

Displays array values as animated bars with color feedback:
- Blue: normal state
- Yellow: elements being compared
- Red: elements being swapped
- Green: correctly sorted elements
"""

import pygame
import sys


class BubbleSortVisualizer:
    """2D animated bubble sort visualizer using Pygame."""

    def __init__(self, values: list[int], width: int = 800, height: int = 600, fps: int = 60):
        """Initialize the visualizer.
        
        Args:
            values: list of integers to sort
            width: window width in pixels
            height: window height in pixels
            fps: frames per second for animation
        """
        self.values = values.copy()
        self.original_values = values.copy()
        self.width = width
        self.height = height
        self.fps = fps
        self.screen = None
        self.clock = None
        
        # Visualization state
        self.comparing_indices = []
        self.swapping_indices = []
        self.sorted_indices = set()
        self.current_pass = 0
        self.swap_count = 0
        self.comparison_count = 0
        self.is_sorting = False
        self.is_done = False
        
        # Colors
        self.COLOR_BG = (20, 20, 40)
        self.COLOR_BAR_DEFAULT = (70, 150, 200)
        self.COLOR_COMPARING = (255, 255, 0)
        self.COLOR_SWAPPING = (255, 50, 50)
        self.COLOR_SORTED = (50, 200, 100)
        
    def init_pygame(self) -> None:
        """Initialize Pygame and create window."""
        pygame.init()
        self.screen = pygame.display.set_mode((self.width, self.height))
        pygame.display.set_caption("Bubble Sort Visualizer")
        self.clock = pygame.time.Clock()
    
    def handle_events(self) -> bool:
        """Handle Pygame events. Return False to quit."""
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                return False
            elif event.type == pygame.KEYDOWN:
                if event.key == pygame.K_ESCAPE:
                    return False
        return True
    
    def draw_bars(self) -> None:
        """Draw bars representing array values."""
        if not self.values:
            return
        
        n = len(self.values)
        max_value = max(self.values)
        bar_width = (self.width - 40) / n
        bar_x_start = 20
        bar_y_bottom = self.height - 100
        max_bar_height = self.height - 150
        
        for i, value in enumerate(self.values):
            bar_height = (value / max_value) * max_bar_height if max_value > 0 else 10
            bar_x = bar_x_start + i * bar_width
            bar_y = bar_y_bottom - bar_height
            
            # Determine color
            if i in self.sorted_indices:
                color = self.COLOR_SORTED
            elif i in self.swapping_indices:
                color = self.COLOR_SWAPPING
            elif i in self.comparing_indices:
                color = self.COLOR_COMPARING
            else:
                color = self.COLOR_BAR_DEFAULT
            
            # Draw bar
            pygame.draw.rect(self.screen, color, (bar_x, bar_y, bar_width - 2, bar_height))
            
            # Draw value label (smaller font)
            font = pygame.font.Font(None, 24)
            text = font.render(str(value), True, (255, 255, 255))
            text_rect = text.get_rect(center=(bar_x + bar_width / 2, bar_y_bottom + 20))
            self.screen.blit(text, text_rect)
    
    def draw_info(self) -> None:
        """Draw sorting statistics and instructions."""
        font_title = pygame.font.Font(None, 28)
        font_text = pygame.font.Font(None, 20)
        
        # Create info strings
        status = "Sorting..." if self.is_sorting else ("Done!" if self.is_done else "Ready")
        info_lines = [
            f"Bubble Sort Visualization",
            f"Status: {status}",
            f"Pass: {self.current_pass}",
            f"Comparisons: {self.comparison_count}",
            f"Swaps: {self.swap_count}",
            f"ESC to quit",
        ]
        
        y_offset = 10
        for i, line in enumerate(info_lines):
            if i == 0:
                text = font_title.render(line, True, (200, 200, 255))
            else:
                text = font_text.render(line, True, (200, 200, 200))
            self.screen.blit(text, (10, y_offset))
            y_offset += 25
    
    def render(self) -> None:
        """Render one frame."""
        self.screen.fill(self.COLOR_BG)
        self.draw_bars()
        self.draw_info()
        pygame.display.flip()
    
    def bubble_sort_step(self) -> bool:
        """Perform one step of bubble sort. Return True if done."""
        n = len(self.values)
        
        if not hasattr(self, '_init_sort'):
            self._init_sort = True
            self._i = 0
            self._j = 0
            self._swapped = False
        
        # Outer loop: passes
        if self._i >= n:
            return True  # Done
        
        # Inner loop: comparisons within pass
        if self._j >= n - self._i - 1:
            self.current_pass = self._i
            if not self._swapped:
                # Mark remaining as sorted
                for k in range(n - self._i, n):
                    self.sorted_indices.add(k)
                return True
            else:
                # Mark newly sorted elements
                self.sorted_indices.add(n - self._i - 1)
                self._i += 1
                self._j = 0
                self._swapped = False
            return False
        
        # Perform comparison
        self.comparing_indices = [self._j, self._j + 1]
        
        if self.values[self._j] > self.values[self._j + 1]:
            # Swap
            self.swapping_indices = [self._j, self._j + 1]
            self.values[self._j], self.values[self._j + 1] = self.values[self._j + 1], self.values[self._j]
            self._swapped = True
            self.swap_count += 1
        
        self.comparison_count += 1
        self._j += 1
        
        return False
    
    def run(self) -> list[int]:
        """Run the visualization. Return sorted list."""
        self.init_pygame()
        self.is_sorting = True
        done_sorting = False
        
        try:
            while True:
                if not self.handle_events():
                    break
                
                if not done_sorting:
                    done_sorting = self.bubble_sort_step()
                    if done_sorting:
                        self.is_sorting = False
                        self.is_done = True
                        # Mark all as sorted
                        for i in range(len(self.values)):
                            self.sorted_indices.add(i)
                
                self.comparing_indices = []
                self.swapping_indices = []
                
                self.render()
                self.clock.tick(self.fps)
        finally:
            pygame.quit()
        
        return self.values


def visualize_bubble_sort(values: list[int], width: int = 800, height: int = 600, fps: int = 60) -> list[int]:
    """Convenience function to run bubble sort visualization.
    
    Args:
        values: list of integers to sort
        width: window width in pixels (default 800)
        height: window height in pixels (default 600)
        fps: animation speed in frames per second (default 60)
    
    Returns:
        sorted list
    """
    viz = BubbleSortVisualizer(values, width, height, fps)
    return viz.run()
