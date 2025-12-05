fresh = []
modified_range = []
res = 0

with open('input.txt', 'r') as f:
    fresh_range, ids = f.read().split('\n\n')
    fresh.append(fresh_range.split('\n'))
    fresh.append(ids.split('\n'))

fresh_range, ids = fresh
ids = list(map(int, ids))
fresh_range = [list(map(int, ranges.split('-'))) for ranges in fresh_range]
fresh_range = sorted(fresh_range, key=lambda x: x[0])

for i in range(len(fresh_range)):
    if not modified_range:
        modified_range.append(fresh_range[i])

    if fresh_range[i][0] > modified_range[-1][1]:
        modified_range.append(fresh_range[i])

    elif fresh_range[i][0] >= modified_range[-1][0] and fresh_range[i][1] >= modified_range[-1][1]:
        modified_range[-1] = ([modified_range[-1][0], fresh_range[i][1]])

    elif fresh_range[i][0] >= modified_range[-1][0] and fresh_range[i][1] <= modified_range[-1][1]:
        continue

for start, end in modified_range:
    res += end - start + 1

print(res)