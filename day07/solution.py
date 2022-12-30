class Folder:
    def __init__(self, name, parent) -> None:
        self.name = name
        self.parent = parent
        self.size = 0
        self.subs = []
        self.totalsize = 0
        
    def add_sub(self, name):
        folder = Folder(name, self)
        self.subs.append(folder)
        
        return folder
    
    def add_size(self, size):
        self.size += size
        
    def calculatetotalsize(self):
        total = self.size
        
        for sub in self.subs:
            total += sub.calculatetotalsize()
            
        self.totalsize = total
        return self.totalsize
    
    def calculateTotalLimited(self, limit):
        global total_limited
        
        if self.totalsize <= limit:
            total_limited += self.totalsize
            
        for sub in self.subs:
            sub.calculateTotalLimited(limit)

    def findClosest(self, goal):
        # folder has to be bigger than goal but as close as possible
        global smallest
        
        if self.totalsize > goal and self.totalsize < smallest:
            smallest = self.totalsize
            
        for sub in self.subs:
            sub.findClosest(goal)

def processInput():
    lines = open("day07/input.txt", "r").readlines()
    
    dummy = Folder(None, None)
    
    current = dummy
    for line in lines:
        line = line.split()
        
        if line[0] == "$":
            if line[1] == "cd":
                if line[2] == "..":
                    current = current.parent
                else:
                    current = current.add_sub(line[2])
        elif line[0].isdigit():
            current.add_size(int(line[0]))
            
    return dummy.subs[0]

def part1():
    root = processInput()
    root.calculatetotalsize()
    
    global total_limited
    total_limited = 0
    
    limit = 100000
    root.calculateTotalLimited(limit)
    
    return total_limited

def part2():
    root = processInput()
    root.calculatetotalsize()
    
    global smallest
    smallest = root.totalsize
    
    total = 70000000
    needed = 30000000
    
    used = root.totalsize
    
    deleted = used - (total - needed)
    
    root.findClosest(deleted)
    
    return smallest

print(part1())
print(part2())