presents = []
regions = []
total = 0

with open('input.txt', 'r') as f:
    lines = f.read().split('\n\n')
    for line in lines:
        line = line.split('\n')
        presents.append(line)

regions = presents[-1]
presents = presents[:-1]
presents = [present[1:] for present in presents]
sizes = [0] * len(presents)

for i in range(len(regions)):
    regions[i] = regions[i].split(':')

for i in range(len(presents)):
    for str in presents[i]:
        sizes[i] += str.count('#')
        
for val in regions:
    region, presents = val
    x, y = list(map(int, region.split('x')))
    region_area = x * y
    presents_area = 0
    presents = list(map(int, presents.split()))
    for i in range(len(presents)):
        presents_area += sizes[i] * presents[i]
    if presents_area * 1.3 < region_area:
        total += 1

print(total)