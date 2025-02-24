def estimate_moves_remaining(state):
    """Estimate the number of moves required to solve the board."""
    groups = state.get_possible_moves()
    num_isolated_blocks = sum(1 for row in state.grid for cell in row if cell != 0 and not state.has_adjacent_same_color(row, cell))
    return len(groups) + num_isolated_blocks  # Simple non-admissible heuristic
