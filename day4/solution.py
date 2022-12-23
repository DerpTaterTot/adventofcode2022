import random

filein = open("day4/input.txt", "r")

lines = filein.readlines()

total = 0

for line in lines:
    line = line.replace("\n", "").split(",")

    pair1 = line[0].split("-")
    pair2 = line[1].split("-")

    for i in range(2):
        pair1[i] = int(pair1[i])
        pair2[i] = int(pair2[i])

    if pair1[0] >= pair2[0] and pair1[1] <= pair2[1]:
        total += 1

    elif pair2[0] >= pair1[0] and pair2[1] <= pair1[1]:
        total += 1
        
print(total)

