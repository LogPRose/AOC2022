import sys
from collections import defaultdict
args = sys.argv
#Part 1

with open(args[1], 'r') as f:
    lines = f.read()

crateInput, instructions = lines.rstrip().split('\n\n')

crates = defaultdict(list)
cratesPart2 = defaultdict(list)
for obj in crateInput.split('\n')[:-1][::-1]:
    print(obj)
    i = 1
    while i < len(obj):
        if obj[i] != ' ':
            crates[(i + 3) / 4].append(obj[i])
            cratesPart2[(i + 3) / 4].append(obj[i])
        i += 4
print(crates)

for instr in instructions.split('\n'):
    _, num, _, start, _, stop = instr.split(' ')
    num, start, stop = int(num), int(start), int(stop)

    for i in range(num):
        crates[stop].append(crates[start].pop())
    cratesPart2[stop].extend(cratesPart2[start][-num:])
    cratesPart2[start] = cratesPart2[start][:-num]
print(''.join(c[-1] for c in crates.values()))
print(''.join(c[-1] for c in cratesPart2.values()))



#Part 2