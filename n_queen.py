import time

class NQueensBacktracking:
    def __init__(self, n):
        self.n = n
        self.board = [['.'] * n for _ in range(n)]
        self.solutions = []

    def is_safe(self, row, col):
        for i in range(row):
            if self.board[i][col] == 'Q':
                return False
            if col - (row - i) >= 0 and self.board[i][col - (row - i)] == 'Q':
                return False
            if col + (row - i) < self.n and self.board[i][col + (row - i)] == 'Q':
                return False
        return True

    def solve_n_queens_backtracking(self, row):
        if row == self.n:
            self.solutions.append([''.join(row) for row in self.board])
            return

        for col in range(self.n):
            if self.is_safe(row, col):
                self.board[row][col] = 'Q'
                self.solve_n_queens_backtracking(row + 1)
                self.board[row][col] = '.'

    def print_solutions(self):
        for solution in self.solutions:
            print('\n'.join(solution))
            print()

class NQueensBranchAndBound(NQueensBacktracking):
    def __init__(self, n):
        super().__init__(n)
        self.visited = [False] * n
        self.diagonal1 = [False] * (2 * n - 1)  # for diagonal \
        self.diagonal2 = [False] * (2 * n - 1)  # for diagonal /

    def is_safe(self, row, col):
        if self.visited[col] or self.diagonal1[row + col] or self.diagonal2[row - col + self.n - 1]:
            return False
        return True

    def solve_n_queens_branch_and_bound(self, row):
        if row == self.n:
            self.solutions.append([''.join(row) for row in self.board])
            return

        for col in range(self.n):
            if self.is_safe(row, col):
                self.board[row][col] = 'Q'
                self.visited[col] = True
                self.diagonal1[row + col] = True
                self.diagonal2[row - col + self.n - 1] = True
                self.solve_n_queens_branch_and_bound(row + 1)
                self.board[row][col] = '.'
                self.visited[col] = False
                self.diagonal1[row + col] = False
                self.diagonal2[row - col + self.n - 1] = False

# Ask user for input
def choose_solver(method, n):
    if method.upper() == 'B':
        return NQueensBranchAndBound(n)
    elif method.upper() == 'BT':
        return NQueensBacktracking(n)
    else:
        print("Invalid input. Please enter 'B' or 'BT'.")

method = input("Enter 'B' for Branch and Bound or 'BT' for Backtracking: ")
n = int(input("Enter the number of queens: "))

solver = choose_solver(method, n)
if solver:
    print("Selected method:", method.upper())
    start_time = time.time()
    if method.upper() == 'B':
        solver.solve_n_queens_branch_and_bound(0)
    elif method.upper() == 'BT':
        solver.solve_n_queens_backtracking(0)
    end_time = time.time()
    if solver.solutions:
        print("Solutions found:")
        solver.print_solutions()
        print("Time taken:", end_time - start_time, "seconds")
    else:
        print("No solutions found.")
else:
    print("No solver selected.")

