#Part 1

scores = {
    "A X": 4,
    "A Y": 8,
    "A Z": 3,
    "B X": 1,
    "B Y": 5,
    "B Z": 9,
    "C X": 7,
    "C Y": 2,
    "C Z": 6,
}

scoresPart2 = {
    "A X": 3,
    "A Y": 4,
    "A Z": 8,
    "B X": 1,
    "B Y": 5,
    "B Z": 9,
    "C X": 2,
    "C Y": 6,
    "C Z": 7,
}

with open('input.txt', 'r') as file:
    finalScore = 0
    finalScorePart2 = 0
    lines = file.readlines()
    for line in lines:
        finalScore += scores[line.strip()]
        finalScorePart2 += scoresPart2[line.strip()]
print(finalScore)
print(finalScorePart2)

#Part 2


