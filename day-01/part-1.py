direction = []
start = 50
res = 0

with open('input.txt', 'r') as f:
    lines = f.readlines()
    for data in lines:
        if data[0] == 'R':
            data = data[1:]
        else:
            data = '-' + data[1:]
        direction.append(int(data.strip()))
    
for i in range(len(direction)):
    start += direction[i]
    start = start % 100
    if start == 0:
        res += 1

print(res)