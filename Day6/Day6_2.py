i = 0
markers = []
markers_sort = []
stop = 0
marker_loop = 0

with open('.\Day6\input_Day6.txt') as f:
    lines = f.readlines()

for line in lines:
    while i < len(line):
        if len(markers) >= 14:
            markers.pop(0)
        markers.append(line[i])
        markers_sort = markers.copy()
        markers_sort.sort()
        if len(markers) >= 14:
            marker_loop = 0
            while marker_loop < len(markers_sort) - 1:
                if (markers_sort[marker_loop] == markers_sort[marker_loop + 1]):
                    break
                if marker_loop == len(markers_sort) - 2 and stop == 0:
                    stop = i + 1
                    break
                marker_loop += 1
        i += 1

print(markers_sort)
print(markers)
print(stop)