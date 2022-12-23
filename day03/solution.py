filein = open("day3/input.txt", "r")

lines = filein.readlines()

total = 0
for line in lines:
    line = line.replace("\n", "")

    sack1 = set(line[:int(len(line)/2)])
    sack2 = set(line[int(len(line)/2):])

    sack1.intersection_update(sack2)
    for i in sack1:
        val = ord(i) - 96
        if val < 0:
            val += 58
            
    total += val
    
print(total)

