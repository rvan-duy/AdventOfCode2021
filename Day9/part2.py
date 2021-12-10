niet_input = open('input.txt', 'r')
heightmap = niet_input.readlines()
niet_input.close()

heightmap.insert(0, [9] * (len(heightmap[0]) + 1))
heightmap.append([9] * (len(heightmap[0]) + 1))
sum_of_map = 0

# Change map to ints with walls (10)
for i in range(1, len(heightmap) - 1):
    heightmap[i] = list(map(int, heightmap[i][:-1]))
    heightmap[i] = [9] + heightmap[i] + [9]


def floodfill(x, y, heightmap):
    basin_size = 0
    if heightmap[x][y] < 9:
        basin_size += 1
        heightmap[x][y] = 9
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

# for row in heightmap:
#     print(row)

print(basin_sizes)
basin_sizes.sort()

print("final_basin_sizes", basin_sizes)
print(basin_sizes[-1] * basin_sizes[-2] * basin_sizes[-3])
