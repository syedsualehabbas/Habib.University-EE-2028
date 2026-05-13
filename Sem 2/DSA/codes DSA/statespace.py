import random
from collections import deque

# Configuration
ROWS, COLS = 10, 10  # Maze dimensions
OPEN_PROB = 0.3      # Probability to open extra cells
DIRECTIONS = [(0, 1), (1, 0), (0, -1), (-1, 0)]  # Right, Down, Left, Up

def generate_maze(rows, cols, open_prob=OPEN_PROB):
    """
    Generates a maze using a state-space tree (DFS) to create a guaranteed
    path from (0,0) to (rows-1, cols-1). After the path is carved, extra
    passages are opened randomly.
    """
    maze = [[0 for _ in range(cols)] for _ in range(rows)]  # 0 = wall, 1 = open
    start, goal = (0, 0), (rows - 1, cols - 1)
    stack = [start]
    visited = set([start])
    
    # DFS until the goal is reached
    while stack:
        r, c = stack[-1]
        maze[r][c] = 1  # carve passage
        if (r, c) == goal:
            break
        # Get all unvisited neighbors
        neighbors = []
        random.shuffle(DIRECTIONS)  # randomize order of moves
        for dr, dc in DIRECTIONS:
            nr, nc = r + dr, c + dc
            if 0 <= nr < rows and 0 <= nc < cols and (nr, nc) not in visited:
                neighbors.append((nr, nc))
        if neighbors:
            next_cell = random.choice(neighbors)
            visited.add(next_cell)
            stack.append(next_cell)
        else:
            stack.pop()  # backtrack if no moves available

    # Open extra passages randomly (without altering the guaranteed path)
    for r in range(rows):
        for c in range(cols):
            if maze[r][c] == 0 and random.random() < open_prob:
                maze[r][c] = 1
    return maze

def solve_maze(maze):
    """
    Solves the maze using BFS, treating the maze as a state-space tree.
    Returns the shortest path from the start to the goal.
    """
    rows, cols = len(maze), len(maze[0])
    start, goal = (0, 0), (rows - 1, cols - 1)
    
    if maze[start[0]][start[1]] == 0 or maze[goal[0]][goal[1]] == 0:
        return None  # No solution if start or goal is blocked
    
    queue = deque([start])
    parent = {start: None}
    
    while queue:
        r, c = queue.popleft()
        if (r, c) == goal:
            break
        for dr, dc in DIRECTIONS:
            nr, nc = r + dr, c + dc
            if 0 <= nr < rows and 0 <= nc < cols and maze[nr][nc] == 1 and (nr, nc) not in parent:
                queue.append((nr, nc))
                parent[(nr, nc)] = (r, c)
    else:
        return None  # No solution found
    
    # Reconstruct the path from goal to start
    path = []
    node = goal
    while node:
        path.append(node)
        node = parent[node]
    path.reverse()
    return path

def print_maze(maze, path=None):
    """
    Prints the maze to the console. Start is marked 'S', goal as 'E',
    the solution path with '.', walls with '█', and open cells with a space.
    """
    for r in range(len(maze)):
        for c in range(len(maze[0])):
            if (r, c) == (0, 0):
                print("S", end=" ")
            elif (r, c) == (len(maze) - 1, len(maze[0]) - 1):
                print("E", end=" ")
            elif path and (r, c) in path:
                print(".", end=" ")
            else:
                print("█" if maze[r][c] == 0 else " ", end=" ")
        print()

def main():
    maze = generate_maze(ROWS, COLS)
    print("Generated Maze:")
    print_maze(maze)
    
    solution = solve_maze(maze)
    if solution:
        print("\nSolved Maze:")
        print_maze(maze, solution)
    else:
        print("\nNo solution found!")

if __name__ == "__main__":
    main()
