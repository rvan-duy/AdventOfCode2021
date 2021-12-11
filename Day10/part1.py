input_file = open('input.txt', 'r')
lines = input_file.readlines()

for i in range(len(lines)):
    lines[i] = lines[i][:-1]

opening_brackets = ['(', '[', '{', '<']
closing_brackets = [')', ']', '}', '>']
total_points = 0
for i in range(len(lines)):
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
                    expected_bracket_index = opening_brackets.index(lines[i][k - 1])
                    print('Syntax error: Expected', closing_brackets[expected_bracket_index], ', but found', lines[i][k])
                    if lines[i][k] == ')':
                        total_points += 3
                    elif lines[i][k] == ']':
                        total_points += 57
                    elif lines[i][k] == '}':
                        total_points += 1197
                    elif lines[i][k] == '>':
                        total_points += 25137
                    break
                k = 0
        k += 1

print(total_points)
