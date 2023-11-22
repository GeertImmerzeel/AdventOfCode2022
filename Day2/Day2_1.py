score = 0

with open('.\Day2\Input_Day2.txt') as file:
    lines = file.readlines()

for line in lines:
    if (line[0] == "A" and line[2] == "Y") or (line[0] == "B" and line[2] == "Z") or (line[0] == "C" and line[2] == "X"):
        score += 6
    if (line[0] == "A" and line[2] == "X") or (line[0] == "B" and line[2] == "Y") or (line[0] == "C" and line[2] == "Z"):
        score += 3
    if (line[2] == "X"):
        score += 1
    if (line[2] == "Y"):
        score += 2
    if (line[2] == "Z"):
        score += 3

print(score)