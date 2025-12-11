equations = []
res = 0
with open('input.txt', 'r') as f:
    lines = f.readlines()
    for line in lines:
        equations.append(list(line.strip('\n')))

equations = list(zip(*equations))

for i in range(len(equations)):
    equations[i] = ''.join(equations[i])

sign = ''
evaluate = []
for equation in equations:
    if equation[-1] in ('*', '+'):
        sign = equation[-1]
    
    if equation.strip() == '':
        res += eval(sign.join(evaluate))
        sign = ''
        evaluate = []
        continue

    evaluate.append(equation[:-1])
    if equation == equations[-1]:
        res += eval(sign.join(evaluate))

print(res)