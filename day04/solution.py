filein = open("day04/input.txt", "r")

lines = filein.readlines()

def processInput(line):
    line = line.replace("\n", "").split(",")

    pair1 = line[0].split("-")
    pair2 = line[1].split("-")

    for i in range(2):
        pair1[i] = int(pair1[i])
        pair2[i] = int(pair2[i])

    return pair1, pair2

def isContaining(pair1, pair2):
    if pair1[0] >= pair2[0] and pair1[1] <= pair2[1]:
        return True

    elif pair2[0] >= pair1[0] and pair2[1] <= pair1[1]:
        return True

    return False

def isContaining2(pair1, pair2):
    if pair1[0] >= pair2[0] and pair1[0] <= pair2[1]:
        return True
    
    elif pair2[0] >= pair1[0] and pair2[0] <= pair1[1]:
        return True
    
    return False

def calculateTotal():
    total = 0
    for line in lines:
        pair1, pair2 = processInput(line)
        if isContaining(pair1, pair2):
            total += 1

    return total

def calculateTotal2():
    total = 0
    for line in lines:
        pair1, pair2 = processInput(line)
        if isContaining2(pair1, pair2):
            total += 1
            
    return total

print("part1:", calculateTotal())
print("part2:", calculateTotal2())
