grid = []
area = []

with open('input.txt', 'r') as f:
    lines = f.readlines()
    for line in lines:
        grid.append(list(map(int, line.strip().split(','))))

for i in range(len(grid)):
    for j in range(i + 1, len(grid)):
        area.append([(i, j), (abs(grid[i][0] - grid[j][0]) + 1) * (1 + abs(grid[i][1] - grid[j][1]))])    

area = sorted(area, key=lambda x: x[1], reverse=True)

print(area[0][1])