from heuristics import estimate_moves_remaining

class IDAStarSolver:
    def __init__(self, problem, max_depth=15, verbosity=0, log_file="idastar_log.txt"):
        self.problem = problem
        self.max_depth = max_depth
        self.verbosity = verbosity
        self.log_file = log_file
        self.nodes_expanded = 0
        self.peak_memory_usage = 0
        self.current_memory_usage = 0

        with open(self.log_file, "w") as f:
            f.write("IDA* Log\n\n")

    def search(self, state, g, threshold):
        f = g + estimate_moves_remaining(state)  # f = g + h
        
        self.nodes_expanded += 1
        self.current_memory_usage += 1
        self.peak_memory_usage = max(self.peak_memory_usage, self.current_memory_usage)

        # Return new threshold
        if f > threshold:
            self.current_memory_usage -= 1
            return f, None

        # Solution found
        if state.is_solved():
            self.current_memory_usage -= 1
            return 0, []

        min_threshold = float("inf")
        best_solution = None

        for move in state.get_possible_moves():
            new_state = state.copy()
            new_state.apply_move(move)

            if self.verbosity >= 2:
                with open(self.log_file, "a") as f:
                    f.write(f"Threshold {threshold}, Move: {move}\n{new_state}\n\n")

            cost, solution = self.search(new_state, g + 1, threshold)

            # Found a valid path
            if solution is not None:
                self.current_memory_usage -= 1
                return cost, [move] + solution  

            min_threshold = min(min_threshold, cost)

        self.current_memory_usage -= 1
        return min_threshold, None

    def solve(self):
        threshold = estimate_moves_remaining(self.problem)

        while threshold <= self.max_depth:
            if self.verbosity >= 1:
                with open(self.log_file, "a") as f:
                    f.write(f"Trying threshold {threshold}\n")

            cost, solution = self.search(self.problem, 0, threshold)

            # Solution found
            if solution is not None:
                with open(self.log_file, "a") as f:
                    f.write(f"Solution found at threshold {threshold}: {solution}\n")
                return solution

            # No solution possible
            if cost == float("inf"):
                return None  

            # Increase threshold
            threshold = cost  

        return None