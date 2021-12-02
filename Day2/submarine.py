class Submarine:
    depth = 0
    horizontal = 0
    aim = 0

    def apply_instruction(self, instruction):
        if instruction[0] == 'forward':
            self.horizontal += instruction[1]
            self.depth += self.aim * instruction[1]
        elif instruction[0] == 'down':
            self.aim += instruction[1]
        elif instruction[0] == 'up':
            self.aim -= instruction[1]

    def print_position(self):
        print('Horizontal position:', self.horizontal)
        print('Depth:', self.depth)
        print('Multiplied:', self.horizontal * self.depth)
