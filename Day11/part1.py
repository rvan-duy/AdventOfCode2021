# Energy level is value between 0 and 9
# Each step:
# - Energy increases by 1
# - if energy level is > 9 it flashes, increases all adjacent octopuses by 1
# -- if octopus is then > 9 it also flashes
# - if octopus has flashed, it goes back to 0

input = open('input.txt', 'r')
octopuses = input.readlines()
for i in range(len(octopuses)):
    octopuses[i] = octopuses[i][:-1]
    octopuses[i] = list(map(int, octopuses[i]))


def octopuses_are_lid(octopuses):
    for y in range(len(octopuses)):
        for x in range(len(octopuses[y])):
            if octopuses[y][x] > 9:
                return True
    return False


def turn_minus_zero(octopuses):
    for y in range(len(octopuses)):
        for x in range(len(octopuses[y])):
            if octopuses[y][x] == -1:
                octopuses[y][x] = 0


def increment_octopus(y, x, octopuses):
    if octopuses[y][x] != -1:
        octopuses[y][x] += 1


flash_count = 0
print('Starting position:')
for i in range(len(octopuses)):
    print(octopuses[i])

for day in range(1, 101):
    for y in range(len(octopuses)):
        for x in range(len(octopuses[y])):
            octopuses[y][x] += 1

    print("2:")
    for i in range(len(octopuses)):
        print(octopuses[i])

    while octopuses_are_lid(octopuses):

        print('after 0')
        for i in range(len(octopuses)):
            print(octopuses[i])

        for y in range(len(octopuses)):
            for x in range(len(octopuses[y])):
                if octopuses[y][x] > 9:
                    octopuses[y][x] = -1
                    flash_count += 1
                    if y > 0:
                        increment_octopus(y - 1, x, octopuses)
                        if x > 0:
                            increment_octopus(y - 1, x - 1, octopuses)
                        if x + 1 < len(octopuses[y]):
                            increment_octopus(y - 1, x + 1, octopuses)
                    if y + 1 < len(octopuses):
                        increment_octopus(y + 1, x, octopuses)
                        if x > 0:
                            increment_octopus(y + 1, x - 1, octopuses)
                        if x + 1 < len(octopuses[y]):
                            increment_octopus(y + 1, x + 1, octopuses)
                    if x > 0:
                        increment_octopus(y, x - 1, octopuses)
                    if x + 1 < len(octopuses[y]):
                        increment_octopus(y, x + 1, octopuses)
        print("Adrenaline:")
        for i in range(len(octopuses)):
            print(octopuses[i])

    turn_minus_zero(octopuses)

    print('After day', day, ':')
    for i in range(len(octopuses)):
        print(octopuses[i])

print('------------------------------------------------------------')
for i in range(len(octopuses)):
    print(octopuses[i])

print('After 100 steps, there have been a total of', flash_count, 'flashes.')
