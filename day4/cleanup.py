import sys

args = sys.argv
#Part 1
with open(args[1], 'r') as file:
    lines = file.readlines()
    pairsCovered = 0
    pairsOverlap = 0
    for line in lines:
        elf1, elf2 = line.split(',')
        elf1cords = list(map(int, elf1.split('-')))
        elf2cords = list(map(int, elf2.split('-')))
        if ((elf1cords[0] <= elf2cords[0]) and (elf1cords[1] >= elf2cords[1])) or ((elf1cords[0] >= elf2cords[0]) and (elf1cords[1] <= elf2cords[1])):
            pairsCovered += 1
        if ((elf1cords[0] <= elf2cords[0] and elf2cords[0] <= elf1cords[1]) or (elf2cords[0] <= elf1cords[0] and elf1cords[0] <= elf2cords[1])):
            pairsOverlap += 1
    #Fancy Part 1
    pairs = [[list(map(int, elf.split('-'))) for elf in line.split(',')] for line in lines]
    pairsCoveredFancy = len([p for p in pairs if (p[0][0] <= p[1][0] and p[1][1] <= p[0][1]) or (p[1][0] <= p[0][0] and p[0][1] <= p[1][1])])

    #Fancy Part2

    pairsOverlapFancy = len([p for p in pairs if ((p[0][0] <= p[1][0] and p[1][0] <= p[0][1]) or (p[1][0] <= p[0][0] and p[0][0] <= p[1][1]))])
    print(pairsCovered)
    print(pairsCoveredFancy)
    print(pairsOverlap)
    print(pairsOverlapFancy)