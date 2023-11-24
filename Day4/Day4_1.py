import math

first_elf = ""
second_elf = ""
first_elf_start = 0
first_elf_end = 0
second_elf_start = 0
second_elf_end = 0

number_fully_contained = 0

with open('.\Day4\Input_Day4.txt') as file:
    lines = file.readlines()

for line in lines:
    first_elf = line.split(',')[0]
    second_elf = line.split(',')[1]
    first_elf_start = int(first_elf.split('-')[0])
    first_elf_end = int(first_elf.split('-')[1])
    second_elf_start = int(second_elf.split('-')[0])
    second_elf_end = int(second_elf.split('-')[1])
    if (first_elf_start <= second_elf_start and first_elf_end >= second_elf_end) or (first_elf_start >= second_elf_start and first_elf_end <= second_elf_end):
        number_fully_contained += 1

print(number_fully_contained)