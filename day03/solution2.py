filein = open("day3/input.txt", "r")

lines = filein.readlines()

total = 0

for i in range(0, len(lines), 3):

    sack1 = set(lines[i].replace("\n", ""))
    sack2 = set(lines[i + 1].replace("\n", ""))
    sack3 = set(lines[i + 2].replace("\n", ""))
    
    sack1.intersection_update(sack2)
    sack1.intersection_update(sack3)
    
    for i in sack1:
        val = ord(i) - 96
        if val < 0:
            val += 58
            
    total += val
    
print(total)

