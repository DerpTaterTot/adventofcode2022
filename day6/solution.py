from collections import Counter

filein = open("day6/input.txt", "r")

line = filein.readlines()[0]

def allUnique(string):
    freq = Counter(string)
    return len(freq) == len(string)
    
i = 0
string = line[i:i+14]
while not allUnique(string):
    string = line[i:i+14]
    i += 1
    
print(i + 13) # i + 4 but since we add 1 its i + 3

  

