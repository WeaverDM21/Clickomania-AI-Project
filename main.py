from clickomania import Clickomania
from solver_idastar import IDAStarSolver
from solver_ids import IDSSolver

def main():
    # Define a sample board (5x8 example)
    # Green = 1, Teal = 2, Red = 3, Brown = 4, Orange = 5
    board = [
    [1, 1, 2, 2, 3],
    [1, 1, 2, 3, 3],
    [4, 4, 2, 3, 3],
    [4, 4, 5, 5, 5],
    [6, 6, 5, 5, 5]
    ]


    problem = Clickomania(board)

    # Solve using IDA*
    idastar_solver = IDAStarSolver(problem, verbosity=1)
    idastar_solution = idastar_solver.solve()
    print("IDA* Solution:", idastar_solution)

    # Solve using IDS
    ids_solver = IDSSolver(problem, verbosity=1)
    ids_solution = ids_solver.solve()
    print("IDS Solution:", ids_solution)

if __name__ == "__main__":
    main()
