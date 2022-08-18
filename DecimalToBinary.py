def decimal_to_binary():
    #Clear Console
    import os
    def clear_console():
        os.system('cls')
    clear_console()

    user_input = int(input('Enter a decimal number you would like to convert to binary: '))

    binary_array = []
    calc_number = [1]

    # Finds how many decimal places the binary number will be and adds the last decimal place
    while (user_input / calc_number[len(calc_number) - 1]) >= 2:
        calc_number.append(calc_number[len(calc_number) - 1] * 2)
    binary_array.append(1)
    calc_number.reverse()

    # Ex.) if decimal number = 21 then 21 - 16 = 5 which is the divisible_remainder
    divisible_remainder = user_input - calc_number[0] 
    i = 0

    # Adds any other 1's and 0 values to the binary number until there aren't any more possible 1 values left
    while divisible_remainder != 0:
        while divisible_remainder / calc_number[i + 1] < 1:
            i += 1
            binary_array.append(0)
        divisible_remainder -= calc_number[i + 1]
        binary_array.append(1)
        i += 1

    # If the binary number is even and doesn't end with a 1, adds the remaining 0's needed to make it a complete binary number
    while len(calc_number) != len(binary_array):
        binary_array.append(0)

    print(f'\nBinary number: {binary_array}')
    print(f'What each binary number stands for: {calc_number}\n')
decimal_to_binary()