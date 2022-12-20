import sys

args = sys.argv
inputFile = args[1]

prio = {
    "a": 1,
    "b": 2,
    "c": 3,
    "d": 4,
    "e": 5,
    "f": 6,
    "g": 7,
    "h": 8,
    "i": 9,
    "j": 10,
    "k": 11,
    "l": 12,
    "m": 13,
    "n": 14,
    "o": 15,
    "p": 16,
    "q": 17,
    "r": 18,
    "s": 19,
    "t": 20,
    "u": 21,
    "v": 22,
    "w": 23,
    "x": 24,
    "y": 25,
    "z": 26,
    "A": 27,
    "B": 28,
    "C": 29,
    "D": 30,
    "E": 31,
    "F": 32,
    "G": 33,
    "H": 34,
    "I": 35,
    "J": 36,
    "K": 37,
    "L": 38,
    "M": 39,
    "N": 40,
    "O": 41,
    "P": 42,
    "Q": 43,
    "R": 44,
    "S": 45,
    "T": 46,
    "U": 47,
    "V": 48,
    "W": 49,
    "X": 50,
    "Y": 51,
    "Z": 52,

}
#Part 1
with open(inputFile, 'r') as file:
    priority = 0
    lines = file.readlines()
    for line in lines:
        firstHalf = line.strip()[0:int((len(line.strip()) / 2))]
        secondHalf = line.strip()[int(len(line.strip()) / 2): int(len(line.strip()))]
        for char in firstHalf:
            if char in secondHalf:
                print(prio[char])
                priority += prio[char]
                break;
print(priority)

#part2
with open(inputFile, 'r') as file:
    badgePrio = 0
    i = 0
    lines = file.readlines()
    while i < len(lines):
        for char in lines[i]:
            if char in lines[i + 1] and char in lines[i + 2] and char != '\n':
                badgePrio += prio[char]
                break;
        i += 3
print(badgePrio)