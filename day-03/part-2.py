banks = []
res = 0

with open('input.txt', 'r') as f:
    lines = f.readlines()
    for line in lines:
        banks.append(line.strip())

for batteries in banks:
    i = 0
    mx_idx = -1
    remaining = 12
    digits = ''
    while remaining > 0:
        end = len(batteries) - remaining
        mx_digits = -1
        for j in range(i, end + 1):
            if int(batteries[j]) > mx_digits:
                mx_digits = int(batteries[j])
                mx_idx = j
        digits += str(mx_digits)
        remaining -= 1
        i = mx_idx + 1
    res += int(digits)

print(res)