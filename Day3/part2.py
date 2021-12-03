# Day 3: Binary Diagnostic
# What is the power consumption of the submarine?
# Author: Ruben van Duyneveldt

# life support rating = oxygen generator rating * CO2 scrubber rating
# bit criteria = oxygen generator rating: most common value in the current bit position
#                CO2 scrubber rating: least common value

def clean_input(report):
    for i in range(len(report)):
        report[i] = report[i][:-1]


def get_oxygen_rating(report):
    for bit in range(len(report[0])):

        zero_bit_count = 0
        one_bit_count = 0
        zero_bit_list = []
        one_bit_list = []

        for line in report:
            if line[bit] == '0':
                zero_bit_count += 1
                zero_bit_list.append(line)
            elif line[bit] == '1':
                one_bit_count += 1
                one_bit_list.append(line)

        if one_bit_count == zero_bit_count:
            report = one_bit_list
        elif one_bit_count > zero_bit_count:
            report = one_bit_list
        elif one_bit_count < zero_bit_count:
            report = zero_bit_list

        if len(report) == 1:
            return report[0]


def get_co2_rating(report):
    for bit in range(len(report[0])):

        zero_bit_count = 0
        one_bit_count = 0
        zero_bit_list = []
        one_bit_list = []

        for line in report:
            if line[bit] == '0':
                zero_bit_count += 1
                zero_bit_list.append(line)
            elif line[bit] == '1':
                one_bit_count += 1
                one_bit_list.append(line)

        if one_bit_count == zero_bit_count:
            report = zero_bit_list
        elif one_bit_count < zero_bit_count:
            report = one_bit_list
        elif one_bit_count > zero_bit_count:
            report = zero_bit_list

        if len(report) == 1:
            return report[0]


f = open('input.txt', 'r')
diagnostic_report = f.readlines()
f.close()

clean_input(diagnostic_report)
oxygen_rating = get_oxygen_rating(diagnostic_report)
co2_rating = get_co2_rating(diagnostic_report)
print(int(oxygen_rating, 2) * int(co2_rating, 2))
