cords = []

with open('input.txt', 'r') as f:
    lines = f.readlines()
    for line in lines:
        cords.append(tuple(map(int, line.strip().split(','))))

distances = {}

def distance_squared(i, j):
    pair = tuple(zip(cords[i], cords[j]))
    dist = 0
    for x, y in pair:
        dist += (x - y) ** 2
    return dist

for i in range(len(cords)):
    for j in range(i + 1, len(cords)):
        distances[(i, j)] = distance_squared(i, j)

sorted_distances = sorted(distances.items(), key=lambda item: item[1])

parent = {i: i for i in range(len(cords))}
size = {i: 1 for i in range(len(cords))}

def find_parent(node):
    global parent
    if parent[node] == node:
        return node
    return find_parent(parent[node])

MAX = 1000

for pair, dist in sorted_distances[:MAX]:
    i, j = pair
    parent_i, parent_j = find_parent(i), find_parent(j)
    if parent_i == parent_j:
        continue
    parent[parent_j] = parent_i
    size[parent_i] += size[parent_j]

parent_node_sizes = []

for i in range(len(cords)):
    if find_parent(i) == i:
        parent_node_sizes.append((i, size[i]))

parent_node_sizes = sorted(parent_node_sizes, key=lambda x: x[1], reverse=True)

print(parent_node_sizes[0][1] * parent_node_sizes[1][1] * parent_node_sizes[2][1])