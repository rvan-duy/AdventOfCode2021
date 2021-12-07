from statistics import median

file = open("input.txt", "r")
crabs = file.read().split(',')
crabs = list(map(int, crabs))

best_position = median(crabs)
total_fuel = 0
for crab in crabs:
    while crab != best_position:
        if crab > best_position:
            crab -= 1
            total_fuel += 1
        elif crab < best_position:
            crab += 1
            total_fuel += 1


print(total_fuel)
