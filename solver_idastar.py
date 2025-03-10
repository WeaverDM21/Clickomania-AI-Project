from heuristics import estimate_moves_remaining

class IDAStarSolver:
    def __init__(self, problem, max_depth=15, verbosity=0, log_file="idastar_log.txt"):
        self.problem = problem # Game board
        self.max_depth = max_depth # Maximum depth to search
        self.verbosity = verbosity # Level for data display
        self.log_file = log_file # Stores the data collected
        self.nodes_expanded = 0 # Tracks the number of nodes expanded
        self.peak_memory_usage = 0 # Tracks peak memory usage (max stored states at any point)
        self.current_memory_usage = 0 # Current number of stored states

        with open(self.log_file, "w") as f:
            f.write("IDA* Log\n\n")

    def search(self, state, g, threshold):
        f = g + estimate_moves_remaining(state)  # f = g + h
        
        self.nodes_expanded += 1 # Increment nodes expanded
        self.current_memory_usage += 1 # Increment stored states
        self.peak_memory_usage = max(self.peak_memory_usage, self.current_memory_usage) # Update peak memory usage

        # Return new threshold
        if f > threshold:
            self.current_memory_usage -= 1
            return f, None

        # Solution found
        if state.is_solved():
            self.current_memory_usage -= 1
            return 0, []

        min_threshold = float("inf") # Initialize minimum threshold

        for move in state.get_possible_moves(): # Get all possible moves
            new_state = state.copy() # Copy the current state
            new_state.apply_move(move) # Apply the move

            if self.verbosity >= 2:
                with open(self.log_file, "a") as f:
                    f.write(f"Threshold {threshold}, Move: {move}\n{new_state}\n\n")

            cost, solution = self.search(new_state, g + 1, threshold) # Recursively search

            # Found a valid path
            if solution is not None:
                self.current_memory_usage -= 1
                return cost, [move] + solution  

            min_threshold = min(min_threshold, cost) # Update threshold

        self.current_memory_usage -= 1
        return min_threshold, None

    def solve(self):
        threshold = estimate_moves_remaining(self.problem) # Initial threshold

        while threshold <= self.max_depth: # Iterate until threshold exceeds max depth
            if self.verbosity >= 1:
                with open(self.log_file, "a") as f:
                    f.write(f"Trying threshold {threshold}\n")

            cost, solution = self.search(self.problem, 0, threshold) # Start search

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

        # No solution found
        return None