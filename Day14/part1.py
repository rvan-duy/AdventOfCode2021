input_file = open('input.txt', 'r')
template = list(input_file.readline()[:-1])
input_file.readline()
insertions = input_file.read().split('\n')[:-1]
insertions = [insertion.split(' -> ') for insertion in insertions]
insertions = dict(insertions)

for step in range(40):
    i = 0
    print(step)
    while i < len(template) - 1:
        insert_value = template[i]+template[i + 1]
        template.insert(i + 1, insertions[insert_value])
        i += 2

counts = [template.count(c) for c in "ABCDEFGHIJKLMNOPQRSTUVWXYZ"]
counts.sort()
counts = [number for number in counts if number != 0]

print(type(template), counts)
print('answer:', counts[-1] - counts[0])
