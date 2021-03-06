import re


def part_1(passwords):
    pass_count = 0
    # each element in passwords looks like: [min, max, letter, password]
    for p in passwords:
        # we count how many times did the letter occur in this password
        letter_count = p[3].count(p[2])
        # checking if password is correct - min and max are string so we have to convert them to int
        if letter_count <= int(p[1]) and letter_count >= int(p[0]):
            pass_count += 1
    return pass_count


def part_2(passwords):
    pass_count = 0
    for p in passwords:
        # we make a new word containing two letters at given positions (1st index = 1, hence we subtract 1 from index)
        # p3 - password - p0 and p1 - indexes
        letter_count = (p[3][int(p[0])-1] + p[3][int(p[1])-1]).count((p[2]))
        # if the given letter occured once, current password is correct
        if letter_count == 1:
            pass_count += 1
    return pass_count


def part_2_v2(passwords):
    pass_count = 0
    for p in passwords:
        # we make a new word containing two letters at given positions (1st index = 1, hence we subtract 1 from index)
        # p3 - password - p0 and p1 - indexes
        # i one condition is true and another one isn't, the password is correct
        if (p[3][int(p[0])-1] == p[2]) != (p[3][int(p[1])-1] == p[2]):
            pass_count += 1
    return pass_count


with open("input.txt", 'r') as input_file:
# regex used here splits strings by '-', ' ' and ': '
    passwords = [re.split('-| |: ', i) for i in input_file.read().splitlines()]
    print("PART 1: ", part_1(passwords))
    print("PART 2: ", part_2(passwords))
    print("PART 2 v2: ", part_2_v2(passwords))
