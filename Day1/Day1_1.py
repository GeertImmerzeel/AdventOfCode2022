max_calories = 0
elf_calories = 0

with open('.\Day1\Input_Day1.txt') as file:
    lines = file.readlines()

for line in lines:
    if line.rstrip('\n') == '':
        elf_calories = 0
    else:
        elf_calories += int(line.rstrip('\n'))
        if elf_calories > max_calories:
            max_calories = elf_calories

print(max_calories)