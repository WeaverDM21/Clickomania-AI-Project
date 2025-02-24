from clickomania import Clickomania

def estimate_moves_remaining(problem):
    """
    Estimates the number of remaining moves required to clear the board.
    - Penalizes isolated blocks.
    - Considers the number of big color groups.
    """
    grid = problem.grid
    isolated_blocks = 0
    color_groups = {}

    for r in range(len(grid)):
        for c in range(len(grid[0])):
            color = grid[r][c]
            if color != 0:
                if not problem.has_adjacent_same_color(r, c):
                    isolated_blocks += 1
                else:
                    if color not in color_groups:
                        color_groups[color] = 0
                    color_groups[color] += 1

    # Fewer groups = better; more isolated blocks = worse
    return len(color_groups) + isolated_blocks * 2
