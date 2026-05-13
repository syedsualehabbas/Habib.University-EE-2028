import random
from collections import deque

# Configuration
MAZE_ROWS = 50
MAZE_COLS = 50


def generate_maze(rows, cols):
    """Generates a maze using a state-space tree approach."""
    matrix = [[0 for _ in range(cols)] for _ in range(rows)]
    path = create_random_path(rows, cols)
    wrong=create_wrong_paths(rows, cols)
    for i in path:
        r, c=i
        matrix[r][c] = 1
    for r in range(rows-1):
        for c in range(cols-1):
            if matrix[r][c] !=1:
                matrix[r][c] = 0
    for i in wrong:
        r, c=i
        matrix[r][c] = 1
    for r in range(rows-1):
        for c in range(cols-1):
            if matrix[r][c] !=1:
                matrix[r][c] = 0
    return matrix



def create_random_path(rows, cols):
    """Creates a guaranteed random path from (0,0) to (rows-1, cols-1)."""
    r, c = 0, 0
    flag=True
    path = [(r, c)]
    while (r, c) != (rows - 1, cols - 1):
        moves = []
        if flag==True:
            if r < rows - 1:
                moves.append((r + 1, c))
            if c < cols - 1:
                moves.append((r, c + 1))
            # if r > 0:
            #     moves.append((r - 1, c))
            if c > 0:
                moves.append((r, c - 1))
            flag=False
        if flag==False:
            if r < rows - 1:
                moves.append((r + 1, c))
            if c < cols - 1:
                moves.append((r, c + 1))
            if r > 0:
                moves.append((r - 1, c))
                # if c > 0:
                #     moves.append((r, c - 1))
            flag=True

        valid_moves = [move for move in moves if move not in path]
        move = random.choice(valid_moves) if valid_moves else random.choice(moves)
        path.append(move)
        r, c = move
    return path

def create_wrong_paths(rows,cols):
    r,c=0,0
    wrong_path=[(r, c)]
    flag=True
    mylist=[1,2,3,4,5,6,7,8,9]
    num=random.choice(mylist)
    while (r, c) != (rows-1, cols//num):
        moves = []
        if flag==True:
            if r < rows-1:
                moves.append((r + 1, c))
            if c < cols//num:
                moves.append((r, c + 1))
            # if r > 0:
            #     moves.append((r - 1, c))
            if c > 0:
                moves.append((r, c - 1))
            flag=False
        if flag==False:
            if r < rows-1:
                moves.append((r + 1, c))
            if c < cols//num:
                moves.append((r, c + 1))
            if r > 0:
                moves.append((r - 1, c))
                # if c > 0:
                #     moves.append((r, c - 1))
            flag=True


        valid_moves = [move for move in moves if move not in wrong_path]
        move = random.choice(valid_moves) if valid_moves else random.choice(moves)
        wrong_path.append(move)
        r, c = move
    return wrong_path

def print_solution(matrix, path):
    """Prints the maze with the solution path."""
    solution_grid = [["█" if cell == 0 else " " for cell in row] for row in matrix]
    for r, c in path:
        solution_grid[r][c] = "*"
    for row in solution_grid:
        print(" ".join(row))

def print_maze(matrix):
    """Prints the maze in a readable format."""
    for row in matrix:
        print(" ".join("█" if cell == 0 else " " for cell in row))

def main():
    matrix = generate_maze(MAZE_ROWS, MAZE_COLS)
    print("Generated Maze:")
    print_maze(matrix)
    solution = solve_maze(matrix)
    if solution:
        print("\nSolved Maze:")
        print_solution(matrix, solution)
    else:
        print("\nNo solution found!")

if __name__ == "__main__":
    main()
