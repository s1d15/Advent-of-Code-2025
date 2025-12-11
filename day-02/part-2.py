ids = []
res = 0

with open('input.txt', 'r') as f:
    lines = f.read().split(',')
    for data in lines:
        ids.append(data.strip())

for id in ids:
    first, last = id.split('-')
    for n in range(int(first), int(last) + 1):
        for i in range(1, len(str(n)) // 2 + 1):
            digits = str(n)[:i]
            mul = len(str(n)) // i
            if digits * mul == str(n):
                res += n    
                break    

print(res)  