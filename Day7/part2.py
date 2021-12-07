import math

file = open("input.txt", "r")
crabs = file.read().split(',')
crabs = list(map(int, crabs))

best_position = math.floor(sum(crabs) / len(crabs))
print(best_position)
total_fuel = 0
for crab in crabs:
    increment = 1
    while crab != best_position:
        if crab > best_position:
            crab -= 1
            total_fuel += increment
            increment += 1
        elif crab < best_position:
            crab += 1
            total_fuel += increment
            increment += 1


print(total_fuel)
