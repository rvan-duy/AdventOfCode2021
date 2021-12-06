file = open('input.txt', 'r')
lanternfish = file.read().split(',')
lanternfish = list(map(int, lanternfish))
file.close()

print("Initial state:", lanternfish)
for day in range(1, 81):
    for fish_index in range(len(lanternfish)):
        if lanternfish[fish_index] != 0:
            lanternfish[fish_index] -= 1
        else:
            lanternfish[fish_index] = 6
            lanternfish.append(8)
    print("After", day, "days:", lanternfish)
print("Total amount of lanternfish:", len(lanternfish))