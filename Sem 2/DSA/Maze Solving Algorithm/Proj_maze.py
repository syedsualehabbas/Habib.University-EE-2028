import random
from collections import deque

######################### Maze Generation Function #################################
"""
    Time Complexity:
    Best Case, Worst Case: O(N^2)
    Reason: Every cell is visited once, and constant time work is done per cell. 
"""

def generate_maze(size):
    if size % 2 == 0:
        size += 1

    # Create an initial grid filled with walls
    maze = [['█' for _ in range(size)] for _ in range(size)]
    
    start_x, start_y = 1, 1
    maze[start_x][start_y] = ' '  
    
    # Define movement directions (up, down, left, right)
    directions = [(-2, 0), (2, 0), (0, -2), (0, 2)]

    # DFS
    stack = [(start_x, start_y)]
    while stack:
        x, y = stack[-1]
        random.shuffle(directions) 
        moved = False
        for dx, dy in directions:
            nx, ny = x + dx, y + dy
            # Check if next cell is inside bounds and still a wall
            if 1 <= nx < size - 1 and 1 <= ny < size - 1 and maze[nx][ny] == '█':
            
                maze[nx][ny] = ' '
                maze[x + dx // 2][y + dy // 2] = ' '
                stack.append((nx, ny))
                moved = True
                break
        if not moved:
            stack.pop()
# Creating extra paths for maze while preserving the main solution path
    extra_paths = size * size // 8
    for _ in range(extra_paths):
        x = random.randrange(1, size - 1, 2)
        y = random.randrange(1, size - 1, 2)
        dx, dy = random.choice(directions)
        nx, ny = x + dx, y + dy
        if 1 <= nx < size - 1 and 1 <= ny < size - 1 and maze[nx][ny] == '█':
            maze[nx][ny] = ' '
            maze[x + dx // 2][y + dy // 2] = ' '

    return maze

############################# Maze Solving Function (BFS) ########################
"""
    Time Complexity: O(N^2)
    Reason: In the worst case, the BFS explores all open cells in the maze. if the start is the goal it will be O(1)
"""

def solve_maze(matrix):
    rows, cols = len(matrix), len(matrix[0])
    start, goal = (1, 1), (rows - 2, cols - 2)
    
    if matrix[start[0]][start[1]] == 0 or matrix[goal[0]][goal[1]] == 0:
        return None

    # Breadth-first search setup
    queue = deque([start])
    came_from = {start: None}
    while queue:
        current = queue.popleft()
        if current == goal:
            break
        for neighbor in get_neighbors(current, matrix):
            if neighbor not in came_from:
                queue.append(neighbor)
                came_from[neighbor] = current
    else:
        return None    # No path found

    path = []
    node = goal
    while node:
        path.append(node)
        node = came_from[node]
    path.reverse()
    return path

# ######################## Neighbor Checking Function ########################
"""
    Time Complexity:
    Best Case, Worst Case O(1)
    Reason: Takes constant time to find all the neigbours of cells
"""
def get_neighbors(cell, matrix):
    r, c = cell
    neighbors = []
    for dr, dc in [(0, 1), (1, 0), (0, -1), (-1, 0)]:
        a, b = r + dr, c + dc
        if 0 <= a < len(matrix) and 0 <= b < len(matrix[0]) and matrix[a][b] == 1:
            neighbors.append((a, b))
    return neighbors

# ######################## Maze Solution Visualization ########################
"""
    Time Complexity:
    Best Case, Worst Case O(N^2)
    Reason: Iterates through every cell in the matrix.
"""

def print_solution(matrix, path):
    # Convert 1/0 matrix back to visual format
    solution_grid = [["█" if cell == 0 else " " for cell in row] for row in matrix]
    for r, c in path:
        solution_grid[r][c] = "*"
    BLUE = '\033[94m'
    RED = '\033[91m'
    RESET = '\033[0m'
    for i, row in enumerate(solution_grid):
        row_str = ""
        for j, cell in enumerate(row):
            if (i, j) == (1, 1):
                row_str += f"{BLUE}S{RESET}" * 2
            elif (i, j) == (len(matrix) - 2, len(matrix[0]) - 2):
                row_str += f"{RED}E{RESET}" * 2
            elif cell == "█":
                row_str += "██"
            elif cell == "*":
                row_str += "**"
            else:
                row_str += "  "
        print(row_str)

# ######################## Helper: Convert Maze to 1/0 Matrix ########################
def convert_maze_to_matrix(maze):
    return [[1 if cell == ' ' else 0 for cell in row] for row in maze]

# ######################## Start Screen ########################
def show_start_screen():
    print("=" * 157)
    print("=" * 157)
    print("\n" * 2)
    print(" " * 57 + "███████╗ ██████╗ ██╗     ██╗   ██╗███████╗")
    print(" " * 57 + "██╔════╝██╔═══██╗██║     ██║   ██║██╔════╝")
    print(" " * 57 + "███████╗██║   ██║██║     ██║   ██║█████╗  ")
    print(" " * 57 + "╚════██║██║   ██║██║     ██║   ██║██╔══╝  ")
    print(" " * 57 + "███████║╚██████╔╝███████╗╚██████╔╝███████╗")
    print(" " * 57 + "╚══════╝ ╚═════╝ ╚══════╝ ╚═════╝ ╚══════╝")
    print(" " * 66 + "████████╗██╗  ██╗███████╗")
    print(" " * 66 + "╚══██╔══╝██║  ██║██╔════╝")
    print(" " * 66 + "   ██║   ███████║█████╗  ")
    print(" " * 66 + "   ██║   ██╔══██║██╔══╝  ")
    print(" " * 66 + "   ██║   ██║  ██║███████╗")
    print(" " * 66 + "   ╚═╝   ╚═╝  ╚═╝╚══════╝")
    print(" " * 61 + "███╗   ███╗ █████╗ ███████╗███████╗")
    print(" " * 61 + "████╗ ████║██╔══██╗╚══███╔╝██╔════╝")
    print(" " * 61 + "██╔████╔██║███████║  ███╔╝ █████╗  ")
    print(" " * 61 + "██║╚██╔╝██║██╔══██║ ███╔╝  ██╔══╝  ")
    print(" " * 61 + "██║ ╚═╝ ██║██║  ██║███████╗███████╗")
    print(" " * 61 + "╚═╝     ╚═╝╚═╝  ╚═╝╚══════╝╚══════╝")
    print("\n" * 1)
    print(" " * 65 + ">>> Press Enter to Play <<<")
    print("=" * 157)
    print("=" * 157)
    input()

# ######################## Difficulty Selection ########################
def show_difficulty_screen():
    print("Select Difficulty Level:")
    print("1) Easy (20 x 20)")
    print("2) Middle (30 x 30)")
    print("3) Hard (40 x 40)")
    print("4) Impossible (50 x 50)")
    
    while True:
        try:
            print("=" * 157)
            print("=" * 157)
            choice = int(input("Enter your choice (1-4): "))
            if choice == 1:
                return 20
            elif choice == 2:
                return 30
            elif choice == 3:
                return 40
            elif choice == 4:
                return 50
            else:
                print("=" * 157)
                print("=" * 157)
                print("Invalid choice! Please enter a number between 1 and 4.")
        except ValueError:
            print("Invalid input! Please enter a valid number between 1 and 4.")

# ######################## Maze Printing ########################
def print_maze(maze):
    for i, row in enumerate(maze):
        row_str = ""
        for j, cell in enumerate(row):
            if (i, j) == (1, 1):
                row_str += "\033[94mS\033[0m" * 2  # Start
            elif (i, j) == (len(maze) - 2, len(row) - 2):
                row_str += "\033[91mE\033[0m" * 2  # End
            elif cell == '█':
                row_str += "██" 
            elif cell == ' ':
                row_str += "  "  
        print(row_str)


# ######################## Main Function ########################
def main():
    show_start_screen()
    size = show_difficulty_screen()  # Ask for difficulty level and get maze size
    maze = generate_maze(size)
    print("=" * 157)
    print("=" * 157)
    print("Unsolved Maze:\n")
    print_maze(maze)  # Display the unsolved maze
    print("=" * 157)
    print("=" * 157)
    
    input("Press Enter to show the solution...")
    
    # Solve the maze and print the solution
    matrix = convert_maze_to_matrix(maze)
    path = solve_maze(matrix)

    if path:
        print("=" * 157)
        print("=" * 157)
        print("Solved Maze:\n")
        print_solution(matrix, path)
        print("=" * 157)
        print("=" * 157)
main()
