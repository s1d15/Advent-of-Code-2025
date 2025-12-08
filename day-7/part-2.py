from functools import cache

start = -1
grid = []
beam = []
visited = set()
cnt = 0
all_beam = []
with open('input.txt', 'r') as f:
    lines = f.readlines()
    for line in lines:
        grid.append(list(line.strip()))

start = grid[0].index('S')

@cache
def time_line(row, col):
    if row >= len(grid):
        return 1
    if grid[row][col] == '.' or grid[row][col] == 'S':
        return time_line(row + 1, col)
    elif grid[row][col] == '^':
        return time_line(row, col - 1) + time_line(row, col + 1)
    
print(time_line(0, start))