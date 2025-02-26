from heuristics import estimate_moves_remaining

class IDAStarSolver:
    def __init__(self, problem, max_depth=15, verbosity=0):
        self.problem = problem
        self.max_depth = max_depth
        self.verbosity = verbosity

    def search(self, state, g, threshold):
        """Performs a depth-first search with pruning based on f = g + h."""
        f = g + estimate_moves_remaining(state)  # f = g + h

        if f > threshold:
            return f, None  # Return the new threshold

        if state.is_solved():
            return 0, []  # Solution found

        min_threshold = float("inf")
        best_solution = None

        print(state)
        print()

        for move in state.get_possible_moves():
            new_state = state.copy()
            new_state.apply_move(move)
            print(new_state)
            print()

            cost, solution = self.search(new_state, g + 1, threshold)
            
            if solution is not None:
                return cost, [move] + solution  # Found a valid path
            
            min_threshold = min(min_threshold, cost)

        return min_threshold, None

    def solve(self):
        """Run IDA* until a solution is found or max depth is reached."""
        threshold = estimate_moves_remaining(self.problem)

        while threshold <= self.max_depth:
            if self.verbosity > 0:
                print(f"Trying threshold {threshold}")

            cost, solution = self.search(self.problem, 0, threshold)

            if solution is not None:
                return solution  # Solution found

            if cost == float("inf"):
                return None  # No solution possible

            threshold = cost  # Increase threshold

        return None
