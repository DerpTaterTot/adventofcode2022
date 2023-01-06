filein = open("day09/input.txt", "r")

lines = filein.readlines()

class Rope:
    def __init__(self, length):
        self.rope = [(0, 0)] * length
        self.previous_distances = []
    
    def moveHead(self, move):
        if move == "U":
            self.rope[0] = (self.rope[0][0], self.rope[0][1] + 1)
        elif move == "D":
            self.rope[0] = (self.rope[0][0], self.rope[0][1] - 1)
        elif move == "L":
            self.rope[0] = (self.rope[0][0] - 1, self.rope[0][1])
        elif move == "R":
            self.rope[0] = (self.rope[0][0] + 1, self.rope[0][1])
    
    def moveNonHead(self, i):        
        if self.rope[i + 1][0] == self.rope[i][0] and abs(self.rope[i + 1][1] - self.rope[i][1]) > 1:
            if self.rope[i + 1][1] < self.rope[i][1]:
                self.rope[i + 1] = (self.rope[i + 1][0], self.rope[i + 1][1] + 1)
            else:
                self.rope[i + 1] = (self.rope[i + 1][0], self.rope[i + 1][1] - 1)
                
        elif self.rope[i + 1][1] == self.rope[i][1] and abs(self.rope[i + 1][0] - self.rope[i][0]) > 1:
            if self.rope[i + 1][0] < self.rope[i][0]:
                self.rope[i + 1] = (self.rope[i + 1][0] + 1, self.rope[i + 1][1])
            else:
                self.rope[i + 1] = (self.rope[i + 1][0] - 1, self.rope[i + 1][1])
                
        else:
            if abs(self.rope[i + 1][0] - self.rope[i][0]) > 1 or abs(self.rope[i + 1][1] - self.rope[i][1]) > 1:
                if self.rope[i + 1][0] < self.rope[i][0]:
                    if self.rope[i + 1][1] < self.rope[i][1]:
                        self.rope[i + 1] = (self.rope[i + 1][0] + 1, self.rope[i + 1][1] + 1)
                    else:
                        self.rope[i + 1] = (self.rope[i + 1][0] + 1, self.rope[i + 1][1] - 1)
                else:
                    if self.rope[i + 1][1] < self.rope[i][1]:
                        self.rope[i + 1] = (self.rope[i + 1][0] - 1, self.rope[i + 1][1] + 1)
                    else:
                        self.rope[i + 1] = (self.rope[i + 1][0] - 1, self.rope[i + 1][1] - 1)
        
        if self.rope[-1] not in self.previous_distances:
            self.previous_distances.append(self.rope[-1])
                        
    def checkPrevious(self):
        if self.rope[-1] not in self.previous_distances:
            self.previous_distances.append(self.rope[-1])
    
    def move(self, move):
        self.moveHead(move)
        for i in range(len(self.rope) - 1):
            self.moveNonHead(i)
    
    def moveDistance(self, move, distance):
        for _ in range(distance):
            self.move(move)
        
    def returnUnique(self):
        return len(self.previous_distances)
    
def processInput():
    for line in lines:
        move, distance = line.split()
        distance = int(distance)
        
        yield move, distance

# Part 1 
length = 2
rope = Rope(length)
for move, distance in processInput():
    rope.moveDistance(move, distance)

print("part1: ", rope.returnUnique())

# Part 2
length = 10
rope = Rope(length)
for move, distance in processInput():
    rope.moveDistance(move, distance)
    
print("part2: ", rope.returnUnique())
