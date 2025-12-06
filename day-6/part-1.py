equations = []
res = 0
with open('input.txt', 'r') as f:
    lines = f.readlines()
    for line in lines:
        equations.append(line.strip().split())

equations = list(zip(*equations))

for equation in equations:
    res += eval(equation[-1].join(equation[:-1]))

print(res)