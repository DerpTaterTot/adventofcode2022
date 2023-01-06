filein = open('day13/input.txt', 'r')

lines = filein.readlines()

class Node:
    def __init__(self, parent, val=None) -> None:
        self.parent = parent
        self.children = []
        self.val = val
    
    def addChild(self, val=None):
        child = Node(self, val)
        self.children.append(child)
        
        return child        

def strToNode(line):
    dummy = Node(None)
    current = dummy
    line = line.strip('\n')
    
    i = 0
    while i < len(line):
        char = line[i]
        if char == '[':
            current = current.addChild()
            i += 1
        elif char == ']':
            current = current.parent
            i += 1
        elif char == ',':
            i += 1
        else:
            numStr = ""
            while line[i].isdigit():
                numStr += line[i]
                i += 1

            current.addChild(val = int(numStr))
    
    return dummy.children[0]

def processInput(part2 = False):
    pairs = []
    pair = []
    for line in lines:
        if line == "\n" and not part2:
            pairs.append(pair)
            pair = []
            continue
        elif line == "\n" and part2:
            continue
        
        tree = strToNode(line)
        
        pair.append(tree)
    
    pairs.append(pair)
    return pairs if not part2 else pair

def compare(node1, node2): # check if node2 is greater than node1
    if (node1.val is not None) and (node2.val is not None):
        return compareInt(node1.val, node2.val)
    
    elif (node1.val is None) and (node2.val is None):
        for i in range(min(len(node1.children), len(node2.children))):
            result = compare(node1.children[i], node2.children[i])
            if result != 0:
                return result    
        return compareInt(len(node1.children), len(node2.children)) # if all children are equal, compare length
    elif node1.val is not None:
        new = Node(node1, node1.val)
        node1.val = None
        node1.children = [new]
        
        return compare(node1, node2)
    
    elif node2.val is not None:
        new = Node(node2, node2.val)
        node2.val = None
        node2.children = [new]
        
        return compare(node1, node2)

def compareInt(val1, val2):
    if val1 < val2:
        return -1
    elif val1 == val2:
        return 0
    else:
        return 1

if __name__ == "__main__":
    # part 1
    pairs = processInput()
    total = 0     
    for i in range(len(pairs)):
        pair = pairs[i]
        if compare(pair[0], pair[1]) == -1:
            total += i + 1

    print("part1:", total)

    # part 2
    import functools

    lines += ["[[2]]", "[[6]]"]
    trees = processInput(part2=True)

    sorted_ind = sorted(range(len(trees)), key=functools.cmp_to_key(lambda i, j: compare(trees[i], trees[j])))
    total = (sorted_ind.index(len(trees) - 1) + 1) * (sorted_ind.index(len(trees) - 2) + 1) # len(trees) - 1 and len(trees) - 2 are the indices of the two new trees added (2 and 6)

    print("part2:", total)
