import random
OPEN_PROB=0.3
def generate_maze(rows, cols):
    """Generates a maze using a state-space tree approach."""
    matrix = [[0 for _ in range(cols)] for _ in range(rows)]
    path = create_random_path(rows, cols)
    for r, c in path:
        matrix[r][c] = 1
    for r in range(rows):
        for c in range(cols):
            if matrix[r][c] == 0 and random.random() < OPEN_PROB:
                matrix[r][c] = 1
    return matrix

def create_random_path(rows, cols):
    """Creates a guaranteed random path from (0,0) to (rows-1, cols-1)."""
    r, c = 0, 0
    path = [(r, c)]
    while (r, c) != (rows - 1, cols - 1):
        moves = []
        if r < rows - 1:
            moves.append((r + 1, c))
        if c < cols - 1:
            moves.append((r, c + 1))
        if r > 0:
            moves.append((r - 1, c))
        if c > 0:
            moves.append((r, c - 1))
        valid_moves = [move for move in moves if move not in path]
        move = random.choice(valid_moves) if valid_moves else random.choice(moves)
        path.append(move)
        r, c = move
    return path

def print_maze(matrix):
    """Prints the maze in a readable format."""
    for row in matrix:
        print(" ".join("█" if cell == 0 else " " for cell in row))


print(print_maze(generate_maze(10,10)))