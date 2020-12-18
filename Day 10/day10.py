from functools import reduce


def get_sequences_count(numbers):
    # example:
    # adapters: 1,2,4,6:
    # you can jump by 3 or less jolts
    # you can get to 6 jolts adapter only from 4 jolts adapter, so x(6) = x(4)
    # you can get to 4 jolts adapter from 1 and 2 jolts adapters, so x(4) = x(2) + x(1)
    # you can get to 2 jolts adapter from the socket and from 1 jolts adapter, so x(2) = x(1) + x(0)
    # YES, YOU CAN JUMP FROM 0 TO 2, YOU DON'T HAVE TO START FROM 1, THIS TOOK ME LIKE 2 DAYS OF
    # GETTING THE SAME  WRONG RESULTS IN DIFFERENT WAYS TO REALIZE
    # you can get to 1 jolts adapter only from the socket, so x(1) = x(0) = 1
    # x(2) = x(1) + x(0) = 2
    # x(4) = x(2) + x(1) = 3
    # x(6) = x(4) = 3
    # sequences: 0 1 2 4 6 | 0 2 4 6 | 0 1 2 6

    # so anyway, you start from the socket - joltage = 0
    sequences = {0: 1}
    # get the max joltage
    max_joltage = numbers[-1]
    # iterate over the adapters
    for num in numbers:
        # initialize each entry, so we can add to it later
        sequences[num] = 0
        # check for joltages 3 or less lower than current
        for x in range(1, 4):
            joltage = num - x
            # add to the current adapter (we don't know if given adapter exists, so we use get function to get the value)
            sequences[num] += sequences.get(joltage, 0)
    return sequences[max_joltage]


def part_1(numbers):
    # just count the differences between consecutive adapters
    diff_1 = 0
    # there's one more 3 jolts difference between the last adapter and your device, we count that one too
    diff_3 = 1
    jolts = 0
    for num in numbers:
        # check difference and increment the correct variable
        diff = num - jolts
        if diff == 1:
            diff_1 += 1
        elif diff == 3:
            diff_3 += 1
        # save current jolts for the next adapter
        jolts = num
    return diff_1 * diff_3


def part_2(lines):
    sequences_count = get_sequences_count(numbers)
    return sequences_count


with open("input.txt", 'r') as input_file:
    lines = input_file.read().splitlines()
    numbers = sorted([int(x) for x in lines])
    print("PART 1: ", part_1(numbers))
    print("PART 2: ", part_2(numbers))
