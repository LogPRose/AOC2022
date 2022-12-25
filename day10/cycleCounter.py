import sys

args = sys.argv



class Computer:

    def __init__(self, lines):
        self.program = lines
        self.clock = 0
        self.regX = 1
        self.total = 0
        self.pixels = {}

    def step(self):
        row = self.clock // 40
        col = self.clock % 40
        self.clock += 1
        if self.regX - 1 <= col <= self.regX + 1:
            pix = '#'
        else:
            pix = ' '
        self.pixels[(row, col)] = pix
        if (self.clock - 20) % 40 == 0:
            self.total += self.clock * self.regX

    def add(self, v):
        self.step()
        self.step()
        self.regX += v

    def noop(self):
        self.step()

    def run(self):
        for line in self.program:
            if line.startswith('noop'):
                self.noop()
            elif line.startswith('addx'):
                v = int(line.split(' ')[1])
                self.add(v)
    
    def print(self):
        for r in range(6):
            for c in range(40):
                print(self.pixels[(r,c)], end=' ')
            print()


with open(args[1], 'r') as f:
    lines = f.readlines()

comp = Computer(lines)
comp.run()

print(comp.total)
comp.print()

