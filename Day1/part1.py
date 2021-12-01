# Day 1: Sonar Sweep
# How many measurements are larger than the previous measurement?
# Author: Ruben van Duyneveldt

file_input = open('input.txt', 'r')
lines = file_input.readlines()
file_input.close()

previous = 0
count = 0
for line in lines:
    if int(line) > previous:
        count = count + 1
    previous = int(line)

print(count - 1)
