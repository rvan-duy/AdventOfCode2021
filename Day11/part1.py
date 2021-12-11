# Energy level is value between 0 and 9
# Each step:
# - Energy increases by 1
# - if energy level is > 9 it flashes, increases all adjacent octopuses by 1
# -- if octopus is then > 9 it also flashes
# - if octopus has flashed, it goes back to 0

input = open('simple_input.txt', 'r')
octopuses = input.readlines()
for i in range(len(octopuses)):
    octopuses[i] = octopuses[i][:-1]
    octopuses[i] = list(map(int, octopuses[i]))


def reset_flashed(octopuses):
    count = 0
    for y in range(len(octopuses)):
        for x in range(len(octopuses[y])):
            if octopuses[y][x] > 9:
                octopuses[y][x] = 0
                count += 1
    return count


def octopuses_are_lid(octopuses):
    print("Started checking")
    for y in range(len(octopuses) - 1):
        print("checking:", octopuses[y])
        for x in range(len(octopuses[y])):
            if octopuses[y][x] > 9:
                return True
    return False


flash_count = 0
for step in range(0, 2):
    print('After step', step, ':')
    for i in range(len(octopuses) - 1):
        print(octopuses[i])

    for y in range(len(octopuses)):
        for x in range(len(octopuses[y])):
            octopuses[y][x] += 1

    print("Tussenstop")
    for i in range(len(octopuses) - 1):
        print(octopuses[i])

    while octopuses_are_lid(octopuses):
        print("Tussenstop_2")
        for i in range(len(octopuses) - 1):
            print(octopuses[i])

        for y in range(len(octopuses)):
            for x in range(len(octopuses[y])):
                if octopuses[y][x] > 9:
                    if y > 0:
                        octopuses[y - 1][x] += 1
                        if x > 0:
                            octopuses[y - 1][x - 1] += 1
                        if x + 1 < len(octopuses[y]):
                            octopuses[y - 1][x + 1] += 1
                    if y + 1 < len(octopuses) - 1:
                        octopuses[y + 1][x] += 1
                        if x > 0:
                            octopuses[y + 1][x - 1] += 1
                        if x + 1 < len(octopuses[y]):
                            octopuses[y + 1][x + 1] += 1
                    if x > 0:
                        octopuses[y][x - 1] += 1
                    if x + 1 < len(octopuses[y]):
                        octopuses[y][x + 1] += 1
        print("Tussenstop_3")
        for i in range(len(octopuses) - 1):
            print(octopuses[i])
        flash_count += reset_flashed(octopuses)
        print("Flash count:", flash_count)

print('------------------------------------------------------------')
for i in range(len(octopuses)):
    print(octopuses[i])

print('After 100 steps, there have been a total of', flash_count, 'flashes.')
