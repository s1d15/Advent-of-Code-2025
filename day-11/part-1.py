from functools import cache

tree = dict()
with open('input.txt', 'r') as f:
    lines = f.readlines()
    for line in lines:
        parent, children = line.strip().split(':')
        tree[parent] = children.split()

@cache
def go(node):
    if tree[node][0] == 'out':
        return 1
    
    total = 0
    for children in tree[node]:
        total += go(children)
    return total

print(go('you'))