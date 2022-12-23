filein = open("day10/input.txt", "r")

lines = filein.readlines()

values = [1]

for line in lines:
    line = line.split()
    
    if line[0] == "addx":
        values.append(int(values[-1]))
        values.append(int(values[-1]) + int(line[1]))
        
    elif line[0] == "noop":
        values.append(int(values[-1]))
        
total = 0

sprite = 0
for i in range(len(values) - 1):
    if i % 40 == 39:
        end = "\n"
    elif i % 40 == 0:
        end = ""
        sprite = 0
    else:
        end = ""
        sprite += 1
    
    if abs(values[i] - sprite) <= 1:
        print("#", end=end)
    else:
        print(".", end=end)


    

    
    
    
    
    
    
