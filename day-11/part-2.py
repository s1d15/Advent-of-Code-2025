from functools import cache

tree = dict()
with open('input.txt', 'r') as f:
    lines = f.readlines()
    for line in lines:
        parent, children = line.strip().split(':')
        tree[parent] = children.split()

@cache
def go(node, include_dac, include_fft):
    if tree[node][0] == 'out':
        if include_dac and include_fft:
            return 1
        return 0
    
    total = 0
    for children in tree[node]:
        total += go(children, include_dac or children == 'dac', include_fft or children == 'fft')
    return total

print(go('svr', False, False))