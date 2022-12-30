import re

filein = open("day05/input.txt", "r")

numbers = re.compile(r'\d+(?:\.\d+)?')

lines = filein.readlines()

class Boxes:
    def __init__(self, boxes):
        self.boxes = boxes
        self.queue = []
    
    def remove(self, index, amount, reverse = False):
        for _ in range(amount):
            self.queue.append(self.boxes[index].pop())
            
        if reverse:
            self.queue.reverse()
        
    def add(self, index):
        for _ in range(len(self.queue)):
            self.boxes[index].append(self.queue.pop(0))

    def returnTopCrates(self): # returns a list of the top crates in each index
        topCrates = []
        for i in range(len(self.boxes)):
            topCrates.append(self.boxes[i][-1])
        return topCrates
    
    def printBoxes(self):
        for i in range(len(self.boxes)):
            print(f"Box {i + 1}: {self.boxes[i]}")
    
def processInput(numBoxes):
    boxes = [[] for _ in range(numBoxes)]

    for i in range(len(lines)):
        lines[i] = lines[i].strip('\n')
        
        if lines[i][1] == "1":         
            for i in range(len(boxes)):
                boxes[i].reverse()
            return i + 2, boxes
        
        currentBox = -1
        for j in range(len(lines[i])):
            if j % 4 == 1:
                currentBox += 1
            if lines[i][j] not in "[ ]":
                boxes[currentBox].append(lines[i][j])       

def processInstructions(line):
    amount, initial, end = numbers.findall(line)
    
    amount = int(amount)
    initial = int(initial) - 1
    end = int(end) - 1
    
    return amount, initial, end

def compute(numBoxes, reverse):
    start, boxes = processInput(numBoxes)
    boxes = Boxes(boxes)
    
    for i in range(start, len(lines)):
        amount, initial, end = processInstructions(lines[i])
        
        boxes.remove(initial, amount, reverse)
        boxes.add(end)
        
    return boxes.returnTopCrates()

numBoxes = 9             
print("day 1:", compute(numBoxes, False))
print("day 2:", compute(numBoxes, True))
