banks = []
res = 0

with open('input.txt', 'r') as f:
    lines = f.readlines()
    for line in lines:
        banks.append(line.strip())

for batteries in banks:
    mx = 0
    for i in range(len(batteries)):
        for j in range(i + 1, len(batteries)):
            battery = batteries[i] + batteries[j]
            if int(battery) > mx:
                mx = int(battery)
    res += mx

print(res)