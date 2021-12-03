# Day 3: Binary Diagnostic
# What is the power consumption of the submarine?
# Author: Ruben van Duyneveldt

def clean_input(report):
    for i in range(len(report)):
        report[i] = report[i][:-1]


def get_rates_in_binary(report):
    gamma_rate_in_binary = ""
    epsilon_rate_in_binary = ""
    for bit in range(len(report[0])):

        zero_bit_count = 0
        one_bit_count = 0

        for line in report:
            if line[bit] == '0':
                zero_bit_count += 1
            elif line[bit] == '1':
                one_bit_count += 1

        if zero_bit_count > one_bit_count:
            gamma_rate_in_binary = gamma_rate_in_binary + "0"
            epsilon_rate_in_binary = epsilon_rate_in_binary + "1"
        elif zero_bit_count < one_bit_count:
            gamma_rate_in_binary = gamma_rate_in_binary + "1"
            epsilon_rate_in_binary = epsilon_rate_in_binary + "0"

    return gamma_rate_in_binary, epsilon_rate_in_binary


f = open('input.txt', 'r')
diagnostic_report = f.readlines()
f.close()

clean_input(diagnostic_report)
gamma_rate, epsilon_rate = get_rates_in_binary(diagnostic_report)
print("Power consumption:")
print(int(gamma_rate, 2) * int(epsilon_rate, 2))
