filein = open("day8/input.txt", "r")

lines = filein.readlines()

tree = []

for i in range(len(lines)):
    tree.append([])
    lines[i] = lines[i].replace("\n", "")
    for height in lines[i]:
        tree[i].append(int(height))

referencetree = [row[:] for row in tree]

count = 0
for line in referencetree:
    maxHeight = -1  
    for i in range(len(tree) - 1):#for i in range(50):
        if line[i] > maxHeight:
            count += 1
            maxHeight = line[i]
            line[i] = -1
            
    maxHeight = -1
    for i in range(1, len(tree)):
        if line[len(line) - i] > maxHeight:
            count += 1
            maxHeight = line[len(line) - i]
            line[len(line) - i] = -1

for i in range(len(tree[0])):
    maxHeight = -1
    for j in range(len(tree) - 1):
        if tree[j][i] > maxHeight:
            maxHeight = tree[j][i]
            if referencetree[j][i] != -1:
                count += 1
                referencetree[j][i] = -1
    maxHeight = -1
    for j in range(1, len(tree)):
        if tree[len(tree) - j][i] > maxHeight:
            maxHeight = tree[len(tree) - j][i]
            if referencetree[len(tree) - j][i] != -1:
                count += 1
                referencetree[len(tree) - j][i] = -1

# for row in referencetree:
#    print(row)
    
print("visible: " + str(count))