file = open('input.txt')
file_input = file.readlines()
file.close()

max_x, max_y = 0, 0
for i in range(len(file_input)):
    file_input[i] = file_input[i][:-1].split()
    file_input[i].remove('->')
    file_input[i][0] = file_input[i][0].split(',')
    file_input[i][1] = file_input[i][1].split(',')
    max_x = max(max_x, int(file_input[i][0][0]), int(file_input[i][1][0]))
    max_y = max(max_y, int(file_input[i][0][1]), int(file_input[i][1][1]))

diagram = []
x, y = 0, 0
while x < max_x + 1:
    diagram.append([])
    y = 0
    while y < max_y + 1:
        diagram[x].append(0)
        y += 1
    x += 1

for entry in file_input:

    if entry[0][0] != entry[1][0] and entry[0][1] != entry[1][1]:
        # print(entry)
        start_x = int(entry[0][1])
        start_y = int(entry[0][0])
        end_x = int(entry[1][1])
        end_y = int(entry[1][0])
        x_modifier = -1 if start_x > end_x else 1
        y_modifier = -1 if start_y > end_y else 1
        while start_x != end_x and start_y != end_y:
            # print(start_x, start_y)
            diagram[start_x][start_y] += 1
            start_x += x_modifier
            start_y += y_modifier
        diagram[start_x][start_y] += 1
    elif entry[0][0] != entry[1][0]:
        end = max(int(entry[0][0]), int(entry[1][0]))
        start = min(int(entry[0][0]), int(entry[1][0]))
        for i in range(start, end + 1):
            diagram[int(entry[0][1])][i] += 1
    elif entry[0][1] != entry[1][1]:
        end = max(int(entry[0][1]), int(entry[1][1]))
        start = min(int(entry[0][1]), int(entry[1][1]))
        for i in range(start, end + 1):
            diagram[i][int(entry[0][0])] += 1

total_overlap_points = 0
for row in diagram:
    for element in row:
        if element > 1:
            total_overlap_points += 1
    print(row)

print('Amount of times points overlap:', total_overlap_points)

# print(max_x, max_y)
# print(file_input)

