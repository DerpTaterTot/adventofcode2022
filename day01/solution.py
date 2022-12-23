filein = open('day1/input.txt', 'r')

lines = filein.readlines()

top3 = [0] * 3

total = 0

for line in lines:
    if line != "\n":
        total += int(line)
    else:
        if total > top3[0]:
            top3[0] = total
            top3.sort()
        
        total = 0
        

print(sum(top3))