import tkinter as tk
from tkinter import messagebox
import random

def is_valid(board, num, pos):
    row, col = pos
    for i in range(9):
        if board[row][i] == num and i != col:
            return False
        if board[i][col] == num and i != row:
            return False
    box_x = col // 3
    box_y = row // 3
    for i in range(box_y * 3, box_y * 3 + 3):
        for j in range(box_x * 3, box_x * 3 + 3):
            if board[i][j] == num and (i, j) != pos:
                return False
    return True

def solve_board(board):
    for i in range(9):
        for j in range(9):
            if board[i][j] == 0:
                for num in range(1, 10):
                    if is_valid(board, num, (i, j)):
                        board[i][j] = num
                        if solve_board(board):
                            return True
                        board[i][j] = 0
                return False
    return True

def generate_board():
    board = [[0]*9 for _ in range(9)]
    solve_board(board)
    return board

def make_puzzle(board, clues=30):
    puzzle = [row[:] for row in board]
    attempts = 81 - clues
    while attempts > 0:
        i = random.randint(0, 8)
        j = random.randint(0, 8)
        if puzzle[i][j] != 0:
            puzzle[i][j] = 0
            attempts -= 1
    return puzzle

class SudokuGUI:
    def __init__(self, root):
        self.root = root
        self.root.title("Sudoku Game")
        self.entries = [[None for _ in range(9)] for _ in range(9)]
        self.solution = generate_board()
        self.puzzle = make_puzzle(self.solution, clues=30)
        self.create_widgets()

    def create_widgets(self):
        frame = tk.Frame(self.root)
        frame.pack()

        for i in range(9):
            for j in range(9):
                entry = tk.Entry(frame, width=2, font=("Arial", 18), justify="center")
                entry.grid(row=i, column=j, padx=2, pady=2)
                if self.puzzle[i][j] != 0:
                    entry.insert(0, str(self.puzzle[i][j]))
                    entry.config(state="disabled", disabledforeground="black")
                self.entries[i][j] = entry

        button_frame = tk.Frame(self.root)
        button_frame.pack(pady=10)

        check_button = tk.Button(button_frame, text="Check", command=self.check_solution)
        check_button.grid(row=0, column=0, padx=5)

        solve_button = tk.Button(button_frame, text="Solve", command=self.fill_solution)
        solve_button.grid(row=0, column=1, padx=5)

        reset_button = tk.Button(button_frame, text="Reset", command=self.reset_board)
        reset_button.grid(row=0, column=2, padx=5)

    def check_solution(self):
        for i in range(9):
            for j in range(9):
                val = self.entries[i][j].get()
                if val.isdigit():
                    if int(val) != self.solution[i][j]:
                        messagebox.showerror("Incorrect", "Oops! There's a mistake.")
                        return
                else:
                    messagebox.showerror("Empty Cells", "Please fill all cells.")
                    return
        messagebox.showinfo("Success", "Congratulations! Puzzle solved correctly.")

    def fill_solution(self):
        for i in range(9):
            for j in range(9):
                self.entries[i][j].delete(0, tk.END)
                self.entries[i][j].insert(0, str(self.solution[i][j]))
                self.entries[i][j].config(disabledforeground="blue")

    def reset_board(self):
        for i in range(9):
            for j in range(9):
                self.entries[i][j].config(state="normal")
                self.entries[i][j].delete(0, tk.END)
                if self.puzzle[i][j] != 0:
                    self.entries[i][j].insert(0, str(self.puzzle[i][j]))
                    self.entries[i][j].config(state="disabled", disabledforeground="black")

if __name__ == "__main__":
    root = tk.Tk()
    app = SudokuGUI(root)
    root.mainloop()
