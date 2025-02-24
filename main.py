from clickomania import Clickomania
from solver_idastar import IDAStarSolver
from solver_ids import IDSSolver

def main():
    # Define a sample board (5x8 example)
    board = [
        [1, 2, 2, 1, 1, 3, 3, 2],
        [1, 1, 2, 3, 1, 3, 3, 2],
        [1, 1, 2, 3, 1, 3, 2, 2],
        [3, 1, 1, 3, 1, 2, 2, 2],
        [3, 3, 1, 1, 3, 2, 2, 1]
    ]

    problem = Clickomania(board)

    # Solve using IDS
    ids_solver = IDSSolver(problem, verbosity=1)
    ids_solution = ids_solver.solve()
    print("IDS Solution:", ids_solution)

    # Solve using IDA*
    idastar_solver = IDAStarSolver(problem, verbosity=1)
    idastar_solution = idastar_solver.solve()
    print("IDA* Solution:", idastar_solution)

if __name__ == "__main__":
    main()
