filein = open("day2/input.txt", "r")

lines = filein.readlines()

# win = 6, draw = 3, loss = 0
# rock = 1, paper = 2, scissors = 3

scoring = {"A": {"X": 4, "Y": 8, "Z": 3}, "B": {"X": 1, "Y": 5, "Z": 9}, "C": {"X": 7, "Y": 2, "Z": 6}}

total = 0
for line in lines:
    total += scoring[line[0]][line[2]]
    
print(total)   

# x = lose, y = tie, z = win
scoring = {"A": {"X": 3, "Y": 4, "Z": 8}, "B": {"X": 1, "Y": 5, "Z": 9}, "C": {"X": 2, "Y": 6, "Z": 7}}
 
total = 0
for line in lines:
    total += scoring[line[0]][line[2]]
    
print(total)
