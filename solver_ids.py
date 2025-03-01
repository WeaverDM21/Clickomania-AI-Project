class IDSSolver:
    def __init__(self, problem, max_depth=15, verbosity=0, log_file="ids_log.txt"):
        self.problem = problem
        self.max_depth = max_depth
        self.verbosity = verbosity
        self.log_file = log_file

        with open(self.log_file, "w") as f:
            f.write("Iterative Deepening Search Log\n\n")

    def depth_limited_search(self, state, depth):
        # Solution found
        if state.is_solved():
            return []

        # No solution 
        if depth == 0:
            return None

        for move in state.get_possible_moves():
            new_state = state.copy()
            new_state.apply_move(move)

            if self.verbosity >= 2:
                with open(self.log_file, "a") as f:
                    f.write(f"Depth {depth}, Move: {move}\n{new_state}\n\n")

            result = self.depth_limited_search(new_state, depth - 1)

            # Path Found
            if result is not None:
                return [move] + result

        return None

    def solve(self):
        for depth in range(self.max_depth + 1):
            if self.verbosity >= 1:
                with open(self.log_file, "a") as f:
                    f.write(f"Trying depth {depth}\n")

            result = self.depth_limited_search(self.problem, depth)

            # Solution Found
            if result is not None:
                with open(self.log_file, "a") as f:
                    f.write(f"Solution found at depth {depth}: {result}\n")
                return result

        return None
