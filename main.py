from clickomania import Clickomania
from solver_idastar import IDAStarSolver

def main():
    # Define a sample board (5x8 example)
    # Green = 1, Teal = 2, Red = 3, Brown = 4, Orange = 5
    board = [
        [1, 2, 2, 1, 1, 3, 3, 2],
        [1, 1, 2, 3, 1, 3, 3, 2],
        [1, 1, 2, 3, 1, 3, 2, 2],
        [3, 1, 1, 3, 1, 2, 2, 2],
        [3, 3, 1, 1, 3, 2, 2, 1]
    ]

    problem = Clickomania(board)

    # Solve using IDA*
    idastar_solver = IDAStarSolver(problem, verbosity=1)
    idastar_solution = idastar_solver.solve()
    print("IDA* Solution:", idastar_solution)

if __name__ == "__main__":
    main()
