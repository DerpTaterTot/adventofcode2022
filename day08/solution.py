filein = open("day08/input.txt", "r")

lines = filein.readlines()

class Trees:
    def __init__(self, trees) -> None:
        self.trees = trees
        self.referencetree = [row[:] for row in trees] # copy the list
        
    def visibleRow(self):
        count = 0
        for i in range(len(self.trees)):
            maxHeight = -1
            for j in range(len(self.trees[i]) - 1):
                if self.trees[i][j] > maxHeight:
                    count += 1
                    maxHeight = self.trees[i][j]
                    self.referencetree[i][j] = -1
                    
            maxHeight = -1
            for j in range(1, len(self.trees)):
                location = self.trees[i][len(self.trees) - j]
                if location > maxHeight:
                    maxHeight = location
                    if self.referencetree[i][len(self.trees) - j] != -1:
                        count += 1
                        self.referencetree[i][len(self.trees) - j] = -1
                    
        return count
                    
    def visibleCol(self):
        count = 0
        
        for i in range(len(self.trees[0])):
            maxHeight = -1
            for j in range(len(self.trees)):
                if self.trees[j][i] > maxHeight:
                    maxHeight = self.trees[j][i]
                    if self.referencetree[j][i] != -1:
                        count += 1
                        self.referencetree[j][i] = -1
        
            maxHeight = -1
            for j in range(1, len(self.trees)):
                if self.trees[len(self.trees) - j][i] > maxHeight:
                    maxHeight = self.trees[len(self.trees) - j][i]
                    if self.referencetree[len(self.trees) - j][i] != -1:
                        count += 1
                        self.referencetree[len(self.trees) - j][i] = -1   
                             
        return count

    def checkLeft(self, tree_i, tree_j):
        height = self.trees[tree_i][tree_j]
        distance = 0
        
        for j in range(tree_j - 1, -1, -1): # this range is from tree_j to 0, -1 is the step
            distance += 1
            if self.trees[tree_i][j] >= height:
                return distance
            
        return distance

    def checkRight(self, tree_i, tree_j):
        height = self.trees[tree_i][tree_j]
        distance = 0
        
        for j in range(tree_j + 1, len(self.trees[tree_i])):
            distance += 1
            
            if self.trees[tree_i][j] >= height:
                return distance
            
        return distance
            
    def checkUp(self, tree_i, tree_j):
        height = self.trees[tree_i][tree_j]
        distance = 0
        
        for i in range(tree_i - 1, -1, -1):
            distance += 1
            
            if self.trees[i][tree_j] >= height:
                return distance

        return distance
    
    def checkDown(self, tree_i, tree_j):
        height = self.trees[tree_i][tree_j]
        distance = 0
        
        for i in range(tree_i + 1, len(self.trees)):
            distance += 1
            
            if self.trees[i][tree_j] >= height:
                return distance

        return distance
    
    def calculateTotal(self, tree_i, tree_j):
        return self.checkLeft(tree_i, tree_j) * self.checkRight(tree_i, tree_j) * self.checkUp(tree_i, tree_j) * self.checkDown(tree_i, tree_j)
    
    def findMaxScore(self):
        maxScore = 0
        for i in range(len(self.trees)):
            for j in range(len(self.trees[i])):
                maxScore = max(maxScore, self.calculateTotal(i, j))
                
        return maxScore
    
def processInput():
    trees = []
    for i in range(len(lines)):
        trees.append([])
        lines[i] = lines[i].replace("\n", "")
        for height in lines[i]:
            trees[i].append(int(height))
    return Trees(trees)

trees = processInput()
total = trees.visibleRow() + trees.visibleCol()

print("part1: " + str(total))
print("part2: " + str(trees.findMaxScore()))
