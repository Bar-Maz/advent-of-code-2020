def part_1(numbers):
    starting_index = 0
    current_index = 0
    for n in numbers[:-1]:
        remainder = 2020 - n
        starting_index += 1
        current_index = starting_index
        # numbers is a sorted list, if next element is bigger than a desired value, we skip to the next number
        while numbers[current_index] < remainder:
            current_index += 1
        # if the first number that isn't smaller than remainder is equal to remainder, we found the answer
        if numbers[current_index] == remainder:
            return([n, remainder, n*remainder])


def part_2(numbers):
    starting_index = 0
    current_index = 0
    current_inner_index = 0
    for n in numbers[:-1]:
        remainder = 2020 - n
        starting_index += 1
        current_index = starting_index
        # numbers is a sorted list, if next element is bigger than a desired value, we skip to the next number
        while numbers[current_index] < remainder:
            # we check every number from the start for each pair of 2 numbers
            current_inner_index = 0
            # we check next remainder to see the upper limit of the third number
            extra_remainder = remainder - numbers[current_index]
            # numbers is a sorted list, if next element is bigger than a desired value, we skip to the next number
            while numbers[current_inner_index] < extra_remainder:
                current_inner_index += 1
            # if the first number that isn't smaller than remainder is equal to remainder, we found the answer
            if current_inner_index not in [current_index, starting_index]:
                if numbers[current_index] + numbers[current_inner_index] == remainder:
                    ci_val = numbers[current_index]
                    cii_val = numbers[current_inner_index]
                    return([n, ci_val, cii_val, n*ci_val*cii_val])
            current_index += 1


input_file = open("input.txt", 'r')
numbers = sorted([int(i) for i in input_file.readlines()])
print("PART 1: ", part_1(numbers))
print("PART 2: ", part_2(numbers))
