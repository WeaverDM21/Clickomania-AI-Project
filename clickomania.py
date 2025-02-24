import copy

class Clickomania:
    def __init__(self, grid):
        self.grid = grid  # 2D list representing the board
    
    def get_possible_moves(self):
        """Find all valid moves (groups of same-colored adjacent blocks)."""
        # Implement BFS/DFS to find connected components
        pass
    
    def apply_move(self, move):
        """Apply a move to the board, update the state."""
        # Remove blocks, apply gravity, shift columns left
        pass
    
    def is_solved(self):
        """Check if the board is completely cleared."""
        return all(cell == 0 for row in self.grid for cell in row)
    
    def copy(self):
        """Return a deep copy of the board state."""
        return copy.deepcopy(self)
    
    def __str__(self):
        """Return a human-readable string representation."""
        return "\n".join(" ".join(str(cell) for cell in row) for row in self.grid)
