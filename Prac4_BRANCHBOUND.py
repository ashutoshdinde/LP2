from queue import PriorityQueue

class NQueensProblem:
    def __init__(self, n):
        self.n = n
        self.queens = [-1] * n
        self.numSolutions = 0

    def solve(self):
        priority_queue = PriorityQueue()
        priority_queue.put((0, 0, self.queens[:]))  # Initial priority, row, board state
        while not priority_queue.empty():
            priority, row, board = priority_queue.get()
            if row == self.n:
                self.numSolutions += 1
                self.print_solution(board)
            else:
                for col in range(self.n):
                    new_board = board[:]
                    new_board[row] = col
                    if self.is_valid(row, col, new_board):
                        new_priority = self.calculate_priority(row, col, new_board)
                        priority_queue.put((new_priority, row + 1, new_board))

    def is_valid(self, row, col, board):
        for i in range(row):
            if board[i] == col or \
               abs(board[i] - col) == abs(i - row):
                return False
        return True

    def calculate_priority(self, row, col, board):
        # In this case, we can prioritize based on how many conflicts a queen in a row will cause
        conflicts = 0
        for i in range(row + 1, self.n):
            if board[i] == col or \
               abs(board[i] - col) == abs(i - row):
                conflicts += 1
        return conflicts

    def print_solution(self, board):
        if self.numSolutions == 1:
            print("Solution: ", end="")
            for i in range(self.n):
                print(board[i], end=" ")
            print()
            print("The Matrix Representation:")
            arr = [[0] * self.n for _ in range(self.n)]
            for i in range(self.n):
                for j in range(self.n):
                    if j == board[i]:
                        arr[i][j] = 1
            for i in range(self.n):
                for j in range(self.n):
                    print(arr[i][j], end=" ")
                print()

if __name__ == "__main__":
    n = int(input("Enter N Queens Problem: "))
    NQueensProblem = NQueensProblem(n)
    NQueensProblem.solve()
    if NQueensProblem.numSolutions == 0:
        print("Solution does not exist")
