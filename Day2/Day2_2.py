score = 0

with open('.\Day2\Input_Day2.txt') as file:
    lines = file.readlines()

for line in lines:
    # I win.
    if (line[2] == "Z"):
        score += 6
    # It's a draw
    if (line[2] == "Y"):
        score += 3
    # I have rock
    if (line[0] == "B" and line[2] == "X") or (line[0] == "A" and line[2] == "Y") or (line[0] == "C" and line[2] == "Z"):
        score += 1
    # I have paper
    if (line[0] == "C" and line[2] == "X") or (line[0] == "B" and line[2] == "Y") or (line[0] == "A" and line[2] == "Z"):
        score += 2
    # I have scissors
    if (line[0] == "A" and line[2] == "X") or (line[0] == "C" and line[2] == "Y") or (line[0] == "B" and line[2] == "Z"):
        score += 3

print(score)