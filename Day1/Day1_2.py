max_calories = 0

elf_calories = 0
elf_array = []

with open('.\Day1\Input_Day1.txt') as file:
    lines = file.readlines()

for line in lines:
    if line.rstrip('\n') == '':
        elf_array.append(elf_calories)
        elf_calories = 0
    else:
        elf_calories += int(line.rstrip('\n'))

elf_array.append(elf_calories)
elf_array.sort(reverse=True)
max_calories = elf_array[0] + elf_array[1] + elf_array[2]

print(max_calories)