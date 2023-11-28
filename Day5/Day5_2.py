totaal = []
stack = 0
line_nr = 0
move_nr = 0
move_from = 0
move_to = 0
move = 0
answer = ''

while stack < 9:
    totaal.append([])
    stack += 1

with open('.\Day5\Input_Day5.txt') as f:
    lines = f.readlines()

stack = 0
for line in lines:
    if line_nr < 8:
        while stack < 9:
            if line[(stack * 4) + 1] != ' ': totaal[stack].append(line[(stack * 4) + 1])
            stack += 1
        stack = 0

    if line_nr >= 10:
        move_nr = int(line.split(' ')[1])
        move_from = int(line.split(' ')[3])
        move_to = int(line.split(' ')[5])
        move = move_nr - 1
        while move >= 0:
            totaal[move_to - 1].insert(0, totaal[move_from - 1][move])
            move -= 1
        move = 0
        while move < move_nr:
            totaal[move_from - 1].pop(0)
            move += 1
    line_nr += 1

stack = 0
while stack < 9:
    print(totaal[stack])
    answer += totaal[stack][0]
    stack += 1

print(answer)