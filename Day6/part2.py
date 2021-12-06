file = open('input.txt', 'r')
lanternfish = file.read().split(',')
lanternfish = list(map(int, lanternfish))
file.close()


fish_that_will_reproduce = [0, 0, 0, 0, 0, 0, 0, 0, 0]
for fish in lanternfish:
    fish_that_will_reproduce[fish] += 1

for day in range(0, 256):
    count = fish_that_will_reproduce.pop(0)
    fish_that_will_reproduce[6] += count
    fish_that_will_reproduce.append(count)

print("Sum:", sum(fish_that_will_reproduce))
