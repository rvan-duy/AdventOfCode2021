input_file = open('vinnie_innie.txt', 'r')
template = list(input_file.readline()[:-1])
input_file.readline()
insertions = input_file.read().split('\n')[:-1]
insertions = [insertion.split(' -> ') for insertion in insertions]
insertions = dict(insertions)
pairs = dict()
letters = dict()

for i in range(len(template)):
    if template[i] in letters:
        letters[template[i]] += 1
    else:
        letters[template[i]] = 1

for i in range(len(template) - 1):
    if template[i] + template[i + 1] in pairs:
        pairs[template[i] + template[i + 1]] += 1
    else:
        pairs[template[i] + template[i + 1]] = 1
print(pairs)
print(letters)

for step in range(10):
    tmp = pairs.copy()
    for pair in pairs:
        if pairs[pair] == 0:
            continue
        count = pairs[pair]
        # print(pair, insertions[pair])
        if pair[0] + insertions[pair] in tmp:
            tmp[pair[0] + insertions[pair]] += count
        else:
            tmp[pair[0] + insertions[pair]] = count
        if insertions[pair] + pair[1] in tmp:
            tmp[insertions[pair] + pair[1]] += count
        else:
            tmp[insertions[pair] + pair[1]] = count
        if insertions[pair] in letters:
            letters[insertions[pair]] += count
        else:
            letters[insertions[pair]] = count
        tmp[pair] -= count
    print(letters)
    pairs = tmp

listy = list(letters.values())
listy.sort()
listy = [number for number in listy if number != 0]
print('answer:', listy[-1] - listy[0])
print(listy[-1], listy[0])
