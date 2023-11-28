i = 0
markers = []
stop = 0

with open('.\Day6\input_Day6.txt') as f:
    lines = f.readlines()

for line in lines:
    while i < len(line):
        if len(markers) >= 4:
            markers.pop(0)
        markers.append(line[i])
        if (len(markers) >=4 and markers[0] != markers[1] and markers[0] != markers[2] and markers[0] != markers[3] and markers[1] != markers[2] and markers[1] != markers[3] and markers[2] != markers[3]):
            stop = i + 1
            break
        i += 1

print(markers)
print(stop)