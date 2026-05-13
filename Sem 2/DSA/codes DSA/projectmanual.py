import tkinter as tk
import random
from collections import deque

# Configuration
CELL_SIZE = 25    # pixel size for each cell
MAZE_ROWS = 20
MAZE_COLS = 20
OPEN_PROB = 0.3   # probability to open extra cells beyond the carved path

class Maze:
    def __init__(self, rows, cols):
        self.rows = rows
        self.cols = cols
        self.grid = [[0 for _ in range(cols)] for _ in range(rows)]

    def generate(self):
        # Reset grid
        self.grid = [[0 for _ in range(self.cols)] for _ in range(self.rows)]
        # Carve a guaranteed path from (0,0) to (rows-1, cols-1)
        path = self._create_random_path()
        for r, c in path:
            self.grid[r][c] = 1

        # Open additional cells randomly, keeping the main path intact.
        for r in range(self.rows):
            for c in range(self.cols):
                if self.grid[r][c] == 0 and random.random() < OPEN_PROB:
                    self.grid[r][c] = 1

    def _create_random_path(self):
        # Start at the top left
        r, c = 0, 0
        path = [(r, c)]
        while (r, c) != (self.rows - 1, self.cols - 1):
            moves = []
            if r < self.rows - 1:  # move down
                moves.append((r + 1, c))
            if c < self.cols - 1:  # move right
                moves.append((r, c + 1))
            # Optionally allow upward and left moves for more variety
            if r > 0:
                moves.append((r - 1, c))
            if c > 0:
                moves.append((r, c - 1))
            valid_moves = [move for move in moves if move not in path]
            if valid_moves:
                move = random.choice(valid_moves)
            else:
                move = random.choice(moves)
            path.append(move)
            r, c = move
        return path

    def solve(self):
        # Use BFS to find the shortest path from (0,0) to (rows-1, cols-1)
        start = (0, 0)
        goal = (self.rows - 1, self.cols - 1)
        if self.grid[start[0]][start[1]] == 0 or self.grid[goal[0]][goal[1]] == 0:
            return None  # no solution if start or end is blocked

        queue = deque([start])
        came_from = {start: None}
        while queue:
            current = queue.popleft()
            if current == goal:
                break
            for neighbor in self._neighbors(current):
                if neighbor not in came_from:
                    queue.append(neighbor)
                    came_from[neighbor] = current
        else:
            return None  # no solution found

        # Reconstruct path from goal to start
        path = []
        node = goal
        while node:
            path.append(node)
            node = came_from[node]
        path.reverse()
        return path

    def _neighbors(self, cell):
        r, c = cell
        neighbors = []
        directions = [(0, 1), (1, 0), (0, -1), (-1, 0)]
        for dr, dc in directions:
            nr, nc = r + dr, c + dc
            if 0 <= nr < self.rows and 0 <= nc < self.cols and self.grid[nr][nc] == 1:
                neighbors.append((nr, nc))
        return neighbors

