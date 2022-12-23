filein = open("day8/input.txt", "r")

lines = filein.readlines()

tree = []
def calculateScore(tree_i, tree_j):
    # score is found by multiplying together the viewing distance in each of the four directions
    
    total = 1
    distance = 0
    height = tree[tree_i][tree_j]

    # check left of height
    for j in range(tree_j - 1, -1, -1): # this range is from tree_j to 0, -1 is the step
        if tree[tree_i][j] < height:
            distance += 1
        else:
            distance += 1
            break
    
    total *= distance
    distance = 0
    
    # check right of height
    for j in range(tree_j + 1, len(tree[tree_i])):
        if tree[tree_i][j] < height:
            distance += 1
        else:
            distance += 1
            break
        
    total *= distance
    distance = 0
        
    # check above height
    for i in range(tree_i - 1, -1, -1):
        if tree[i][tree_j] < height:
            distance += 1
        else:
            distance += 1
            break

    total *= distance
    distance = 0
    
    # check below height
    for i in range(tree_i + 1, len(tree)):
        if tree[i][tree_j] < height:
            distance += 1
        else:
            distance += 1
            break
        
    total *= distance
    distance = 0
    
    return total
    

for i in range(len(lines)):
    tree.append([])
    lines[i] = lines[i].replace("\n", "")
    for height in lines[i]:
        tree[i].append(int(height))

# iterate through the tree and find the highest score
max = 0
for i in range(len(tree)):
    for j in range(len(tree[i])):
        score = calculateScore(i, j)
        if score > max:
            max = score

print(max)
