class IDSSolver:
    def __init__(self, problem, max_depth=15, verbosity=0, log_file="ids_log.txt"):
        self.problem = problem
        self.max_depth = max_depth
        self.verbosity = verbosity
        self.log_file = log_file
        self.nodes_expanded = 0  # Tracks the number of nodes expanded
        self.peak_memory = 0  # Tracks peak memory usage (max stored states at any point)
        self.current_memory = 0  # Current number of stored states

        with open(self.log_file, "w") as f:
            f.write("Iterative Deepening Search Log\n\n")

    def depth_limited_search(self, state, depth):
        self.nodes_expanded += 1  # Increment nodes expanded
        self.current_memory += 1  # Increase stored states
        self.peak_memory = max(self.peak_memory, self.current_memory)

        # Solution found
        if state.is_solved():
            self.current_memory -= 1  # Decrement stored states when backtracking
            return []

        # No solution possible at this depth
        if depth == 0:
            self.current_memory -= 1  # Decrement stored states when backtracking
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
                self.current_memory -= 1  # Decrement stored states when backtracking
                return [move] + result

        self.current_memory -= 1  # Decrement stored states when backtracking
        return None

    def solve(self):
        for depth in range(self.max_depth + 1):
            if self.verbosity >= 1:
                with open(self.log_file, "a") as f:
                    f.write(f"Trying depth {depth}\n")

            # Reset counters for each depth iteration
            self.nodes_expanded = 0
            self.peak_memory = 0
            result = self.depth_limited_search(self.problem, depth)

            # Solution Found
            if result is not None:
                with open(self.log_file, "a") as f:
                    f.write(f"Solution found at depth {depth}: {result}\n")
                    f.write(f"Nodes expanded: {self.nodes_expanded}\n")
                    f.write(f"Peak memory usage: {self.peak_memory}\n")
                return result, self.nodes_expanded, self.peak_memory

        return None, self.nodes_expanded, self.peak_memory
