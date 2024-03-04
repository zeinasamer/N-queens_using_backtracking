import tkinter as tk
from tkinter import messagebox
from tkinter import ttk
from tkinter import PhotoImage  # Import PhotoImage for displaying images


def solve_n_queens_backtracking(n):
    solver = BacktrackingNQueensSolver(n)
    solver.solve()
    
class BacktrackingNQueensSolver:
    def __init__(self, n):
        self.n = n
        self.board = [-1] * n
        self.solutions = []

    def solve(self):
        self._solve_n_queens(0)
        if self.solutions:
            self.display_solution(self.solutions[0])

    def _is_valid(self, row, col):
        for i in range(row):
            if self.board[i] == col or \
               abs(self.board[i] - col) == abs(i - row):
                return False
        return True

    def _solve_n_queens(self, row):
        if row == self.n:
            self.solutions.append(self.board[:])
            return

        for col in range(self.n):
            if self._is_valid(row, col):
                self.board[row] = col
                self._solve_n_queens(row + 1)
                self.board[row] = -1

    def display_solution(self, solution):
        for widget in solution_frame.winfo_children():
            widget.destroy()

        queen_image = PhotoImage(file="queen.png")
        empty_image = PhotoImage(file="tile.png")

        solution_frame.queen_image_ref = queen_image
        solution_frame.empty_image_ref = empty_image

        for row, col in enumerate(solution):
            for i in range(self.n):
                frame = ttk.Frame(solution_frame, width=30, height=30, relief="ridge")
                frame.grid(row=row, column=i, padx=1, pady=1)

                if col == i:
                    label = ttk.Label(frame, image=queen_image)
                else:
                    label = ttk.Label(frame, image=empty_image)

                label.pack(fill="both", expand=True)
 
def print_board(solution, n):
    root = tk.Tk()
    root.title("N-Queens Solution")

    queen_image = PhotoImage(file="queen.png")  # Replace "queen.png" with your queen image file
    empty_image = PhotoImage(file="tile.png")   # Replace "tile.png" with your empty cell image file

    for i, j in enumerate(solution):
        for k in range(n):
            frame = ttk.Frame(root, width=30, height=30, relief="ridge")
            frame.grid(row=i, column=k, padx=1, pady=1)

            # Use an image label for queens and empty cells
            if k == j:
                label = ttk.Label(frame, image=queen_image)
            else:
                label = ttk.Label(frame, image=empty_image)

            label.pack(fill="both", expand=True)

    # Call mainloop once after setting up the entire GUI
    root.mainloop()

def create_gui():
    global size_entry, solution_frame

    root = tk.Tk()
    root.title("N-Queens Problem Solver")

    main_frame = ttk.Frame(root, padding=20)
    main_frame.grid()

    size_label = ttk.Label(main_frame, text="Number of Queens:")
    size_label.grid(row=0, column=0, sticky="W")

    size_entry = ttk.Entry(main_frame, width=10)
    size_entry.grid(row=0, column=1, padx=5, pady=5)

    solve_button = ttk.Button(main_frame, text="Solve", command=lambda: solve_n_queens_problem())
    solve_button.grid(row=0, column=4, padx=5, pady=5)

    clear_button = ttk.Button(main_frame, text="Clear", command=clear_solution)
    clear_button.grid(row=0, column=5, padx=5, pady=5)

    solution_frame = ttk.Frame(main_frame, padding=10)
    solution_frame.grid(row=1, column=0, columnspan=6)

    root.mainloop()

def clear_solution():
    for widget in solution_frame.winfo_children():
        widget.destroy()

def solve_n_queens_problem():
    size_str = size_entry.get()

    if not size_str:
        messagebox.showerror("Error", "Please enter a positive integer for the board size.")
        return

    try:
        size = int(size_str)
        if size <= 3:
            raise ValueError("Number of queens must be more than 3 .")
    except ValueError as e:
        messagebox.showerror("Error", str(e))
        return

    solve_n_queens_backtracking(size)

def display_solution(solution, size):
    for widget in solution_frame.winfo_children():
        widget.destroy()

    # Load the queen image
    queen_image = PhotoImage(file="queen.png")  # Replace "queen.png" with your image file
    empty_image = PhotoImage(file="tile.png")  # Replace "tile.png" with your image file for empty cells

    # Retain the reference to the images to prevent garbage collection
    solution_frame.queen_image_ref = queen_image
    solution_frame.empty_image_ref = empty_image

    for row, col in enumerate(solution):
        for i in range(size):
            frame = ttk.Frame(solution_frame, width=30, height=30, relief="ridge")
            frame.grid(row=row, column=i, padx=1, pady=1)

            # Use an image label for queens and empty cells
            if col == i:
                label = ttk.Label(frame, image=queen_image)
            else:
                label = ttk.Label(frame, image=empty_image)

            label.pack(fill="both", expand=True)

# Run the GUI
create_gui()


