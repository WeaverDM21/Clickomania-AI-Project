import copy

class Clickomania:
    def __init__(self, grid):
        """Initialize the game board."""
        self.grid = grid
        self.rows = len(grid)
        self.cols = len(grid[0])

    def get_possible_moves(self):
        """Finds all valid moves (groups of same-colored adjacent blocks)."""
        visited = set()
        moves = []

        def bfs(start_row, start_col):
            """Finds all blocks connected to (start_row, start_col) of the same color."""
            queue = [(start_row, start_col)]
            color = self.grid[start_row][start_col]
            group = set(queue)

            while queue:
                r, c = queue.pop(0)
                for dr, dc in [(-1, 0), (1, 0), (0, -1), (0, 1)]:  # Up, Down, Left, Right
                    nr, nc = r + dr, c + dc
                    if (0 <= nr < self.rows and 0 <= nc < self.cols and
                            (nr, nc) not in visited and (nr, nc) not in group and
                            self.grid[nr][nc] == color):
                        queue.append((nr, nc))
                        group.add((nr, nc))

            return group if len(group) > 1 else None  # Only return valid groups

        # Find all groups of adjacent same-colored blocks
        for r in range(self.rows):
            for c in range(self.cols):
                if self.grid[r][c] != 0 and (r, c) not in visited:
                    group = bfs(r, c)
                    if group:
                        moves.append(group)
                        visited.update(group)

        return moves

    def apply_move(self, move):
        """Applies the move (removes blocks, shifts down, and shifts left)."""
        # 1. Remove the blocks
        for r, c in move:
            self.grid[r][c] = 0  # Set to empty

        # 2. Apply gravity (shift blocks down)
        for c in range(self.cols):
            non_zero_blocks = [self.grid[r][c] for r in range(self.rows) if self.grid[r][c] != 0]
            new_column = [0] * (self.rows - len(non_zero_blocks)) + non_zero_blocks
            for r in range(self.rows):
                self.grid[r][c] = new_column[r]

        # 3. Shift columns left if they become empty
        new_grid = []
        for c in range(self.cols):
            if any(self.grid[r][c] != 0 for r in range(self.rows)):  # If column is not empty
                new_grid.append([self.grid[r][c] for r in range(self.rows)])

        # Pad with empty columns to maintain grid shape
        while len(new_grid) < self.cols:
            new_grid.append([0] * self.rows)

        # Transpose back to original format
        for c in range(self.cols):
            for r in range(self.rows):
                self.grid[r][c] = new_grid[c][r]

    def has_adjacent_same_color(self, row, col):
        """
        Returns True if the block at (row, col) has at least one adjacent block of the same color.
        """
        color = self.grid[row][col]
        if color == 0:  # Empty space
            return False

        # Check up, down, left, right
        for dr, dc in [(-1, 0), (1, 0), (0, -1), (0, 1)]:
            nr, nc = row + dr, col + dc
            if 0 <= nr < len(self.grid) and 0 <= nc < len(self.grid[0]) and self.grid[nr][nc] == color:
                return True

        return False


    def is_solved(self):
        """Returns True if the board is completely cleared."""
        return all(cell == 0 for row in self.grid for cell in row)

    def copy(self):
        """Returns a deep copy of the board state."""
        return Clickomania(copy.deepcopy(self.grid))

    def __str__(self):
        """Returns a human-readable string representation."""
        return "\n".join(" ".join(str(cell) for cell in row) for row in self.grid)
