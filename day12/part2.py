filein = open('day12/input.txt', 'r')

lines = filein.readlines()

def findLocation(hmap, value):
    for row in range(len(hmap)):
        for col in range(len(hmap[row])):
            if hmap[row][col] == value:
                location = (row, col)
                return location
    

def processInput():
    hmap = []
    for line in lines:
        hmap.append([(ord(i) - ord('a')) for i in line.strip('\n')])
    
    start = findLocation(hmap, -14)
    end = findLocation(hmap, -28)
            
    hmap[start[0]][start[1]] = 0
    hmap[end[0]][end[1]] = 25
                
    return hmap, start, end

def cost(coord, end):
    # find the distance from the start to the current coord and the end to the current coord and add them together
    endDist = abs(end[0] - coord[0]) + abs(end[1] - coord[1])
    
    return endDist

def cost2(hmap, coord): # part 2 cost
    cost = hmap[coord[0]][coord[1]]
    
    return cost

def getNeighbors(hmap, coord):
    # return the neighbors of the current coord and check if they are valid
    neighbors = []

    currentHeight = hmap[coord[0]][coord[1]]
    
    if coord[0] >= 1 and (hmap[coord[0] - 1][coord[1]] - currentHeight >= -1):
        neighbors.append((coord[0] - 1, coord[1]))
    if coord[0] <= len(hmap) - 2 and hmap[coord[0] + 1][coord[1]] - currentHeight >= -1:
        neighbors.append((coord[0] + 1, coord[1]))
    if coord[1] >= 1 and hmap[coord[0]][coord[1] - 1] - currentHeight >= -1:
        neighbors.append((coord[0], coord[1] - 1))
    if coord[1] <= len(hmap[0]) - 2 and hmap[coord[0]][coord[1] + 1] - currentHeight >= -1:
        neighbors.append((coord[0], coord[1] + 1))
    
    # check if the neighbors exist and are only 1 unit higher or lower
    
    return neighbors

def findBestPath(hmap, start):
    # using A* algorithm
    queue = []
    
    # queue.append((start, steps, cost, parent))
    queue.append((start, 0, cost2(hmap, start), start))
    
    visited = {} # key = coordinate, values are steps and parent
        
    current = None
    while queue:
        # print('\n'*3)
        # print(visited)
        # set current to the node with the lowest cost
        current = min(queue, key=lambda x: x[1] + x[2])
        visited[current[0]] = (current[1], current[3]) # steps and parent
        queue.remove(current)
        
        if hmap[current[0][0]][current[0][1]] == 0:
            print('goal reached')
            return current[0], visited
        
        for neighbor in getNeighbors(hmap, current[0]):
            if neighbor not in visited:
                queuelist = [x[0] for x in queue]
                if neighbor in queuelist:
                    idx = queuelist.index(neighbor)
                    if current[1] + 1 < queue[idx][1]:
                        queue.pop(idx)
                        queue.append((neighbor, current[1] + 1, cost2(hmap, neighbor), current[0]))
                else:
                # checking if neighbor coordinates not in queue or already visited
                    queue.append((neighbor, current[1] + 1, cost2(hmap, neighbor), current[0]))
    
def visualizePath(hmap, bestPath):
    # edit the hmap to show the path as upper and the start and end as S and E
    for loc in bestPath:
        hmap[loc[0]][loc[1]] = hmap[loc[0]][loc[1]] + ord('A')-ord('a')
    
    for row in hmap:
        for col in row:
            print(chr(col + ord('a')), end='')
        print('')

hmap, start, end = processInput()
location, visited = findBestPath(hmap, end)

# print(visited)

bestPath = []
current = location
while not current == end:
    bestPath.append(current)
    current = visited[current][1]
    
bestPath.append(end)
bestPath.reverse()

# print(start, end)
# print(visited)
print("distance:", visited[location][0])
# print("-----visualized path-----")
visualizePath(hmap, bestPath)