input_file = open('input.txt', 'r')
lines = input_file.readlines()

for i in range(len(lines)):
    lines[i] = lines[i][:-1]

opening_brackets = ['(', '[', '{', '<']
closing_brackets = [')', ']', '}', '>']
total_points = []
for i in range(len(lines)):
    corrupted_line = 0
    line_len = len(lines[i])
    k = 0
    while k < line_len:
        # print(i, k, line_len, len(lines[i]), lines[i])
        if lines[i][k] in closing_brackets:
            index = closing_brackets.index(lines[i][k])
            if closing_brackets[index] == lines[i][k]:
                if opening_brackets[index] == lines[i][k - 1]:
                    lines[i] = lines[i][0:k:] + lines[i][k + 1::]
                    lines[i] = lines[i][0:k - 1:] + lines[i][k::]
                    line_len -= 2
                else:
                    corrupted_line = 1
                    break
                k = 0
        k += 1
    score = 0
    if corrupted_line == 0:
        line_len = len(lines[i])
        j = line_len - 1
        print(lines[i])
        while j >= 0:
            index_of_bracket = opening_brackets.index(lines[i][j]) + 1
            score = (score * 5) + index_of_bracket
            j -= 1
        total_points.append(score)


total_points.sort()
middle_index = (len(total_points) - 1)/2

print(total_points)
print(middle_index)
print(total_points[int(middle_index)])
