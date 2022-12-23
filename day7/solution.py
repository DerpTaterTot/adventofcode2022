filein = open("day7/input.txt", "r")

lines = filein.readlines()

dirDict = {"/": []}
fileDict = {}
location = "/"

for line in lines:
    line = line.split()
    
    if line[0] == "$":
        if line[1] == "cd":
            if line[2] == "..":
                location = "/".join(location.split("/")[0:-2]) + "/" # move back one folder

            else:
                if line[2] != "/":
                    location += line[2] + "/" # set location to cd value
    
    elif line[0] == "dir":
        dirDict[location].append(location + line[1] + "/") # add the directory to the dictionary
        dirDict[dirDict[location][-1]] = [] # create a new entry for the dictionary at the recent added value
        
    else: # file size case
        if location not in fileDict:
            fileDict[location] = 0

        fileDict[location] += int(line[0])

def findFolderSize(folder):
    if folder in fileDict:
        total = fileDict[folder]
    else:
        total = 0
    
    for directory in dirDict[folder]:
        total += findFolderSize(directory)
        
    return total


total = 70000000
needed = 30000000

used = findFolderSize("/") # 5000000
spaceDeleted = used - (total - needed)

#print(used - spaceDeleted)
result = findFolderSize("/")
for folder in dirDict:
    fs = findFolderSize(folder)
    if fs >= spaceDeleted and result > fs:
        result = fs

print(result)
# total should be 41272621
"""
print(fileDict["/"])
total = 0
for folder in dirDict["/"]:
    print(folder + " size: " + str(findFolderSize(folder)))
"""