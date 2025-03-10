import threading
from clickomania import Clickomania
from solver_idastar import IDAStarSolver
from solver_ids import IDSSolver
import time
import random

TIMEOUT = 60
BOARD_SIZE = 5
TOTAL_TESTS = 5
VERBOSITY = 2

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

def run_with_timeout(func, *args, timeout=TIMEOUT):
    """
    Runs a function with a timeout. If it takes longer than `timeout` seconds,
    it stops execution and returns None.
    """
    result_container = [None]
    exception_container = [None]

    def wrapper():
        try:
            result_container[0] = func(*args)
        except Exception as e:
            exception_container[0] = e

    thread = threading.Thread(target=wrapper)
    thread.start()
    thread.join(timeout)

    if thread.is_alive():
        return None  # Indicate timeout
    
    if exception_container[0] is not None:
        raise exception_container[0]  # Raise exception if function failed

    return result_container[0]

def main():
    total_ids_time = 0
    total_idastar_time = 0
    total_ids_nodes = 0
    total_idastar_nodes = 0
    total_ids_memory = 0
    total_idastar_memory = 0
    total_same_answer = 0

    for i in range(TOTAL_TESTS):
        print(f"\nTest {i + 1}")
        board = generate_solvable_board(BOARD_SIZE)
        for row in board:
            print(row)

        problem = Clickomania(board)

        # Solve using IDA*
        start_time = time.time()
        idastar_solver = IDAStarSolver(problem, verbosity=VERBOSITY)
        idastar_solution = run_with_timeout(idastar_solver.solve)

        if idastar_solution is None:
            print("IDA* solver timed out.")
            continue  # Skip comparison if IDA* timed out
        else:
            print(f"IDA* solution: {idastar_solution}")

        idastar_time = time.time() - start_time
        total_idastar_time += idastar_time
        total_idastar_nodes += idastar_solver.nodes_expanded
        total_idastar_memory += idastar_solver.peak_memory_usage

        # Solve using IDS
        start_time = time.time()
        ids_solver = IDSSolver(problem, verbosity=VERBOSITY)
        ids_solution = run_with_timeout(ids_solver.solve)

        if ids_solution is None:
            print("IDS solver timed out.")
            continue  # Skip comparison if IDS timed out
        else:
            print(f"IDS solution: {ids_solution}")

        ids_time = time.time() - start_time
        total_ids_time += ids_time
        total_ids_nodes += ids_solver.nodes_expanded
        total_ids_memory += ids_solver.peak_memory

        if idastar_solution == ids_solution:
            total_same_answer += 1

    # Final statistics
    print(f"\nAverage IDA* time: {total_idastar_time / TOTAL_TESTS:.2f} seconds")
    print(f"Average IDS time: {total_ids_time / TOTAL_TESTS:.2f} seconds")
    print(f"Average IDA* nodes: {total_idastar_nodes / TOTAL_TESTS}")
    print(f"Average IDS nodes: {total_ids_nodes / TOTAL_TESTS}")
    print(f"Average IDA* memory: {total_idastar_memory / TOTAL_TESTS}")
    print(f"Average IDS memory: {total_ids_memory / TOTAL_TESTS}")
    print(f"Percent same answer: {total_same_answer} / {TOTAL_TESTS}")

if __name__ == "__main__":
    main()
