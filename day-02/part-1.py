ids = []
res = 0

with open('input.txt', 'r') as f:
    lines = f.read().split(',')
    for data in lines:
        ids.append(data.strip())

for id in ids:
    first, last = id.split('-')
    for n in range(int(first), int(last) + 1):
        mid = len(str(n)) // 2
        if str(n)[:mid] == str(n)[mid:]:
            res += n
        
print(res)  