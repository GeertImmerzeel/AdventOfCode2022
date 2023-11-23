import math

score = 0
first = ""
second = ""
ascii_value = 0

with open('.\Day3\Input_Day3.txt') as file:
    lines = file.readlines()

for line in lines:
    first = line[0:math.ceil(len(line)/2) - 1]
    second = line[math.ceil(len(line)/2) - 1:len(line)]
    for character in first:
        if character in second:
            ascii_value = ord(character)
            score += ascii_value - 96 if ascii_value >= 97 else ascii_value - 38
            break

print(score)