inputty = open('input.txt', 'r')
lines = inputty.readlines()


def splitty(splitty_line):
    return splitty_line[:-1].split('|')


def find_word_of_len(words, len_to_find):
    words = words.split()
    for string in words:
        if len(string) == len_to_find:
            return string


def characters_in_string(characters, string):
    result = 0
    for c in characters:
        if c in string:
            result += 1
    if len(characters) == result:
        return True
    return False


def character_not_in_string(c, string):
    for characters in string:
        if c == characters:
            return True
    return False


def find_missing(big_number, small_number):
    return [x for x in big_number if x not in small_number][0]


def find_number_with_other_number(words, number_inside, modifier):
    words = words.split()
    for word in words:
        if len(word) == len(number_inside) + modifier and characters_in_string(number_inside, word):
            return word


def thing(big_number, small_number, display_segment):
    lst = [x for x in big_number if x not in small_number]
    for thingy in lst:
        if thingy != display_segment:
            return thingy


def find_number_without_segment(words, display_segment, word_len):
    words = words.split()
    for word in words:
        if len(word) == word_len and character_not_in_string(display_segment, word):
            return word


def find_six(words, zero, nine, word_len):
    words = words.split()
    for word in words:
        if not characters_in_string(zero, word) and not characters_in_string(nine, word) and len(word) == word_len:
            return word


def find_two(words, five, three, word_len):
    words = words.split()
    for word in words:
        if not characters_in_string(five, word) and not characters_in_string(three, word) and len(word) == word_len:
            return word


def find_zero(words, nine, one, word_len):
    words = words.split()
    for word in words:
        # print(one)
        # print(word, len(word) == word_len, not characters_in_string(nine, word), characters_in_string(one, word))
        if len(word) == word_len and not characters_in_string(nine, word) and characters_in_string(one, word):
            return word


def find_five(words, six, word_len):
    words = words.split()
    for word in words:
        if len(word) == word_len and characters_in_string(word, six):
            return word


lines = list(map(splitty, lines))
output = []
input = []
for line in lines:
    input.append(line[0])
    output.append(line[1])

appearances = [0, 0, 0, 0, 0, 0, 0, 0, 0, 0]
display_segments_list = []

i = 0
THIS_IS_FINAL_NUMBER_OFZO = 0
for input_line in input:
    display_segments = [""] * 7
    output_string = ""
    print(input_line)
    numbers = [0] * 10
    numbers[1] = find_word_of_len(input_line, 2)
    numbers[4] = find_word_of_len(input_line, 4)
    numbers[7] = find_word_of_len(input_line, 3)
    numbers[8] = find_word_of_len(input_line, 7)
    numbers[9] = find_number_with_other_number(input_line, numbers[4], 2)
    display_segments[0] = find_missing(numbers[7], numbers[1])
    display_segments[6] = find_missing(numbers[9], numbers[4][1:] + display_segments[0])
    display_segments[4] = find_missing(numbers[8], numbers[9])
    numbers[3] = find_number_with_other_number(input_line, numbers[7], 2)
    display_segments[3] = thing(numbers[3], numbers[7], display_segments[6])
    numbers[0] = find_zero(input_line, numbers[9], numbers[1], 6)
    numbers[6] = find_six(input_line, numbers[0], numbers[9], 6)
    numbers[5] = find_five(input_line, numbers[6], 5)
    numbers[2] = find_two(input_line, numbers[5], numbers[3], 5)
    output[i] = output[i].split()
    for h in range(4):
        for index in range(len(numbers)):
            if sorted(output[i][h]) == sorted(numbers[index]):
                output_string += str(index)
    THIS_IS_FINAL_NUMBER_OFZO += int(output_string)
    print(numbers, display_segments, output_string)
    i += 1

print(THIS_IS_FINAL_NUMBER_OFZO)
