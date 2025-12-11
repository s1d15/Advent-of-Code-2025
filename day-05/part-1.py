fresh = []
res = 0

with open('input.txt', 'r') as f:
    fresh_range, ids = f.read().split('\n\n')
    fresh.append(fresh_range.split('\n'))
    fresh.append(ids.split('\n'))

fresh_range, ids = fresh
ids = list(map(int, ids))
fresh_range = [list(map(int, ranges.split('-'))) for ranges in fresh_range]
fresh_range = [range(start, end + 1) for start, end in fresh_range]

for id in ids:
    for ranges in fresh_range:
        if id in ranges:
            res += 1
            break

print(res)