filein = open('day01/input.txt', 'r')

lines = filein.readlines()

def calculateTotal():
    top3 = [0, 0, 0]
    total = 0
    
    for line in lines:
        if line != "\n":
            total += int(line)
        else:
            if total > top3[0]:
                top3[0] = total
                top3.sort()
            
            total = 0
            
    return top3

top3 = calculateTotal()
print("part1:", top3[2])
print("part2:", sum(top3))