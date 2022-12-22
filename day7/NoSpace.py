import sys
from collections import defaultdict
args = sys.argv

with open(args[1], 'r') as f:
    lines = f.readlines()
directorySize = defaultdict(int)
path = []
size = 0
for line in lines:
    tokens = line.strip().split(' ')

    if tokens[0] == '$' and tokens[1] == "cd":
        if tokens[2] == "..":
            path.pop()
        elif tokens[2] == '/':
            path = ['/']
        else:
            path.append(tokens[2])
    elif tokens[0] == '$' and tokens[1] == "ls":
        pass
    else:
        try:
            size = int(tokens[0])
            for i in range(0, len(path)):
                directorySize['/'.join(path[:i+1])] += size
        except ValueError:
            pass
print(sum(s for s in directorySize.values() if s <= 100000))

#Part2

totalSize = 70000000
neededSpace = 30000000
toFree = neededSpace - (totalSize - directorySize['/'])

print(sorted(s for s in directorySize.values() if s >= toFree)[0])
