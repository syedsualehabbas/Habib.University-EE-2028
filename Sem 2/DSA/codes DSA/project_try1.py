import random
def create_randompath(rows, cols):
    r, c=0, 0  #initializing starting position
    path=[(r,c)]  
    while (r, c)!=(rows-1,cols-1):  #will move till the end position
        moves=[]
        if r<rows-1: #move down
            moves.append((r+1,c))
        if c<cols-1:  #move right
            moves.append((r,c+1))
        if r>0:    #move up
            moves.append((r-1, c))
        if c>0:    #move left
            moves.append((r,c-1))
        valid_moves= [move for move in moves if move not in path]   #avoid unnecessary loops filters out moves
        move =random.choice(valid_moves) if valid_moves else random.choice(moves)
        path.append(move)  #selected move added to the path
        r,c =move #current position is updated
    return path
print(create_randompath(2,2))