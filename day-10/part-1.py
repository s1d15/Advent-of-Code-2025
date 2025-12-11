import re
import itertools

total = 0
with open('input.txt', 'r') as f:
    lines = f.readlines()
    for line in lines:
        match = re.match(r"\[([.#]+)\] ([()\d, ]+) \{([\d,])+\}", line.strip())
        target, buttons, joltages = match.groups()
        target = {index for index, light in enumerate(target) if light == '#'}
        buttons = [set(map(int, button[1:-1].split(','))) for button in buttons.split()]
        found = False
        for count in range(1, len(buttons) + 1):
            combination = itertools.combinations(buttons, count)
            for attempt in combination:
                lights = set()
                for button in attempt:
                    lights ^= button
                if lights == target:
                    total += count
                    print(attempt, count)
                    found = True
                    break
            if found:
                break

print(total)