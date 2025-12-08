start = -1
grid = []
beam = []
visited = set()
cnt = 0

with open('input.txt', 'r') as f:
    lines = f.readlines()
    for line in lines:
        grid.append(list(line.strip()))

start = grid[0].index('S')
beam.append((0, start))

def add_beam(row, col):
    if (row, col) in visited:
        return
    visited.add((row, col))
    beam.append((row, col))

while beam:
    row, col = beam.pop(0)
    if grid[row][col] == '.' or grid[row][col] == 'S':
        if row == len(grid) - 1:
            continue
        add_beam(row + 1, col)
    elif grid[row][col] == '^':
        cnt += 1
        add_beam(row, col - 1)
        add_beam(row, col + 1)        
    
print(cnt)