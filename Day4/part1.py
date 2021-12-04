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

    return structured_board


# Looks for the row and col on the board that contains the number
def find_row_and_col(number, board):
    for row in board:
        for element in row:
            if element == number:
                return board.index(row), row.index(element)
    return -1, -1


def check_horizontal_bingo(sequence, row):
    count = 0
    for element in row:
        for number in sequence:
            if number == element:
                count += 1
    if count == len(row):
        return True
    else:
        return False


def check_vertical_bingo(sequence, board, col):
    count = 0
    for row in board:
        for number in sequence:
            if number == row[col]:
                count += 1
    if count == len(board):
        return True
    else:
        return False


def calculate_sum_of_unmarked_number(board, chosen_numbers):
    sum = 0
    for row in board:
        for element in row:
            if element not in chosen_numbers:
                sum += int(element)
    return sum


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
        print(len(boards))
        if check_horizontal_bingo(chosen_numbers, board[row]):
            if len(boards) == 1:
                print("Score of last board:",
                      calculate_sum_of_unmarked_number(board, chosen_numbers) * int(chosen_numbers[-1]))
            boards.remove(board)
        elif check_vertical_bingo(chosen_numbers, board, col):
            if len(boards) == 1:
                print("Score of last board:",
                      calculate_sum_of_unmarked_number(board, chosen_numbers) * int(chosen_numbers[-1]))
            boards.remove(board)
