filein = open("day10/input.txt", "r")

lines = filein.readlines()

values = [1] # each index is a cycle

def processInput():
    for line in lines:
        line = line.split()
        
        if line[0] == "addx":
            values.append(int(values[-1]))
            values.append(int(values[-1]) + int(line[1]))
            
        elif line[0] == "noop":
            values.append(int(values[-1]))
            
    return values

def calculateSum(values):
    total = 0
    for i in range(20, 221, 40):
        total += values[i - 1] * i
    
    return total

def printCRT(values):
    sprite = 0
    for i in range(len(values)): 
        if i % 40 == 39:
            end = "\n"
        elif i % 40 == 0:
            end = ""
            sprite = 0
        else:
            end = ""
            sprite += 1
        
        if abs(values[i] - sprite) <= 1:
            print("#", end=end)
        else:
            print(".", end=end)

values = processInput()

print("part1:", calculateSum(values))
print("part2:")
printCRT(values)
    

    
    
    
    
    
    
