# Day 2: Dive!
# What do you get if you multiply your final horizontal position by your final depth?
# Author: Ruben van Duyneveldt

f = open('input.txt', 'r')
instructions = f.readlines()
f.close()

depth = 0
horizontal = 0
for instruction in instructions:

    list_item = instruction.split(' ')
    list_item[1] = list_item[1][:-1]

    if list_item[0] == 'forward':
        horizontal += int(list_item[1])
    elif list_item[0] == 'down':
        depth += int(list_item[1])
    elif list_item[0] == 'up':
        depth -= int(list_item[1])

print('Result: ' + str(horizontal * depth))
