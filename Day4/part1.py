def parse_data(parsed_input):
    parsed_sequence = parsed_input.pop(0)
    board_count = 0

    for i in range(len(parsed_input)):
        if parsed_input[i] == '\n':
            board_count += 1
        parsed_input[i] = parsed_input[i][:-1]

    parsed_input.pop(0)
    parsed_input.append('')
    parsed_sequence = list(parsed_sequence.split(','))
    parsed_sequence[-1] = parsed_sequence[-1][:-1]

    return parsed_sequence, parsed_input, board_count


def create_boards(unstructured_boards):
    board = []
    structured_board = []

    for element in unstructured_boards:
        if element == '':
            structured_board.append(board)
            board = []
        else:
            board.append(element)

    for i in range(len(structured_board)):
        for j in range(len(structured_board[i])):
            structured_board[i][j] = list(structured_board[i][j].split())

    print(structured_board)
    return structured_board


def find_row_and_col(number, board):
    for row in board:
        for element in row:
            if element == number:
                return row.index(), element.index()


file = open('input.txt', 'r')
file_input = file.readlines()
file.close()

sequence, boards_list, amount_of_boards = parse_data(file_input)
boards = create_boards(boards_list)

chosen_numbers = []

for number in sequence:
    chosen_numbers.append(number)
    for board in boards:
        row, col = find_row_and_col(number, board)

# print(boards)
print(find_row_and_col(63, boards[0]))

# print(sequence)

# print(amount_of_boards)
# print(boards)
