from clickomania import Clickomania
from solver_idastar import IDAStarSolver
from solver_ids import IDSSolver
import time;
import random;

def generate_solvable_board(size, colors=5):
    board = [[0] * size for _ in range(size)]  # Empty board

    def get_neighbors(x, y):
        neighbors = []
        if x > 0: neighbors.append((x - 1, y))
        if x < size - 1: neighbors.append((x + 1, y))
        if y > 0: neighbors.append((x, y - 1))
        if y < size - 1: neighbors.append((x, y + 1))
        return neighbors

    def place_cluster(x, y, color, cluster_size=2):
        stack = [(x, y)]
        board[x][y] = color
        while stack and cluster_size > 1:
            cx, cy = stack.pop()
            random.shuffle(stack)  # Shuffle for randomness
            for nx, ny in get_neighbors(cx, cy):
                if board[nx][ny] == 0 and cluster_size > 1:  # Unassigned cell
                    board[nx][ny] = color
                    stack.append((nx, ny))
                    cluster_size -= 1

    # Fill the board with clusters
    for x in range(size):
        for y in range(size):
            if board[x][y] == 0:  # Empty spot
                color = random.randint(1, colors)
                place_cluster(x, y, color, cluster_size=random.randint(2, 4))  # Ensure groups

    return board

def main():
    board = generate_solvable_board(8)
    for row in board:
        print(row)

    problem = Clickomania(board)

    # Solve using IDA*
    start_time = time.time()
    idastar_solver = IDAStarSolver(problem, verbosity=2)
    idastar_solution = idastar_solver.solve()
    idastar_time = time.time() - start_time

    print("IDA* time:", idastar_time)
    print("IDA* Solution:", idastar_solution)
    print("Nodes expanded:", idastar_solver.nodes_expanded)
    print("Peak memory usage:", idastar_solver.peak_memory_usage)

    # Solve using IDS
    ids_solver = IDSSolver(problem, verbosity=2)
    start_time = time.time()
    ids_solution, nodes_expanded, peak_memory = ids_solver.solve()
    ids_time = time.time() - start_time
    
    print("IDS time:", ids_time)
    print("IDS Solution:", ids_solution)
    print("Nodes expanded:", nodes_expanded)
    print("Peak memory usage:", peak_memory)


if __name__ == "__main__":
    main()
