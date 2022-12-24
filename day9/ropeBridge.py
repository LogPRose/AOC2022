import sys
import math
args = sys.argv
move = {
    'L': (-1, 0),
    'R': (1, 0),
    'U': (0, -1),
    'D': (0, 1),
}
def moves(lines, num_knots):
    #hx, hy, tx, ty = 0, 0, 0, 0
    knots = [(0,0)] * num_knots
    visited = { (0,0) }
    for line in lines:
        direction, num = line.split(' ')
        m = move[direction]
        for _ in range(int(num)):
            knots[0] = (knots[0][0] + m[0], knots[0][1] + m[1])
            for i in range(1, len(knots)):
                dx = knots[i-1][0] - knots[i][0]
                dy = knots[i-1][1] - knots[i][1]

                if abs(dx) > 1 or abs(dy) > 1:
                    nx, ny = knots[i][0], knots[i][1]
                    if dx:
                        nx = knots[i][0] + math.copysign(1, dx)
                    if dy:
                        ny = knots[i][1] + math.copysign(1, dy)
                    knots[i] = (nx, ny)
            visited.add(knots[-1])
    return len(visited)

#....
#.TH.
#....

#....
#.H..
#..T.
#....

#...
#.H. (H covers T)
#...

with open(args[1], 'r') as f:
    lines = f.readlines()


print(moves(lines, 2))
print(moves(lines, 10))


