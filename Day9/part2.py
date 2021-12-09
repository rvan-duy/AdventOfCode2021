niet_input = open('simple_input.txt', 'r')
heightmap = niet_input.readlines()
niet_input.close()

heightmap.insert(0, [10] * (len(heightmap[0]) + 1))
heightmap.append([10] * len(heightmap[0]))
sum_of_map = 0

# Change map to ints with walls (10)
for i in range(1, len(heightmap) - 1):
    heightmap[i] = list(map(int, heightmap[i][:-1]))
    heightmap[i] = [10] + heightmap[i] + [10]


def floodfill(heightmap, x, y):
    print(type(heightmap[x][y]))
    if heightmap[x][y] < 9:
        heightmap[x][y] += 20
        floodfill(x, y + 1, heightmap)
        floodfill(x, y - 1, heightmap)
        floodfill(x + 1, y, heightmap)
        floodfill(x - 1, y, heightmap)



for i in range(1, len(heightmap) - 1):
    for k in range(1, len(heightmap[i]) - 1):
        floodfill(heightmap, i, k)

# for i in range(1, len(heightmap) - 1):
#     for k in range(1, len(heightmap[i]) - 1):
#         queue.append([i, k])
#         print(queue)
#         basin_size = 0
#         for element in queue:
#             if heightmap[queue[0][0]][queue[0][1]] < 9:
#                 print("Test:", heightmap[queue[0][0]][queue[0][1]], heightmap[queue[0][0] + 1][queue[0][1]], heightmap[queue[0][0] - 1][queue[0][1]], heightmap[queue[0][0]][queue[0][1] - 1], heightmap[queue[0][0]][queue[0][1] + 1])
#                 if heightmap[queue[0][0]][queue[0][1]] < heightmap[queue[0][0] - 1][queue[0][1]] and \
#                         heightmap[queue[0][0]][queue[0][1]] < heightmap[queue[0][0] + 1][queue[0][1]] and \
#                         heightmap[queue[0][0]][queue[0][1]] < heightmap[queue[0][0]][queue[0][1] - 1] and \
#                         heightmap[queue[0][0]][queue[0][1]] < heightmap[queue[0][0]][queue[0][1] + 1]:
#                     print(queue)
#                     heightmap[[queue[0][0]][queue[0][1]]] += 20
#                     print("Hello?")
#                     basin_size += 1
#                 queue.pop(0)
#
#
#                 # heightmap[i][k] += 20
#                 # queue.append([i - 1, k])
#                 # queue.append([i + 1, k])
#                 # queue.append([i, k - 1])
#                 # queue.append([i, k + 1])
#                 # basin_size += 4

for row in heightmap:
    print(row)

print("Sum:", basin_size)
