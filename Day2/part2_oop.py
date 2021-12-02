from submarine import Submarine


def get_instructions_from_file(filename):
    file = open(filename)
    result = file.readlines()
    file.close()
    return result


instructions = get_instructions_from_file('input.txt')
uboat = Submarine()

for instruction in instructions:
    instruction, value = instruction.split(' ')
    value = int(value[:-1])
    uboat.apply_instruction(instruction, value)

uboat.print_position()
