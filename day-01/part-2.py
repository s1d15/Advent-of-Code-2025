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
    if direction[i] > 0:
        for j in range(direction[i]):
            start += 1
            start = start % 100
            if start == 0:
                res += 1
    else:
        for j in range(abs(direction[i])):
            start -= 1
            start = start % 100
            if start == 0:
                res += 1
        

print(res)