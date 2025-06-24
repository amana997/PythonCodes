import random

# Function to print the Sudoku board
def print_board(board):
    for i in range(9):
        if i % 3 == 0 and i != 0:
            print("-" * 21)
        for j in range(9):
            if j % 3 == 0 and j != 0:
                print("|", end=" ")
            if board[i][j] == 0:
                print(".", end=" ")
            else:
                print(board[i][j], end=" ")
        print()

# Check if placing a number is valid
def is_valid(board, num, pos):
    row, col = pos
    for i in range(9):
        if board[row][i] == num and i != col:
            return False
        if board[i][col] == num and i != row:
            return False
    start_row, start_col = 3 * (row // 3), 3 * (col // 3)
    for i in range(start_row, start_row + 3):
        for j in range(start_col, start_col + 3):
            if board[i][j] == num and (i, j) != pos:
                return False
    return True

# Solve Sudoku using backtracking
def solve(board):
    for i in range(9):
        for j in range(9):
            if board[i][j] == 0:
                for num in range(1, 10):
                    if is_valid(board, num, (i, j)):
                        board[i][j] = num
                        if solve(board):
                            return True
                        board[i][j] = 0
                return False
    return True

# Generate a full board
def generate_full_board():
    board = [[0] * 9 for _ in range(9)]
    solve(board)  # uses backtracking to fill the board
    return board

# Remove numbers to create a puzzle
def make_puzzle(board, clues=30):
    puzzle = [row[:] for row in board]
    attempts = 81 - clues
    while attempts > 0:
        row = random.randint(0, 8)
        col = random.randint(0, 8)
        if puzzle[row][col] != 0:
            puzzle[row][col] = 0
            attempts -= 1
    return puzzle

# Allow user to play the game
def play_game(puzzle, solution):
    board = [row[:] for row in puzzle]
    while True:
        print_board(board)
        inp = input("Enter move (row col num) or 'q' to quit: ")
        if inp.lower() == 'q':
            print("Exiting game.")
            break
        try:
            row, col, num = map(int, inp.split())
            if puzzle[row][col] != 0:
                print("Cannot change original numbers!")
            elif is_valid(board, num, (row, col)):
                board[row][col] = num
                if board == solution:
                    print_board(board)
                    print("Congratulations! You solved the puzzle.")
                    break
            else:
                print("Invalid move.")
        except:
            print("Invalid input. Format: row col num (0-indexed)")

# Run the game
if __name__ == "__main__":
    full_board = generate_full_board()
    puzzle = make_puzzle(full_board, clues=30)
    play_game(puzzle, full_board)
