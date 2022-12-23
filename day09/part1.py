filein = open("day9/input.txt", "r")

lines = filein.readlines()

previous_distances = []
    
rope = [(0, 0)] * 10

for line in lines:
    move, distance = line.split()
    print(move, distance)
    for _ in range(int(distance)):
        if move == "U":
            rope[0] = (rope[0][0], rope[0][1] + 1)
        elif move == "D":
            rope[0] = (rope[0][0], rope[0][1] - 1)
        elif move == "L":
            rope[0] = (rope[0][0] - 1, rope[0][1])
        elif move == "R":
            rope[0] = (rope[0][0] + 1, rope[0][1])
        # iterate through the rope from the beginning to the end
        for i in range(len(rope) - 1):
            # update rope[i + 1]
            if rope[i + 1][0] == rope[i][0] and abs(rope[i + 1][1] - rope[i][1]) > 1:
                # print("updating y ")
                if rope[i + 1][1] < rope[i][1]:
                    rope[i + 1] = (rope[i + 1][0], rope[i + 1][1] + 1)
                else:
                    rope[i + 1] = (rope[i + 1][0], rope[i + 1][1] - 1)

            elif rope[i + 1][1] == rope[i][1] and abs(rope[i + 1][0] - rope[i][0]) > 1:
                # print("updating x")
                # print("i: ", i)
                # print("rope[i + 1][0]: ", rope[i + 1][0])
                # print("rope[i][0]: ", rope[i][0])
                if rope[i + 1][0] < rope[i][0]:
                    rope[i + 1] = (rope[i + 1][0] + 1, rope[i + 1][1])
                else:
                    rope[i + 1] = (rope[i + 1][0] - 1, rope[i + 1][1])

            else:
                # check if rope[i + 1] is not directly diagonal from rope[i] and touching
                if not (abs(rope[i + 1][0] - rope[i][0]) == 1 and abs(rope[i + 1][1] - rope[i][1]) == 1) and (abs(rope[i + 1][0] - rope[i][0]) > 1 or abs(rope[i + 1][1] - rope[i][1]) > 1):
                    # find where the rope[i] is in relation to the rope[i + 1]
                    if rope[i + 1][0] < rope[i][0]:
                        if rope[i + 1][1] < rope[i][1]:
                            rope[i + 1] = (rope[i + 1][0] + 1, rope[i + 1][1] + 1)
                        else:
                            rope[i + 1] = (rope[i + 1][0] + 1, rope[i + 1][1] - 1)
                    else:
                        if rope[i + 1][1] < rope[i][1]:
                            rope[i + 1] = (rope[i + 1][0] - 1, rope[i + 1][1] + 1)
                        else:
                            rope[i + 1] = (rope[i + 1][0] - 1, rope[i + 1][1] - 1)
                            
            if rope[-1] not in previous_distances:
                previous_distances.append(rope[-1])
    print(rope)

print(len(previous_distances))
    

    
    
    
    
    
    
