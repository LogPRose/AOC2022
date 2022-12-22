import sys

args = sys.argv
def score(grid, r, c):
    if c == 0 or c == C - 1 or r == 0 or r == R - 1:
        return 0
    
    right = 0
    left = 0
    up = 0
    down = 0
    for dc in range(1, c+1):
        if grid[r][c - dc] >= grid[r][c]:
            break
    left = dc
    for dc in range(1, C - c):
        if grid[r][c + dc] >= grid[r][c]:
            break
    right = dc
    for dr in range(1, r+1):
        if grid[r - dr][c] >= grid[r][c]:
            break
    top = dr
    for dr in range(1, R - r):
        if grid[r + dr][c] >= grid[r][c]:
            break
    bottom = dr
    return left * right * top * bottom







def visible(grid, r, c):
    if c == 0 or c == C-1 or r == 0 or r == R - 1:
        return 1
    #up
    if all(grid[row][c] < grid[r][c] for row in range(r)):
        return 1
    #down
    if all(grid[row][c] < grid[r][c] for row in range(r + 1, R)):
        return 1
    #right
    if all(grid[r][col] < grid[r][c] for col in range(c+1, C)):
        return 1
    #left
    if all(grid[r][col] < grid[r][c] for col in range(c)):
        return 1
    return 0




with open(args[1], 'r') as f:
    treeGrid = [list(map(int, line.strip())) for line in f.readlines()]

tooShort = 0
scenicScore = 0
R = len(treeGrid)
C = len(treeGrid[0])
for rows in range(R):
    for cols in range(C):
        tooShort += visible(treeGrid, rows, cols)
        scenicScore = max(scenicScore, score(treeGrid, rows, cols))

print(tooShort)
print(scenicScore)
#Part 2