filein = open("day03/input.txt", "r")

lines = filein.readlines()


def processInput(line):
    line = line.replace("\n", "")
    
    sack1 = set(line[:int(len(line)/2)])
    sack2 = set(line[int(len(line)/2):])
        
    return sack1, sack2

def processInput2(i):
    sack1 = set(lines[i].replace("\n", ""))
    sack2 = set(lines[i + 1].replace("\n", ""))
    sack3 = set(lines[i + 2].replace("\n", ""))
    
    return sack1, sack2, sack3

def calculateValue(letter):
    valueString = "abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ"
    
    return valueString.index(letter) + 1


def calculateIntersection(sack1, sack2):
    sack1.intersection_update(sack2)
    for i in sack1:
        val = calculateValue(i)
            
    return val

def calculateIntersection2(sack1, sack2, sack3):
    sack1.intersection_update(sack2)
    sack1.intersection_update(sack3)
    
    for i in sack1:
        val = calculateValue(i)

    return val

def calculateTotal():
    total = 0
    for line in lines:
        sack1, sack2 = processInput(line)  
        total += calculateIntersection(sack1, sack2)
    
    return total

def calculateTotal2():
    total = 0
    for i in range(0, len(lines), 3):
        sack1, sack2, sack3 = processInput2(i)
        total += calculateIntersection2(sack1, sack2, sack3)
    
    return total


print("part1:", calculateTotal())
print("part2:", calculateTotal2())

