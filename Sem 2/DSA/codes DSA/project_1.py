import tkinter as tk
import random
from collections import deque

# Configuration
CELL_SIZE = 25    # pixel size for each cell
MAZE_ROWS = 30
MAZE_COLS = 30
OPEN_PROB = 0.5   # probability to open extra cells beyond the carved path

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
            # Determine possible moves (right and down, and also up/left if needed)
            moves = []
            if r < self.rows - 1:  # move down
                moves.append((r + 1, c))
            if c < self.cols - 1:  # move right
                moves.append((r, c + 1))
            # Optionally allow upward and left moves to add some twist, if not at boundary.
            if r > 0:
                moves.append((r - 1, c))
            if c > 0:
                moves.append((r, c - 1))
            # Choose randomly a move that doesn't immediately backtrack
            # (avoid going to a cell already in the path if possible)
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
        directions = [(0,1), (1,0), (0,-1), (-1,0)]
        for dr, dc in directions:
            nr, nc = r + dr, c + dc
            if 0 <= nr < self.rows and 0 <= nc < self.cols and self.grid[nr][nc] == 1:
                neighbors.append((nr, nc))
        return neighbors

class MazeGUI:
    def __init__(self, master, maze):
        self.master = master
        self.maze = maze
        self.canvas = tk.Canvas(master, width=MAZE_COLS * CELL_SIZE,
                                height=MAZE_ROWS * CELL_SIZE)
        self.canvas.pack()
        
        # Button frame
        frame = tk.Frame(master)
        frame.pack()
        tk.Button(frame, text="Generate Maze", command=self.generate_maze).pack(side=tk.LEFT)
        tk.Button(frame, text="Solve Maze", command=self.solve_maze).pack(side=tk.LEFT)

        # Initially generate and draw a maze.
        self.generate_maze()

    def generate_maze(self):
        self.maze.generate()
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
        # Redraw start and finish on top
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
    root.title("Maze Maker and Solver")
    maze = Maze(MAZE_ROWS, MAZE_COLS)
    gui = MazeGUI(root, maze)
    root.mainloop()

if __name__ == "__main__":
    main()
