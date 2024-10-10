#!/usr/bin/python3
import sys

def print_usage_and_exit(message, exit_code):
    print(message)
    sys.exit(exit_code)

def is_valid(board, row, col):
    # Check for the same column and the two diagonals
    for i in range(row):
        if board[i] == col or \
           board[i] - i == col - row or \
           board[i] + i == col + row:
            return False
    return True

def solve_nqueens(N):
    def backtrack(row, board):
        if row == N:
            # Convert board representation to the format required
            solution = [[i, board[i]] for i in range(N)]
            solutions.append(solution)
            return
        
        for col in range(N):
            if is_valid(board, row, col):
                board[row] = col
                backtrack(row + 1, board)
                # No need to explicitly reset the board[row] because it will be overwritten in the next iteration

    solutions = []
    board = [-1] * N  # Board is represented as a list where index is the row and value is the column
    backtrack(0, board)
    return solutions

def main():
    # Check the number of arguments
    if len(sys.argv) != 2:
        print_usage_and_exit("Usage: nqueens N", 1)
    
    try:
        N = int(sys.argv[1])
    except ValueError:
        print_usage_and_exit("N must be a number", 1)
    
    # Validate N
    if N < 4:
        print_usage_and_exit("N must be at least 4", 1)
    
    # Solve the N-Queens problem and print the solutions
    solutions = solve_nqueens(N)
    for solution in solutions:
        print(solution)

if __name__ == "__main__":
    main()
