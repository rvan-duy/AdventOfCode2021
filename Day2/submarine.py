class Submarine:
    def __init__(self):
        self.depth = 0
        self.horizontal = 0
        self.aim = 0

    def apply_instruction(self, instruction, value):
        if instruction == 'forward':
            self.horizontal += value
            self.depth += self.aim * value
        elif instruction == 'down':
            self.aim += value
        elif instruction == 'up':
            self.aim -= value

    def print_position(self):
        print('Horizontal position:', self.horizontal)
        print('Depth:', self.depth)
        print('Multiplied:', self.horizontal * self.depth)
