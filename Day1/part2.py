# Day 1: Sonar Sweep
# How many measurements are larger than the previous measurement?
# Author: Ruben van Duyneveldt

file_input = open('input.txt', 'r')
lines = file_input.readlines()
file_input.close()

lines = [int(i) for i in lines]

prev_sum = 0
count = 0
array_len = len(lines)
i = 0
while i < array_len - 2:
    window_sum = lines[i] + lines[i + 1] + lines[i + 2]
    if window_sum > prev_sum:
        count += 1
    prev_sum = window_sum
    i += 1

count = count - 1
print(count)
