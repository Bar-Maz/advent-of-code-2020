def check_number(current, preamble):
    # find two values that sum up to the current number
    preamble = sorted(preamble)
    i1 = 0
    i2 = len(preamble) - 1
    while i1 != i2:
        if preamble[i1] + preamble[i2] > current:
            i2 -= 1
        elif preamble[i1] + preamble[i2] < current:
            i1 += 1
        else:
            return True
    return False


def find_error(lines):
    # get starting preamble
    preamble = [int(x) for x in lines[:25]]
    # get other values
    content = [int(x) for x in lines[25:]]

    for idx, number in enumerate(content): 
        # check if a number is valid
        if not check_number(number, preamble):
            # if it isn't, return it
            return (number, idx)
        # get new preamble - constant length, delete 1st value, get next
        preamble = [*preamble[1:], number]


def find_sequence(current, numbers, target, idx):
    # if sum is smaller than target, call the function with a next number in current array
    if sum(current) < target:
        return find_sequence([*current, numbers[idx+1]], numbers, target, idx+1)
    # if sum is equal to target, that's the right sequence
    if sum(current) == target:
        return current
    # don't continue if current sum is too big
    if sum(current) > target:
        return False


def part_1(lines):
    # get invalid value
    return find_error(lines)[0]


def part_2(lines):
    #get invalid value and its index
    target, index = find_error(lines)
    # get numbers up to the invalid value
    numbers = [int(x) for x in lines][:index]
    for idx, number in enumerate(numbers):
        # for every number call the find_sequence function
        seq = find_sequence([number], numbers, target, idx)
        # if it didn't return False, that's the one
        if seq:
            # return sum of biggest and smallest number in the sequence
            return min(seq) + max(seq)


input_file = open("input.txt", 'r')
lines = input_file.read().splitlines()
print("PART 1: ", part_1(lines))
print("PART 2: ", part_2(lines))
