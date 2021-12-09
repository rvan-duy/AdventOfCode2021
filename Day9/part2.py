niet_input = open('input.txt', 'r')
heightmap = niet_input.readlines()
niet_input.close()

heightmap.insert(0, [10] * (len(heightmap[0]) + 1))
heightmap.append([10] * len(heightmap[0]))
sum_of_map = 0

# Change map to ints with walls (10)
for i in range(1, len(heightmap) - 1):
    heightmap[i] = list(map(int, heightmap[i][:-1]))
    heightmap[i] = [10] + heightmap[i] + [10]


def floodfill(x, y, heightmap):
    basin_size = 0
    if heightmap[x][y] < 9 and \
            heightmap[x][y] < heightmap[x - 1][y] and \
            heightmap[x][y] < heightmap[x + 1][y] and \
            heightmap[x][y] < heightmap[x][y - 1] and \
            heightmap[x][y] < heightmap[x][y + 1]:
        basin_size += 1
        heightmap[x][y] += 20
        basin_size += floodfill(x, y + 1, heightmap)
        basin_size += floodfill(x, y - 1, heightmap)
        basin_size += floodfill(x + 1, y, heightmap)
        basin_size += floodfill(x - 1, y, heightmap)
    return basin_size


basin_sizes = []
for i in range(1, len(heightmap) - 1):
    for k in range(1, len(heightmap[i]) - 1):
        basin_size = floodfill(i, k, heightmap)
        if basin_size != 0:
            basin_sizes.append(basin_size)

for row in heightmap:
    print(row)

final_basin_sizes = []
for i in range(0, 3):
    max = 0
    for j in range(len(basin_sizes)):
        if basin_sizes[j] > max:
            max = basin_sizes[j]

    basin_sizes.remove(max)
    final_basin_sizes.append(max)

print("final_basin_sizes", final_basin_sizes)
print(9 * 14 * 9)
