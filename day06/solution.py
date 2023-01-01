from collections import Counter

filein = open("day06/input.txt", "r")

line = filein.readline()

def allUnique(string):
    freq = Counter(string)
    return len(freq) == len(string)

def countCharacters(length):
    i = 0
    string = line[i:i+length]
    while not allUnique(string):
        string = line[i:i+length]
        i += 1
    
    return i + length - 1

print("part1: " + str(countCharacters(4)))
print("part2: " + str(countCharacters(14)))

  