class MazeGUI:
    def __init__(self, master, maze):
        self.master = master
        self.maze = maze
        self.edit_mode = False           # for editing the maze grid
        self.user_solve_mode = False     # for manual maze solving by the user
        self.user_path = []              # stores the user's manual path

        # Set up canvas and bind click events
        self.canvas = tk.Canvas(master, width=MAZE_COLS * CELL_SIZE,
                                height=MAZE_ROWS * CELL_SIZE)
        self.canvas.pack()
        self.canvas.bind("<Button-1>", self.canvas_click)

        # Button frame
        frame = tk.Frame(master)
        frame.pack(pady=5)
        tk.Button(frame, text="Generate Maze", command=self.generate_maze).pack(side=tk.LEFT, padx=5)
        tk.Button(frame, text="Solve Maze (Auto)", command=self.solve_maze).pack(side=tk.LEFT, padx=5)
        self.edit_button = tk.Button(frame, text="Toggle Edit Mode: OFF", command=self.toggle_edit_mode)
        self.edit_button.pack(side=tk.LEFT, padx=5)
        self.user_solve_button = tk.Button(frame, text="Toggle User Solve Mode: OFF", command=self.toggle_user_solve_mode)
        self.user_solve_button.pack(side=tk.LEFT, padx=5)
        self.reset_user_solve_button = tk.Button(frame, text="Reset Manual Solve", command=self.reset_user_solve)
        self.reset_user_solve_button.pack(side=tk.LEFT, padx=5)

        # Initially generate and draw a maze.
        self.generate_maze()

    def toggle_edit_mode(self):
        # Ensure only one mode is active at a time.
        if self.user_solve_mode:
            self.toggle_user_solve_mode(disable=True)
        self.edit_mode = not self.edit_mode
        self.edit_button.config(text=f"Toggle Edit Mode: {'ON' if self.edit_mode else 'OFF'}")

    def toggle_user_solve_mode(self, disable=False):
        # Ensure only one mode is active at a time.
        if disable:
            self.user_solve_mode = False
            self.user_solve_button.config(text="Toggle User Solve Mode: OFF")
            self.user_path = []
            self.draw_maze()
            return
        if self.edit_mode:
            self.toggle_edit_mode()  # disable edit mode if active

        self.user_solve_mode = not self.user_solve_mode
        if self.user_solve_mode:
            # Start manual solve at the start cell.
            self.user_path = [(0, 0)]
            self.user_solve_button.config(text="Toggle User Solve Mode: ON")
            self.draw_maze()
            self.draw_user_path()
        else:
            self.user_path = []
            self.user_solve_button.config(text="Toggle User Solve Mode: OFF")
            self.draw_maze()

    def reset_user_solve(self):
        if self.user_solve_mode:
            self.user_path = [(0, 0)]
            self.draw_maze()
            self.draw_user_path()

    def canvas_click(self, event):
        col = event.x // CELL_SIZE
        row = event.y // CELL_SIZE
        if self.edit_mode:
            # In edit mode, toggle the cell state (except start/finish).
            if (row, col) in [(0, 0), (self.maze.rows - 1, self.maze.cols - 1)]:
                return
            self.maze.grid[row][col] = 0 if self.maze.grid[row][col] == 1 else 1
            self.draw_cell(row, col, "white" if self.maze.grid[row][col] == 1 else "black")
        elif self.user_solve_mode:
            # In manual solve mode, try to add the clicked cell to the user's path.
            if not (0 <= row < self.maze.rows and 0 <= col < self.maze.cols):
                return
            if self.maze.grid[row][col] == 0:
                return  # cannot move onto an obstacle
            # Validate that the clicked cell is adjacent to the last cell in the user path.
            last_r, last_c = self.user_path[-1]
            if abs(last_r - row) + abs(last_c - col) != 1:
                return
            # Allow backtracking if the user clicks the previous cell.
            if (row, col) in self.user_path and len(self.user_path) > 1:
                if (row, col) != self.user_path[-2]:
                    return
                else:
                    self.user_path.pop()
                    self.draw_user_path()
                    return
            # Append the valid move.
            self.user_path.append((row, col))
            self.draw_user_path()
            # Check if reached finish cell.
            if (row, col) == (self.maze.rows - 1, self.maze.cols - 1):
                print("Congratulations! You solved the maze!")

    def generate_maze(self):
        self.maze.generate()
        self.user_path = []
        self.draw_maze()

    def solve_maze(self):
        solution = self.maze.solve()
        if solution is None:
            print("No solution found!")
        else:
            self.draw_solution(solution)

    def draw_maze(self):
        self.canvas.delete("all")
        for r in range(self.maze.rows):
            for c in range(self.maze.cols):
                color = "white" if self.maze.grid[r][c] == 1 else "black"
                self.draw_cell(r, c, color)
        # Mark start and finish cells
        self.draw_cell(0, 0, "green")
        self.draw_cell(self.maze.rows - 1, self.maze.cols - 1, "red")

    def draw_solution(self, path):
        # Redraw maze first
        self.draw_maze()
        # Overlay the solution path in blue.
        for r, c in path:
            self.draw_cell(r, c, "blue")
        # Redraw start and finish on top.
        self.draw_cell(0, 0, "green")
        self.draw_cell(self.maze.rows - 1, self.maze.cols - 1, "red")

    def draw_user_path(self):
        # Redraw maze first.
        self.draw_maze()
        # Overlay the user's manual path in orange.
        for r, c in self.user_path:
            self.draw_cell(r, c, "orange")
        # Ensure start and finish remain marked.
        self.draw_cell(0, 0, "green")
        self.draw_cell(self.maze.rows - 1, self.maze.cols - 1, "red")

    def draw_cell(self, r, c, color):
        x1 = c * CELL_SIZE
        y1 = r * CELL_SIZE
        x2 = x1 + CELL_SIZE
        y2 = y1 + CELL_SIZE
        self.canvas.create_rectangle(x1, y1, x2, y2, fill=color, outline="gray")

def main():
    root = tk.Tk()
    root.title("Maze Maker, Solver, and Manual Solve")
    maze = Maze(MAZE_ROWS, MAZE_COLS)
    MazeGUI(root, maze)
    root.mainloop()

if __name__ == "__main__":
    main()
