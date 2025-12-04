grid = []
dir = (-1, -1), (-1, 0), (-1, 1), (0, 1), (1, 1), (1, 0), (1, -1), (0, -1)
res = 0

with open('input.txt', 'r') as f:
    lines = f.readlines()
    for line in lines:
        grid.append(list(line.strip()))

while True:
    cond = False
    for i in range(len(grid)):
        for j in range(len(grid[i])):
            cnt = 0 
            if grid[i][j] == '.':
                continue
            for x, y in dir:
                curr_x = i + x
                curr_y = j + y
                if curr_x >= 0 and curr_x < len(grid) and curr_y >= 0 and curr_y < len(grid[i]):
                    if grid[curr_x][curr_y] == '@':
                        cnt += 1
            if cnt < 4:
                grid[i][j] = '.'
                cond = True
                res += 1
    if not cond:
        break

print(res)