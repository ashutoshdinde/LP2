class NQueens:
    def __init__(self, n):
        self.n = n
        self.board = [-1] * n
        self.solution_count = 0

    def is_safe(self, row, col):
        for prev_row in range(row):
            if (
                self.board[prev_row] == col
                or abs(self.board[prev_row] - col) == abs(prev_row - row)
            ):
                return False
        return True

    def solved_backtracking(self, row):
        if row == self.n:
            self.print_solution()
            self.solution_count += 1
          

        for col in range(self.n):
            if self.is_safe(row, col):
                self.board[row] = col
                if self.solved_backtracking(row + 1):
                    return True
                self.board[row] = -1
        return False

    def solved_branch_and_bound(self, row, queens_left=None):
        if row == self.n:
            self.print_solution()
            self.solution_count += 1
            

        queens_left = queens_left or set(range(self.n))

        for col in queens_left:
            if self.is_safe(row, col):
                self.board[row] = col
                if self.solved_branch_and_bound(row + 1, queens_left - {col}):
                 return True
                self.board[row] = -1

        return False

    def print_solution(self):
        print(f"Solution {self.solution_count}:")
        for row in range(self.n):
            line = ["Q" if col == self.board[row] else "." for col in range(self.n)]
            print("".join(line))
        print()

    def find_solutions_backtracking(self):
        self.solved_backtracking(0)

    def find_solutions_branch_and_bound(self):
        self.solved_branch_and_bound(0)


if __name__ == "__main__":
    n_queen_solver = NQueens(8)  

    print("Solutions using Backtracking:")
    n_queen_solver.find_solutions_backtracking()
    print("Total Solutions:", n_queen_solver.solution_count)

    n_queen_solver.solution_count = 0

    print("\nSolutions using Branch and Bound:")
    n_queen_solver.find_solutions_branch_and_bound()
    print("Total Solutions:", n_queen_solver.solution_count)
