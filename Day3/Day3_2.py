import math

score = 0
first = ""
second = ""
third = ""
counter = 0
ascii_value = 0

with open('.\Day3\Input_Day3.txt') as file:
    lines = file.readlines()

for line in lines:
    if counter % 3 == 0:
        first = line
    if counter % 3 == 1:
        second = line
    if counter % 3 == 2:
        third = line
        for character in first:
            if character in second:
                if character in third:
                    ascii_value = ord(character)
                    score += ascii_value - 96 if ascii_value >= 97 else ascii_value - 38
                    break
    counter += 1

print(score)