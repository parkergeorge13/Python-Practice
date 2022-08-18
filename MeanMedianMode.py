def math():
    #Clear Console
    import os
    def clear_console():
        os.system('cls')
    clear_console()

    # asks the user for the number values they want to find the mean, median, and mode for.
    numbers = []
    num = ''
    while num.upper() != 'STOP':
        num = input('Type stop when you are done. What are your numbers?: ')
        if num.upper() != 'STOP':
            numbers.append(float(num))

    def mean_func():
        mean = sum(numbers) / len(numbers)
        return mean

    def median_func():
        numbers.sort()
        position = 0
        median = 0
        total = len(numbers)
        position = round(total/2)
        # if the inputted amount of values is even
        if (total % 2) == 0:
            median = (numbers[position - 1] + numbers[position]) / 2
        # if the inputted amount of values is odd
        else:
            median = numbers[position - 1]
        return median

    def mode_func():
        mode = []
        count_duplicates = []
        duplicates = []
        yes_duplicates = False
        numbers.sort()
        # takes out all of the duplicates and converts the dictionary into a list
        no_duplicates = list(set(numbers))
        # checks to see if there is a mode in the data, if there isn't then 'N/A' is displayed
        for i in range(len(numbers)):
            count_duplicates.append(numbers.count(i))
        for i in count_duplicates:
            if i > 1:
                yes_duplicates = True
        # if there is a possible mode, finds the mode or modes if there are multiple
        if yes_duplicates == True:
            # finds the amount of times each number is shown in the list
            for i in no_duplicates:   
                duplicates.append(numbers.count(i))
            # find the maximum amount of times a number is displayed in the list
            max_times = max(duplicates)
            # takes each mode and adds it to the mode list
            for i in range(len(duplicates)):
                if duplicates[i] == max_times:
                    mode.append(no_duplicates[i])
        else:
            mode.append('N/A')
        return mode

    # function calls
    mean_func()
    median_func()
    mode_func()

    # final results displayed
    clear_console()
    print(f'Initial list values: {numbers}')
    print(f'Mean = {mean_func()}')
    print(f'Median = {median_func()}')
    print(f'Mode = {mode_func()}')
math()




    
    
    


