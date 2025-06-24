import tkinter as tk
from tkinter import messagebox, ttk
import random
import time
import threading

# Sudoku logic
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

def make_puzzle(board, clues):
    puzzle = [row[:] for row in board]
    attempts = 81 - clues
    while attempts > 0:
        i = random.randint(0, 8)
        j = random.randint(0, 8)
        if puzzle[i][j] != 0:
            puzzle[i][j] = 0
            attempts -= 1
    return puzzle

# GUI Class
class SudokuGUI:
    def __init__(self, root):
        self.root = root
        self.root.title("Sudoku Game")

        self.entries = [[None for _ in range(9)] for _ in range(9)]
        self.solution = None
        self.puzzle = None
        self.start_time = None
        self.timer_running = False

        self.create_menu()
        self.create_widgets()
        self.choose_difficulty("Easy")

    def create_menu(self):
        difficulty_frame = tk.Frame(self.root)
        difficulty_frame.pack(pady=5)

        tk.Label(difficulty_frame, text="Difficulty:").pack(side=tk.LEFT)
        self.difficulty_var = tk.StringVar(value="Easy")
        difficulty_menu = ttk.Combobox(difficulty_frame, textvariable=self.difficulty_var, values=["Easy", "Medium", "Hard"], state="readonly")
        difficulty_menu.pack(side=tk.LEFT, padx=5)
        difficulty_menu.bind("<<ComboboxSelected>>", lambda e: self.choose_difficulty(self.difficulty_var.get()))

        self.timer_label = tk.Label(difficulty_frame, text="Time: 00:00")
        self.timer_label.pack(side=tk.RIGHT, padx=20)

    def create_widgets(self):
        self.board_frame = tk.Frame(self.root)
        self.board_frame.pack()

        for i in range(9):
            for j in range(9):
                entry = tk.Entry(self.board_frame, width=2, font=("Arial", 18), justify="center")
                entry.grid(row=i, column=j, padx=2, pady=2)
                self.entries[i][j] = entry

        button_frame = tk.Frame(self.root)
        button_frame.pack(pady=10)

        tk.Button(button_frame, text="Check", command=self.check_solution).grid(row=0, column=0, padx=5)
        tk.Button(button_frame, text="Hint", command=self.give_hint).grid(row=0, column=1, padx=5)
        tk.Button(button_frame, text="Solve", command=self.fill_solution).grid(row=0, column=2, padx=5)
        tk.Button(button_frame, text="Reset", command=self.reset_board).grid(row=0, column=3, padx=5)

    def choose_difficulty(self, level):
        clues = {"Easy": 40, "Medium": 32, "Hard": 25}.get(level, 40)
        self.solution = generate_board()
        self.puzzle = make_puzzle(self.solution, clues)
        self.reset_board()
        self.start_timer()

    def reset_board(self):
        for i in range(9):
            for j in range(9):
                entry = self.entries[i][j]
                entry.config(state="normal")
                entry.delete(0, tk.END)
                if self.puzzle[i][j] != 0:
                    entry.insert(0, str(self.puzzle[i][j]))
                    entry.config(state="disabled", disabledforeground="black")
        self.start_timer()

    def check_solution(self):
        for i in range(9):
            for j in range(9):
                val = self.entries[i][j].get()
                if val.isdigit():
                    if int(val) != self.solution[i][j]:
                        messagebox.showerror("Incorrect", f"Incorrect entry at row {i+1}, col {j+1}")
                        return
                else:
                    messagebox.showwarning("Incomplete", "Please fill all cells.")
                    return
        self.timer_running = False
        messagebox.showinfo("Solved", f"Congratulations! You solved the puzzle in {self.timer_label.cget('text')}.")

    def fill_solution(self):
        for i in range(9):
            for j in range(9):
                self.entries[i][j].config(state="normal")
                self.entries[i][j].delete(0, tk.END)
                self.entries[i][j].insert(0, str(self.solution[i][j]))
                self.entries[i][j].config(disabledforeground="blue")
        self.timer_running = False

    def give_hint(self):
        for i in range(9):
            for j in range(9):
                entry = self.entries[i][j]
                if entry.get() == "":
                    entry.insert(0, str(self.solution[i][j]))
                    entry.config(fg="blue")
                    return
        messagebox.showinfo("Hints", "All cells are filled!")

    def start_timer(self):
        self.start_time = time.time()
        self.timer_running = True
        self.update_timer()

    def update_timer(self):
        if not self.timer_running:
            return
        elapsed = int(time.time() - self.start_time)
        minutes, seconds = divmod(elapsed, 60)
        self.timer_label.config(text=f"Time: {minutes:02}:{seconds:02}")
        self.root.after(1000, self.update_timer)

# Run the game
if __name__ == "__main__":
    root = tk.Tk()
    app = SudokuGUI(root)
    root.mainloop()
