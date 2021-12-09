niet_input = open('input.txt', 'r')
heightmap = niet_input.readlines()
niet_input.close()

heightmap.insert(0, [9] * (len(heightmap[0]) + 1))
heightmap.append([9] * len(heightmap[0]))
sum = 0

for i in range(1, len(heightmap) - 1):
    heightmap[i] = list(map(int, heightmap[i][:-1]))
    heightmap[i] = [9] + heightmap[i] + [9]

for i in range(1, len(heightmap) - 1):
    for k in range(1, len(heightmap[i]) - 1):
        if heightmap[i][k] < heightmap[i - 1][k] and heightmap[i][k] < heightmap[i][k - 1] and heightmap[i][k] < heightmap[i + 1][k] and heightmap[i][k] < heightmap[i][k + 1]:
            sum += (1 + heightmap[i][k])
print("Sum:", sum)
