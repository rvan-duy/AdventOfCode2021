from submarine import Submarine

f = open('input.txt')
instructions = f.readlines()
f.close()

uboat = Submarine()

for instruction in instructions:
    list_item = instruction.split(' ')
    list_item[1] = int(list_item[1][:-1])
    uboat.apply_instruction(list_item)

uboat.print_position()
