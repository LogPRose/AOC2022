import sys

args = sys.argv

with open(args[1], 'r') as f:
    line = f.read().strip()

i = 4
markerPart1 = None
markerPart2 = 0
while i < len(line):
    if not markerPart1 and len(set(line[i - 4:i])) == 4:
        markerPart1 = i
    if len(set(line[i-14:i])) == 14:
        markerPart2 = i
        break
    i += 1
print(markerPart1)
print(markerPart2)