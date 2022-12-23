import re

filein = open("day5/input.txt", "r")

lines = filein.readlines()

boxes = [[], [], [], [], [], [], [], [], []]

i = 0
while lines[i][1] != "1":
    line = lines[i]
    for j in range(1, 36, 4):
        if line[j] != " ":
            boxes[int((j - 1) / 4)].append(line[j])
    i += 1
    
for i in range(9):
    boxes[i].reverse()
    

numbers = re.compile(r'\d+(?:\.\d+)?')

stack = []
for i in range(10, 513):
# i = 10
    amount, initial, end = numbers.findall(lines[i])
    amount = int(amount)
    initial = int(initial) - 1
    end = int(end) - 1

    for _ in range(amount):
        stack.append(boxes[initial].pop())
        
    for _ in range(len(stack)):
        boxes[end].append(stack.pop())
            
for i in range(9):
    print(boxes[i])